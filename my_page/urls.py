"""my_page URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

admin.site.site_header = 'Наша админка'  # Название админки
admin.site.index_title = 'Главный заголовок'  # Название заголовка

urlpatterns = [
    path('admin/', admin.site.urls),
    path('horoscope/', include('horoscope.urls')),
    path('week_days/', include('week_days.urls')),
    path('calculate_geometry/', include('geometry.urls')),
    path('movie_app/', include('movie_app.urls')),
    path('book_app/', include('book_app.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
]
