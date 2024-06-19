from django.db import models
from django.contrib.auth.models import User


class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Person(models.Model):
    ACTOR = 'actor'
    DIRECTOR = 'director'
    BOTH = 'both'
    ROLE_CHOICES = [
        (ACTOR, 'Actor'),
        (DIRECTOR, 'Director'),
        (BOTH, 'Both'),
    ]

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birth_date = models.DateField()
    death_date = models.DateField(null=True, blank=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default=ACTOR)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_year = models.PositiveIntegerField()
    duration_minutes = models.PositiveIntegerField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    directors = models.ManyToManyField(Person, related_name='directed_movies',
                                       limit_choices_to={'role__in': ['director', 'both']})

    def __str__(self):
        return f"{self.title} ({self.release_year})"


class Cast(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, limit_choices_to={'role__in': ['actor', 'both']})
    role_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.person} as {self.role_name} in {self.movie}"


class Award(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class MovieAward(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    award = models.ForeignKey(Award, on_delete=models.CASCADE)
    category = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.movie} - {self.award} ({self.category})"


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 11)])
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review of {self.movie} by {self.user}'
