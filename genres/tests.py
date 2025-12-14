from django.test import TestCase
from django.urls import reverse
from genres.models import Genre
import json


class GenreModelTestCase(TestCase):
    """Test cases for the Genre model."""

    def test_genre_str_method(self):
        """Test that the __str__ method returns the correct string representation."""
        genre = Genre.objects.create(name='Action')
        self.assertEqual(str(genre), 'Action')


class GenreListCreateAPITestCase(TestCase):
    """Test cases for the genre list and create API endpoint."""

    def setUp(self):
        """Set up test data."""
        Genre.objects.create(name='Action')
        Genre.objects.create(name='Comedy')
        Genre.objects.create(name='Drama')

    def test_get_genres_list(self):
        """Test GET request to /genres/ returns a list of genres."""
        response = self.client.get(reverse('genre-create-list'))
        self.assertEqual(response.status_code, 200)

        data = json.loads(response.content)
        self.assertEqual(len(data), 3)
        self.assertEqual(data[0]['name'], 'Action')
        self.assertEqual(data[1]['name'], 'Comedy')
        self.assertEqual(data[2]['name'], 'Drama')

    def test_post_create_genre(self):
        """Test POST request to /genres/ creates a new genre."""
        payload = {'name': 'Horror'}
        response = self.client.post(
            reverse('genre-create-list'),
            data=json.dumps(payload),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, 201)
        data = json.loads(response.content)
        self.assertEqual(data['name'], 'Horror')
        self.assertTrue('id' in data)

        # Verify the genre was actually created in the database
        self.assertTrue(Genre.objects.filter(name='Horror').exists())
        self.assertEqual(Genre.objects.count(), 4)


class GenreDetailAPITestCase(TestCase):
    """Test cases for the genre detail API endpoint."""

    def setUp(self):
        """Set up test data."""
        self.genre = Genre.objects.create(name='Thriller')

    def test_get_genre_detail(self):
        """Test GET request to /genres/<id>/ returns the correct genre."""
        response = self.client.get(reverse('genre-detail-view', args=[self.genre.id]))
        self.assertEqual(response.status_code, 200)

        data = json.loads(response.content)
        self.assertEqual(data['id'], self.genre.id)
        self.assertEqual(data['name'], 'Thriller')

    def test_get_genre_detail_not_found(self):
        """Test GET request to /genres/<id>/ returns 404 for non-existent ID."""
        non_existent_id = 9999
        response = self.client.get(reverse('genre-detail-view', args=[non_existent_id]))
        self.assertEqual(response.status_code, 404)
