from django.urls import path
from movies.views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    path('movies/', MovieListView.as_view(), name='movie_list'),
    path('movies/<int:pk>/', MovieDetailView.as_view(), name='movie_detail'),
    path('movies/add/', MovieCreateView.as_view(), name='movie_add'),
    path('movies/<int:pk>/edit/', MovieUpdateView.as_view(), name='movie_edit'),
    path('movies/<int:pk>/delete/', MovieDeleteView.as_view(), name='movie_delete'),

    path('casts/add/', CastCreateView.as_view(), name='cast_add'),
    path('casts/<int:pk>/edit/', CastUpdateView.as_view(), name='cast_edit'),
    path('casts/<int:pk>/delete/', CastDeleteView.as_view(), name='cast_delete'),

    path('genres/', GenreListView.as_view(), name='genre_list'),
    path('genres/add/', GenreCreateView.as_view(), name='genre_add'),
    path('genres/<int:pk>/edit/', GenreUpdateView.as_view(), name='genre_edit'),
    path('genres/<int:pk>/delete/', GenreDeleteView.as_view(), name='genre_delete'),

    path('persons/', PersonListView.as_view(), name='person_list'),
    path('persons/add/', PersonCreateView.as_view(), name='person_add'),
    path('persons/<int:pk>/edit/', PersonUpdateView.as_view(), name='person_edit'),
    path('persons/<int:pk>/delete/', PersonDeleteView.as_view(), name='person_delete'),
    path('persons/<int:pk>/', PersonDetailView.as_view(), name='person_detail'),
]
