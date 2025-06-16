# from django.http import JsonResponse
# from django.shortcuts import render
# from .models import Movie

# # Create your views here.


# def movie_list(request):
#     movie = Movie.objects.all()
#     data = list(movie.values())
#     # return render(request, "test.html", {"movies": data})
#     return JsonResponse(
#         {"data": data}, safe=False
#     )  # Return JSON response with movie data


# # old way to make json response
# # def details(request, id):
# #     try:
# #         movie = Movie.objects.get(id=id)
# #         data = {
# #             "id": movie.id,
# #             "name": movie.name,
# #             "description": movie.description,
# #             "active": movie.active,
# #             "release_date": movie.release_date,
# #         }
# #         return JsonResponse(data)
# #     except Movie.DoesNotExist:
# #         return JsonResponse({"error": "Movie not found"}, status=404)


# # convert data type into JSON response
# # using rest_framework  (serializers)
