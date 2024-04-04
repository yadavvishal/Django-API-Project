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

``
ABOUT THE PROJECT

Create a REST API that takes in multiple paragraphs of text as input, stores each paragraph
and the words to paragraph mappings on a postgreSQL database.

Custom User Model
{
"id": "xxx", // user ID (PK)
"name": "test", // user name
"email": "john@website.com" // email ID (unique)
"dob": "", // date of birth
"createdAt": "" // user created date
"modifiedAt": "" // user modified date
}

Requirements
Given a word to search for, it lists out the top 10 paragraphs in which the word is present
Few points to consider
● Tokenize the words by splitting at whitespace.
● Convert all words to lowercase.
● Index these words against the paragraph they are from.
● Generate a unique ID for every paragraph that is indexed.
● A paragraph is defined by two newline characters.

Example
Sample Input: Two paragraphs separated by two new lines
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut
labore et dolore magna aliqua.

Sample search
Input - lorem | Output: Paragraph 1 and 2 are returned
Input - Maecenas | Output: Paragraph 2

Functionality
● User should first login via the api
● All subsequent api requests must be authenticated or else they will fail
● The API should follow typical RESTful API design patterns.
● The data should be saved in the PostgreSQL DB.
● Provide proper README with usage instructions.
● Provide proper Swagger/Postman API documentation.

Tech stack
● Use Django Rest Framework
● Use a Relational DB. PostgreSQL is preferred.
