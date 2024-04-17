from django.urls import path
from .views import MovieListView, MovieDetailView

app_name = "legal"
urlpatterns = [
    path("", MovieListView.as_view(), name="list"),
    path("<int:pk>/detail/", MovieDetailView.as_view(), name="detail"),
]
