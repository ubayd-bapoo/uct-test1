from django.urls import path
from .views import MovieListView, MovieDetailView, MovieCreateView, MovieUpdateView

app_name = "legal"
urlpatterns = [
    path("", MovieListView.as_view(), name="list"),
    path("<int:pk>/detail/", MovieDetailView.as_view(), name="detail"),
    path("create/", MovieCreateView.as_view(), name="create"),
    path("<int:pk>/update/", MovieUpdateView.as_view(), name="update"),
]
