# Movies App

This directory contains the Django app for managing movies.

## Files

### `admin.py`

This file registers the `Movie` model with the Django admin interface.

- **`MovieAdmin`**: Customizes the admin view for the `Movie` model, displaying the `id`, `title`, `release_date`, and `resume` fields.

### `apps.py`

This file contains the application configuration for the `movies` app.

- **`MoviesConfig`**: A subclass of `AppConfig` that defines metadata for the app, such as its name.

### `models.py`

This file defines the data model for movies.

- **`Movie`**: A Django model representing a movie with the following fields:
    - `title` (CharField): The movie's title.
    - `genre` (ForeignKey): A relationship to the `Genre` model. `on_delete=models.PROTECT` prevents the deletion of a genre if it's associated with any movie.
    - `actors` (ManyToManyField): A relationship to the `Actor` model.
    - `release_date` (DateField): The release date of the movie.
    - `resume` (TextField): A summary of the movie.

### `serializers.py`

This file defines how `Movie` model instances are serialized.

- **`MovieModelSerializer`**: A `ModelSerializer` for the `Movie` model.
    - **`rate`**: A read-only `SerializerMethodField`. The implementation of `get_rate` appears to be a work in progress, as it filters reviews but doesn't calculate a rating.
    - **`validate_release_date`**: A custom validation method that ensures the movie's release year is not earlier than 1900. Note the discrepancy in the error message, which states 1990.
    - **`validate_resume`**: A custom validation method that limits the resume to 500 characters. Note the discrepancy in the error message, which states 200 characters.

### `tests.py`

This file is intended to contain tests for the `movies` app. It is currently empty.

### `urls.py`

This file defines the URL routing for the `movies` API endpoints.

- **`/movies/`**: Maps to `MovieCreateListView` for listing and creating movies.
- **`/movies/<int:pk>`**: Maps to `MovieRetrieveUpdateDestroyView` for handling individual movie instances.

### `views.py`

This file contains the API views for the `movies` app.

- **`MovieCreateListView`**: A generic view that provides `GET` (list) and `POST` (create) methods for movies.
- **`MovieRetrieveUpdateDestroyView`**: A generic view that provides `GET` (retrieve), `PUT`/`PATCH` (update), and `DELETE` methods for a single movie.
