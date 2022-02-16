from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:sign_zodiac>/', views.get_info_about_zodiac_sign_number, name='horoscope-number'),
    path('<str:sign_zodiac>/', views.get_info_about_zodiac_sign, name='horoscope-name'),
]