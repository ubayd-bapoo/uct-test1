from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from .models import Movie, Genre
from .views import MovieListView


class MovieModelTestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='password')

        self.genre = Genre.objects.create(name='Action')
        self.movie = Movie.objects.create(name='Test Movie', year_released=2022)
        self.movie.genres.add(self.genre)

    def test_movie_creation(self):
        self.assertTrue(isinstance(self.movie, Movie))
        self.assertEqual(self.movie.name, 'Test Movie')
        self.assertEqual(self.movie.year_released, 2022)
        self.assertEqual(self.movie.genres.count(), 1)

    def test_movie_str(self):
        self.assertEqual(str(self.movie), 'Test Movie')


class MovieListViewTestCase(TestCase):
    def test_movie_list_view_authenticated(self):
        # Log in the test user
        self.client.login(username='testuser', password='password')
        print(self.client.session)  # Should print the user ID if logged in

        # Make a GET request to the movie list view
        response = self.client.get(reverse('legal:list'))

        # Print response content for debugging
        print(response.content)

        self.assertEqual(response.status_code, 302)

    def test_movie_list_view_unauthenticated(self):
        # Ensure the user is not logged in
        self.client.logout()

        # Make a GET request to the movie list view
        response = self.client.get(reverse('legal:list'))

        # Check that the response status code is 302 (redirect to login page)
        self.assertEqual(response.status_code, 302)

        # Check that the user is redirected to the login page
        self.assertRedirects(response, f"/accounts/login/?next={reverse('legal:list')}")

        # Alternatively, you can check the login URL directly
        # self.assertContains(response, 'login', status_code=302)
