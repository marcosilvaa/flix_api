# Genres App

This directory contains the Django app for managing movie genres.

## Files

### `admin.py`

This file registers the `Genre` model with the Django admin interface.

- **`GenreAdmin`**: Customizes the admin view for the `Genre` model, displaying the `id` and `name` fields in the list view.

### `apps.py`

This file contains the application configuration for the `genres` app.

- **`GenresConfig`**: A subclass of `AppConfig` that defines metadata for the app, such as its name.

### `models.py`

This file defines the data model for genres.

- **`Genre`**: A Django model representing a movie genre with a single field:
    - `name` (CharField): The name of the genre.

### `serializers.py`

This file defines how `Genre` model instances are serialized to JSON.

- **`GenreSerializer`**: A `ModelSerializer` that serializes the `id` and `name` fields of the `Genre` model.

### `tests.py`

This file contains test cases for the `genres` app.

- **`GenreModelTestCase`**: Tests the string representation of the `Genre` model.
- **`GenreListCreateAPITestCase`**: Includes tests for listing all genres (`GET`) and creating a new genre (`POST`).
- **`GenreDetailAPITestCase`**: Contains tests for retrieving a single genre by its ID (`GET`) and handling cases where the genre is not found.

### `urls.py`

This file defines the URL routing for the `genres` API endpoints.

- **`/genres/`**: Maps to `GenreCreateListView` for listing and creating genres.
- **`/genres/<int:pk>/`**: Maps to `GenreRetrieveUpdateDestroyView` for retrieving, updating, and deleting a specific genre.

### `views.py`

This file contains the API views that handle requests for the `genres` app.

- **`GenreCreateListView`**: A generic view that provides `GET` (list) and `POST` (create) methods for genres.
- **`GenreRetrieveUpdateDestroyView`**: A generic view that provides `GET` (retrieve), `PUT`/`PATCH` (update), and `DELETE` methods for a single genre instance.
