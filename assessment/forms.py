from django import forms
from .models import Movie, Genre


class MovieForm(forms.ModelForm):
    genres = forms.ModelMultipleChoiceField(queryset=Genre.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Movie
        fields = ['name', 'year_released', 'genres']