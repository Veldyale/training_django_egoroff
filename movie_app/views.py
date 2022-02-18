from django.shortcuts import render, get_object_or_404
from .models import Movie


def main(request):
    movies = Movie.objects.order_by('-rating', 'name')
    context = {
        'movies': movies
    }
    return render(request, 'movie_app/index.html', context=context)

def detail(request, slug_movie:str):
    movie = get_object_or_404(Movie, slug=slug_movie)
    context = {
        'movie': movie
    }
    return render(request, 'movie_app/detail.html', context=context)
