from rest_framework import status
from rest_framework.decorators import api_view
from .models import Movie, Cinema
from .serializers import MovieSerializer
from rest_framework.response import Response


# Create your views here.


@api_view(['GET'])
def afisha_view(request):
    afisha = Movie.objects.all()
    # afisha.update(cinema_id=1)
    data = MovieSerializer(afish    a, many=True).data
    return Response(data=data)


@api_view(['GET'])
def movie_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
        # film = Cinema.objects.get(id=id)

    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data = MovieSerializer(movie).data
    return Response(data=data)
