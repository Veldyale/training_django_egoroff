from django.shortcuts import render, get_object_or_404
from .models import Movie


def main(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies
    }
    return render(request, 'movie_app/index.html', context=context)

def detail(request, id_movie:int):
    movie = get_object_or_404(Movie, id=id_movie)
    context = {
        'movie': movie
    }
    return render(request, 'movie_app/detail.html', context=context)
