# films/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.films_list, name='films_list'),  # Главная страница
    path('add/', views.add_film, name='add_film'),
]
