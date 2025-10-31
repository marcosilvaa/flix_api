# App Directory

This directory contains the core configuration for the Django project.

## Files

### `asgi.py`

This file provides the configuration for running the project with an ASGI (Asynchronous Server Gateway Interface) compatible web server. It's used for deploying asynchronous applications.

### `settings.py`

This is the main settings file for the Django project. It includes configurations for:

- **`SECRET_KEY`**: A secret key for cryptographic signing.
- **`DEBUG`**: A boolean that turns on/off debug mode.
- **`ALLOWED_HOSTS`**: A list of strings representing the host/domain names that this Django site can serve.
- **`INSTALLED_APPS`**: A list of all Django applications that are activated in this project. This includes the built-in Django apps, `rest_framework`, and the custom apps: `genres`, `actors`, `movies`, and `reviews`.
- **`MIDDLEWARE`**: A list of middleware to be executed during the request/response processing.
- **`ROOT_URLCONF`**: The path to the root URL configuration module.
- **`TEMPLATES`**: Configuration for the template engine.
- **`DATABASES`**: Database connection settings. By default, it's configured to use SQLite.
- **`AUTH_PASSWORD_VALIDATORS`**: A list of validators used to check the strength of users' passwords.
- **`LANGUAGE_CODE`**, **`TIME_ZONE`**, **`USE_I18N`**, **`USE_TZ`**: Internationalization settings.
- **`STATIC_URL`**: The base URL to serve static files from.

### `urls.py`

This file defines the project's root URL patterns. It's the entry point for URL routing.

- **`/admin/`**: The URL for the Django admin site.
- **`/api/v1/`**: This path includes the URL patterns from the `genres`, `actors`, `movies`, and `reviews` apps, making their endpoints available under this versioned API prefix.

### `wsgi.py`

This file provides the configuration for running the project with a WSGI (Web Server Gateway Interface) compatible web server. It's used for deploying synchronous applications.
