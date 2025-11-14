#!/bin/sh

set -e

uv run python manage.py collectstatic --noinput

uv run python manage.py migrate

uv run python manage.py compilemessages

mkdir -p media
cd media
umask 011
cd ..

uv run gunicorn --bind 0.0.0.0:8000 core.wsgi
