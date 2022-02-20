from django.db.models import *
from django.shortcuts import render, get_object_or_404
from .models import Movie


def main(request):
    movies = Movie.objects.order_by('-rating', 'name')
    agg = movies.aggregate(Avg('budget'), Min('rating'), Max('rating'), Count('id'))
    context = {
        'movies': movies,
        'agg': agg,
        'total': movies.count()
    }
    return render(request, 'movie_app/index.html', context=context)

def detail(request, slug_movie:str):
    movie = get_object_or_404(Movie, slug=slug_movie)
    context = {
        'movie': movie,
    }
    return render(request, 'movie_app/detail.html', context=context)
