from django import forms
from .models import Movie, Genre, Person, Cast, Award, MovieAward, Review


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'description', 'release_year', 'duration_minutes', 'genre', 'directors']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tytuł'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Opis...'}),
            'release_year': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Rok wydania'}),
            'duration_minutes': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Czas trwania'}),
            'genre': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Gatunek'}),
            'directors': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name']


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'birth_date', 'death_date', 'role']


class CastForm(forms.ModelForm):
    class Meta:
        model = Cast
        fields = ['movie', 'person', 'role_name']


class AwardForm(forms.ModelForm):
    class Meta:
        model = Award
        fields = ['name']


class MovieAwardForm(forms.ModelForm):
    class Meta:
        model = MovieAward
        fields = ['award', 'category']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['movie', 'rating', 'text']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)