from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def get_rectangle_area(request, width: int, height: int):
    area = width * height
    return HttpResponse(f'Площадь прямоугольника размером {width}x{height} равна {area}')


def get_square_area(request, side: int):
    area = side ** 2
    return HttpResponse(f'Площадь квадрата размером {side}x{side} равна {area}')


def get_circle_area(request, radius: int):
    area = 3.14 * radius ** 2
    return HttpResponse(f'Площадь круга размером с радиусом {radius} равна {area}')


def get_rectangle_area_redirect(request, width: int, height: int):
    redirect_url = reverse('rectangle_area', args=[width, height])
    return HttpResponseRedirect(redirect_url)


def get_square_area_redirect(request, side: int):
    redirect_url = reverse('square_area', args=[side])
    return HttpResponseRedirect(redirect_url)


def get_circle_area_redirect(request, radius: int):
    redirect_url = reverse('circle_area', args=[radius])
    return HttpResponseRedirect(redirect_url)

