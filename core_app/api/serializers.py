from rest_framework import serializers

from core_app.models import Movie


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=500)
    active = serializers.BooleanField()
    # release_date = serializers.DateField(required=False)

    def create(self, validated_data):
        
        return Movie.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get("name", instance.name)
    #     instance.description = validated_data.get("description", instance.description)
    #     instance.active = validated_data.get("active", instance.active)
    #     instance.release_date = validated_data.get(
    #         "release_date", instance.release_date
    #     )
    #     instance.save()
    #     return instance
