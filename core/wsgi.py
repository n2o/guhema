"""
WSGI config for core project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os, sys, site
site.addsitedir('/var/www/vhosts/guhema.com/django/guhema-venv/lib/python3.4/site-packages')
sys.path.append('/var/www/vhosts/guhema.com/httpdocs/django/core')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
