from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Movie
from .forms import MovieForm


class MovieListView(LoginRequiredMixin, ListView):
    model = Movie

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class MovieDetailView(LoginRequiredMixin, DetailView):
    model = Movie

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class MovieCreateView(LoginRequiredMixin, CreateView):
    model = Movie
    form_class = MovieForm
    template_name = 'assessment/movie_form.html'  # Create a template for movie form

    def form_valid(self, form):
        self.object = form.save()  # Save the form data
        return redirect('legal:list')  # Redirect to the 'list' URL after successful creation


class MovieUpdateView(LoginRequiredMixin, UpdateView):
    model = Movie
    form_class = MovieForm
    template_name = 'assessment/movie_form.html'  # Use the same template for movie form

    def form_valid(self, form):
        self.object = form.save()  # Save the form data
        return redirect('legal:list')  # Redirect to the 'list' URL after successful update
