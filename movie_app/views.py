from django.shortcuts import render


def main(request):
    return render(request, 'movie_app/index.html')
