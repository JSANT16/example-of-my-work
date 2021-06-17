#!/bin/bash

# Collect static files
# ls frontend/build
# echo "Collect static files"
# python manage.py collectstatic --noinput

# Apply python makemigrations
echo "Apply python makemigrations"
python manage.py makemigrations

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# Start server
echo "Test code"
python manage.py test

# Start server
echo "Starting server"
python manage.py runserver 0.0.0.0:8000