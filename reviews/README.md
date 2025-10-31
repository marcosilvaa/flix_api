# Reviews App

This directory contains the Django app for managing movie reviews.

## Files

### `admin.py`

This file registers the `Review` model with the Django admin interface.

- **`ReviewAdmin`**: Customizes the admin view for the `Review` model, displaying the `id`, `movie`, `stars`, and `comment` fields.

### `apps.py`

This file contains the application configuration for the `reviews` app.

- **`ReviewsConfig`**: A subclass of `AppConfig` that defines metadata for the app, such as its name.

### `models.py`

This file defines the data model for reviews.

- **`Review`**: A Django model representing a movie review with the following fields:
    - `movie` (ForeignKey): A relationship to the `Movie` model. `on_delete=models.PROTECT` prevents the deletion of a movie if it has reviews.
    - `stars` (IntegerField): The star rating for the review, with validators ensuring the value is between 0 and 5.
    - `comment` (TextField): The text content of the review.

### `serializers.py`

This file defines how `Review` model instances are serialized.

- **`ReviewSerializers`**: A `ModelSerializer` that exposes all fields of the `Review` model.

### `tests.py`

This file is intended to contain tests for the `reviews` app. It is currently empty.

### `urls.py`

This file defines the URL routing for the `reviews` API endpoints.

- **`/reviews/`**: Maps to `ReviewCreateListView` for listing and creating reviews.
- **`/reviews/<int:pk>`**: Maps to `ReviewRetrieveUpdateDestroyView` for handling individual review instances.

### `views.py`

This file contains the API views for the `reviews` app.

- **`ReviewCreateListView`**: A generic view that provides `GET` (list) and `POST` (create) methods for reviews.
- **`ReviewRetrieveUpdateDestroyView`**: A generic view that provides `GET` (retrieve), `PUT`/`PATCH` (update), and `DELETE` methods for a single review.
