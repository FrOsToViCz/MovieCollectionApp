import pytest
from django.contrib.auth.models import User
from movies.models import Movie, Award, Person, Genre, Review, MovieAward


@pytest.fixture
def user():
    return User.objects.create_user(username='testuser', password='password')


@pytest.fixture
def genre():
    return Genre.objects.create(name='Action')


@pytest.fixture
def person():
    return Person.objects.create(
        first_name='Jack',
        last_name='Smith',
        birth_date='1998-01-01',
        role='both'
    )


@pytest.fixture
def movie(genre, person):
    movie = Movie.objects.create(
        title='Test Movie',
        description='Test Description',
        release_year=2006,
        duration_minutes=120,
        genre=genre
    )
    movie.directors.add(person)
    return movie


@pytest.fixture
def award():
    return Award.objects.create(name='Oscar')


@pytest.fixture
def movie_award(movie, award):
    return MovieAward.objects.create(
        movie=movie,
        award=award,
        category='Best Picture'
    )


@pytest.fixture
def review(user, movie):
    return Review.objects.create(
        user=user,
        movie=movie,
        rating=8,
        text='Great movie!'
    )
