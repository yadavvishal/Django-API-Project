# Django API Project

This is a Django project implementing a RESTful API for user authentication and managing paragraphs.

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd <project-directory>


Create a virtual environment and activate it:

    -python -m venv venv
    -source venv/bin/activate  # On Windows, use venv\Scripts\activate


Install dependencies:
    -pip install -r requirements.txt

Apply migrations to create the database schema:
    -python manage.py migrate


Run the development server:
    -python manage.py runserver

The API will be accessible at http://localhost:8000/api/.


Endpoints-
    /api/register/: Register a new user.
    /api/login/: Login with username and password to get an authentication token.
    /api/users/: Retrieve all users (requires authentication token).
    /api/paragraphs/: Create a new paragraph (requires authentication token).
    /api/search-paragraphs/: Search for paragraphs containing a specific keyword (requires authentication token).


Authentication-

    Authentication is done via token-based authentication using Django REST Framework's Token Authentication.

    To access endpoints that require authentication, include an Authorization header in the request with the value Token <your-token>.


Technologies Used-
    Django
    Django REST Framework
    SQLite (default database)
    Python

```
