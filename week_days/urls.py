from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('todo_week/<int:day>/', views.todo_week_days_number, name='todo_week_day_int'),
    path('todo_week/<str:day>/', views.todo_week_days, name='todo_week_day_str'),
]
