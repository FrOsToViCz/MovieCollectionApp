import logging
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from movies.forms import MovieForm, PersonForm, GenreForm, CastForm, ReviewForm, AwardForm, MovieAwardForm
from movies.models import Movie, Review, Person, Genre, Cast, Award, MovieAward


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        movies = list(Movie.objects.all())
        context['movies'] = movies
        return context


class MovieListView(ListView):
    model = Movie
    template_name = 'movies/movie_list.html'
    context_object_name = 'movies'

    def get_queryset(self):
        queryset = self.request.GET.get('q')
        if queryset:
            return Movie.objects.filter(title__icontains=queryset)
        return Movie.objects.all()


class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movies/movie_detail.html'
    context_object_name = 'movie'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = Review.objects.filter(movie=self.object)
        return context


class MovieCreateView(LoginRequiredMixin, CreateView):
    model = Movie
    form_class = MovieForm
    template_name = 'movies/movie_form.html'
    success_url = reverse_lazy('movie_list')


class MovieUpdateView(LoginRequiredMixin, UpdateView):
    model = Movie
    form_class = MovieForm
    template_name = 'movies/movie_form.html'
    success_url = reverse_lazy('movie_list')


class MovieDeleteView(LoginRequiredMixin, DeleteView):
    model = Movie
    template_name = 'movies/movie_confirm_delete.html'
    success_url = reverse_lazy('movie_list')


logger = logging.getLogger(__name__)


class CastCreateView(LoginRequiredMixin, CreateView):
    model = Cast
    form_class = CastForm
    template_name = 'movies/cast_form.html'

    def form_valid(self, form):
        movie_id = self.request.GET.get('movie')
        logger.debug(f"Creating cast for movie ID: {movie_id}")
        form.instance.movie = get_object_or_404(Movie, pk=movie_id)
        return super().form_valid(form)

    def get_success_url(self):
        movie_pk = self.object.movie.pk
        logger.debug(f"Redirecting to movie detail for movie ID: {movie_pk}")
        return reverse_lazy('movie_detail', kwargs={'pk': movie_pk})


class CastUpdateView(LoginRequiredMixin, UpdateView):
    model = Cast
    form_class = CastForm
    template_name = 'movies/cast_form.html'

    def get_success_url(self):
        movie_pk = self.object.movie.pk
        logger.debug(f"Redirecting to movie detail for movie ID: {movie_pk}")
        return reverse_lazy('movie_detail', kwargs={'pk': movie_pk})


class CastDeleteView(LoginRequiredMixin, DeleteView):
    model = Cast
    template_name = 'movies/cast_confirm_delete.html'

    def get_success_url(self):
        movie_pk = self.get_object().movie.pk
        logger.debug(f"Redirecting to movie detail for movie ID: {movie_pk}")
        return reverse_lazy('movie_detail', kwargs={'pk': movie_pk})


class GenreListView(ListView):
    model = Genre
    template_name = 'movies/genre_list.html'
    context_object_name = 'genres'


class GenreCreateView(LoginRequiredMixin, CreateView):
    model = Genre
    form_class = GenreForm
    template_name = 'movies/genre_form.html'
    success_url = reverse_lazy('genre_list')


class GenreUpdateView(LoginRequiredMixin, UpdateView):
    model = Genre
    form_class = GenreForm
    template_name = 'movies/genre_form.html'
    success_url = reverse_lazy('genre_list')


class GenreDeleteView(LoginRequiredMixin, DeleteView):
    model = Genre
    template_name = 'movies/genre_confirm_delete.html'
    success_url = reverse_lazy('genre_list')


class PersonListView(ListView):
    model = Person
    template_name = 'movies/person_list.html'
    context_object_name = 'persons'

    def get_queryset(self):
        query = self.request.GET.get('q')
        role = self.request.GET.get('role')
        queryset = Person.objects.all()
        if role:
            if role == 'actor':
                return Person.objects.filter(role__in=['actor', 'both'])
            elif role == 'director':
                return Person.objects.filter(role__in=['director', 'both'])
        if query:
            queryset = queryset.filter(first_name__icontains=query) | queryset.filter(last_name__icontains=query)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for person in context['persons']:
            if person.role == 'both':
                person.display_role = 'Actor, Director'
            elif person.role == 'actor':
                person.display_role = 'Actor'
            elif person.role == 'director':
                person.display_role = 'Director'
        return context


class PersonCreateView(LoginRequiredMixin, CreateView):
    model = Person
    form_class = PersonForm
    template_name = 'movies/person_form.html'
    success_url = reverse_lazy('person_list')


class PersonUpdateView(LoginRequiredMixin, UpdateView):
    model = Person
    form_class = PersonForm
    template_name = 'movies/person_form.html'
    success_url = reverse_lazy('person_list')


class PersonDeleteView(LoginRequiredMixin, DeleteView):
    model = Person
    template_name = 'movies/person_confirm_delete.html'
    success_url = reverse_lazy('person_list')


class PersonDetailView(DetailView):
    model = Person
    template_name = 'movies/person_detail.html'
    context_object_name = 'person'


class AwardListView(ListView):
    model = Award
    template_name = 'movies/award_list.html'
    context_object_name = 'awards'


class AwardCreateView(LoginRequiredMixin, CreateView):
    model = Award
    form_class = AwardForm
    template_name = 'movies/award_form.html'
    success_url = reverse_lazy('award_list')


class AwardUpdateView(LoginRequiredMixin, UpdateView):
    model = Award
    form_class = AwardForm
    template_name = 'movies/award_form.html'
    success_url = reverse_lazy('award_list')


class AwardDeleteView(LoginRequiredMixin, DeleteView):
    model = Award
    template_name = 'movies/award_confirm_delete.html'
    success_url = reverse_lazy('award_list')


class AwardDetailView(DetailView):
    model = Award
    template_name = 'movies/award_detail.html'
    context_object_name = 'award'


class MovieAwardCreateView(LoginRequiredMixin, CreateView):
    model = MovieAward
    form_class = MovieAwardForm
    template_name = 'movies/movieaward_form.html'

    def get_initial(self):
        initial = super().get_initial()
        movie_id = self.request.GET.get('movie')
        if movie_id:
            initial['movie'] = get_object_or_404(Movie, pk=movie_id)
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        movie_id = self.request.GET.get('movie')
        if movie_id:
            context['movie'] = get_object_or_404(Movie, pk=movie_id)
        return context

    def form_valid(self, form):
        movie_id = self.request.GET.get('movie')
        form.instance.movie = get_object_or_404(Movie, pk=movie_id)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('movie_detail', kwargs={'pk': self.object.movie.pk})


class MovieAwardDeleteView(LoginRequiredMixin, DeleteView):
    model = MovieAward
    template_name = 'movies/movieaward_confirm_delete.html'
    success_url = reverse_lazy('movie_list')

    def get_success_url(self):
        movie_pk = self.get_object().movie.pk
        logger.debug(f"Redirecting to movie detail for movie ID: {movie_pk}")
        return reverse_lazy('movie_detail', kwargs={'pk': movie_pk})


class ReviewListView(ListView):
    model = Review
    template_name = 'movies/review_list.html'
    context_object_name = 'reviews'
    ordering = ['-created_at']


class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'movies/review_form.html'
    success_url = reverse_lazy('review_list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ReviewUpdateView(LoginRequiredMixin, UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = 'movies/review_form.html'
    success_url = reverse_lazy('review_list')


class ReviewDeleteView(LoginRequiredMixin, DeleteView):
    model = Review
    template_name = 'movies/review_confirm_delete.html'
    success_url = reverse_lazy('review_list')
