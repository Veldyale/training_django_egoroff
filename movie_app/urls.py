from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='movies'),
    path('movie/<int:id_movie>', views.detail, name='movie-detail'),
]