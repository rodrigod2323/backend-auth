DJANGO / REACT AUTHENTICATION

This is the backend of a Django and React authentication project using DRF, JWT and a custom User model

Installation
Clone the repository.
Install dependencies with pip install -r requirements.txt.
Run migrations with python manage.py migrate.
Configuration
Set environment variables:

SECRET_KEY: Django secret key.

DEBUG: Set to True for development, False for production.

Usage

Run the development server with python manage.py runserver.

Deployment
To deploy this project, follow these steps:

Configure your production settings.
Set DEBUG to False in your environment variables.
Run python manage.py collectstatic to collect static files.
Use a WSGI server to serve your application in production.
