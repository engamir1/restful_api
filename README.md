1- create app 
2- register in settings 
3- manage.py migrate & cretasuperuser 
<!-- Here are the key differences between serializer.Serializer and serializer.ModelSerializer in Django Rest Framework:

 -->

Here are the key differences between `serializer.Serializer` and `serializer.ModelSerializer` in Django Rest Framework:

1. **Basic Structure**:

```python
# Regular Serializer
from rest_framework import serializers

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)
    description = serializers.CharField()
    release_date = serializers.DateField()

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.release_date = validated_data.get('release_date', instance.release_date)
        instance.save()
        return instance
```

```python
# ModelSerializer
from rest_framework import serializers

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'release_date']
        # or fields = '__all__' for all fields
```

2. **Key Differences**:

- **Code Volume**: ModelSerializer requires less code as it automatically generates:
  - Fields based on model
  - Create/update methods
  - Field validations
  - Nested relationships

- **Customization**:
  - `Serializer`: More control over fields and validation
  - `ModelSerializer`: Less control but faster development

- **Use Cases**:
  - `Serializer`: Use when data structure differs from models
  - `ModelSerializer`: Use when serializer maps directly to model

3. **Features of ModelSerializer**:

- Automatic field generation
- Automatic validators
- Default `.create()` and `.update()`
- Nested relationship handling
- Model-specific field arguments (`unique`, `blank`, etc.)

4. **Example with Relations**:

```python
# Regular Serializer with relations
class DirectorSerializer(serializers.Serializer):
    name = serializers.CharField()
    movies = MovieSerializer(many=True)

    def create(self, validated_data):
        movies_data = validated_data.pop('movies')
        director = Director.objects.create(**validated_data)
        for movie_data in movies_data:
            Movie.objects.create(director=director, **movie_data)
        return director
```

```python
# ModelSerializer with relations
class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['name', 'movies']
        depth = 1  # Automatically handles nested relations
```

Choose based on your needs:
- Use `ModelSerializer` when:
  - Your serializer matches your model structure
  - You want rapid development
  - Default create/update behavior is sufficient

- Use `Serializer` when:
  - You need custom data structure
  - Complex validation logic
  - Non-model data handling
  - Complete control over serialization




# Class-Based Views vs Function-Based Views in DRF

## 1. Basic Structure Comparison

### Function-Based View
````python
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def movie_list(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
````

### Class-Based View
````python
# filepath: views.py
from rest_framework import generics

class MovieList(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
````

## 2. Key Differences

| Feature | Function-Based Views | Class-Based Views |
|---------|---------------------|-------------------|
| Code Length | More verbose | More concise |
| Readability | Simple for basic operations | Better for complex logic |
| Inheritance | No inheritance | Supports inheritance |
| Reusability | Less reusable | More reusable |
| HTTP Methods | Manual handling | Built-in method handlers |
| Learning Curve | Easier to learn | Steeper learning curve |

## 3. Common Use Cases

### Function-Based Views
- Simple CRUD operations
- Custom API endpoints
- Quick prototyping
- Specific business logic

### Class-Based Views
- Standard CRUD operations
- Complex filtering/pagination
- Permission handling
- Mixins and inheritance

## 4. Advanced Example Comparison

### Function-Based View with Features
````python
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def movie_list(request):
    # Pagination
    page = request.GET.get('page', 1)
    page_size = request.GET.get('size', 10)
    
    # Filtering
    genre = request.GET.get('genre')
    queryset = Movie.objects.all()
    if genre:
        queryset = queryset.filter(genre=genre)
    
    # Pagination logic
    paginator = Paginator(queryset, page_size)
    movies = paginator.page(page)
    
    serializer = MovieSerializer(movies, many=True)
    return Response({
        'data': serializer.data,
        'total_pages': paginator.num_pages,
        'current_page': page
    })
````

### Class-Based View with Features
````python
class MovieList(generics.ListAPIView):
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination
    
    def get_queryset(self):
        queryset = Movie.objects.all()
        genre = self.request.query_params.get('genre')
        if genre:
            queryset = queryset.filter(genre=genre)
        return queryset
````

## 5. When to Use Each

**Use Function-Based Views when:**
- Building simple endpoints
- Need full control over logic
- Specific, non-reusable functionality
- Quick prototyping

**Use Class-Based Views when:**
- Building standard CRUD operations
- Need built-in features (pagination, filtering)
- Want to reuse code through inheritance
- Working with complex permissions
- Need consistent API patterns

The choice between CBV and FBV often depends on your specific requirements and project complexity. CBVs are generally preferred in DRF due to their built-in functionality and reusability.

