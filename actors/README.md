# Actors App

This directory contains the Django app for managing actors in the flix-api project.

## Files

### `admin.py`

This file registers the `Actor` model with the Django admin interface, allowing administrators to manage actor data through the admin panel.

- **`ActorAdmin`**: A ModelAdmin class that customizes the admin interface for the `Actor` model.
- **`list_display`**: Configures the columns shown in the actor list view within the admin panel (`id`, `name`, `birthdate`, `nationality`).

### `apps.py`

This file contains the application configuration for the `actors` app.

- **`ActorsConfig`**: A subclass of `AppConfig` that defines metadata for the app, such as its name.

### `models.py`

This file defines the data model for actors.

- **`NATIONALITY_CHOICES`**: A tuple defining the allowed values for the `nationality` field.
- **`Actor`**: A Django model representing an actor with the following fields:
    - `name` (CharField): The actor's name.
    - `birthdate` (DateField): The actor's birthdate.
    - `nationality` (CharField): The actor's nationality, restricted to the choices defined in `NATIONALITY_CHOICES`.

### `serializers.py`

This file defines how `Actor` model instances are converted to and from JSON.

- **`ActorSerializer`**: A `ModelSerializer` from Django Rest Framework that automatically handles serialization and deserialization for the `Actor` model, exposing all its fields.

### `tests.py`

This file is intended to contain tests for the `actors` app. It is currently empty.

### `urls.py`

This file defines the URL routing for the `actors` API endpoints.

- **`/actors/`**: Maps to `ActorCreateListView`, handling `GET` requests to list all actors and `POST` requests to create a new actor.
- **`/actors/<int:pk>/`**: Maps to `ActorRetrieveUpdateDestroyView`, handling `GET`, `PUT`, `PATCH`, and `DELETE` requests for a single actor identified by its primary key.

### `views.py`

This file contains the API views that handle the business logic for the `actors` app.

- **`ActorCreateListView`**: A generic view from Django Rest Framework that provides the functionality to list all actors and create a new one.
- **`ActorRetrieveUpdateDestroyView`**: A generic view that provides the functionality to retrieve, update, and delete a specific actor instance.
