from django.urls import path
from .views import movie_list, details

urlpatterns = [
    path("list/", movie_list, name="movie_list"),
    path("<int:id>/", details, name="details"),
]
