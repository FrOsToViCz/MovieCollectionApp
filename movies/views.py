from django.shortcuts import render
from django.views.generic import TemplateView

from movies.models import Movie


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        movies = list(Movie.objects.all())
        context['movies'] = movies
        return context
