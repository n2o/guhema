#!/bin/sh

poetry run python manage.py collectstatic --noinput

poetry run python manage.py migrate

poetry run gunicorn --bind 0.0.0.0:8000 core.wsgi
