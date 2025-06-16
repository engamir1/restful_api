from rest_framework.response import Response
from rest_framework.decorators import api_view
from core_app.api.serializers import MovieSerializer
from core_app.models import Movie


@api_view(["GET", "POST"])
def movie_list(request):
    if request.method == "GET":
        movie = Movie.objects.all()
        serializer = MovieSerializer(movie, many=True)
        return Response(
            {"data": serializer.data}, status=200
        )  # Return JSON response with movie data

    if request.method == "POST":
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data, status=201
            )  # Return JSON response with created movie data
        else:
            return Response(
                serializer.errors, status=400
            )       


@api_view(["GET"])
def details(request, id):
    try:
        movie = Movie.objects.get(id=id)
        serializer = MovieSerializer(movie)
        return Response(serializer.data, status=200)
    except Movie.DoesNotExist:
        return Response({"error": "Movie not found"}, status=404)
