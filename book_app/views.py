from django.shortcuts import render


def main(request):
    return render(request, 'book_app/index.html')
