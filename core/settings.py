"""
Django settings for core project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

import os
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import sys

# Needed for login
import django.contrib.auth
from django.utils.translation import ugettext_lazy as _

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Import SECRET_KEY and check it
try:
    from core.settings_secret import *
except ImportError:
    print("[ERROR] core/settings_secret.py not found. Please create it according to the template settings_secret.py.template")
    sys.exit()

if SECRET_KEY == "CHANGE_ME":
    print("[ERROR] Please change your secret key, stored in core/settings_secret.py")
    print("More information: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-SECRET_KEY")
    sys.exit()
elif len(SECRET_KEY) < 50:
    print("[WARNING] Your SECRET_KEY is too short. Please consider changing it.")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['pt8lpuijgniy33u5.myfritz.net', 'cmeter.de', 'christian-meter.de', 'dori']

SITE_ID = 1

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',

    # 3rd party
    'autoslug',
    'easy_thumbnails',
    'pagedown',
    'markdown_deux',
    'captcha',
    'django_forms_bootstrap',
    'modeltranslation',

    # Own apps
    #'login',
    'news',
    'products',
    'contact',
    'fairs',
)
# Application definition


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'core.urls'

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/
LANGUAGE_CODE = 'de-de'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

LANGUAGES = [
    ('de', _('German')),
    ('en', _('English')),
    ('ru', _('Russian')),
]


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
#STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'templates/core'),
)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Configure Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.request',
            ],
            'debug': DEBUG,
        },
    },
]

# Configure Easy Thumbnails
THUMBNAIL_ALIASES = {
    '': {
        'news_front': {'size': (360, 165), 'crop': "smart", 'quality': 100},
        'news_detail': {'size': (452, 254), 'crop': "scale", 'quality': 100},
        'products_300': {'size': (300, 200), 'crop': "scale", 'quality': 100},
        'products_clamping': {'size': (250, 80), 'crop': "scale", 'quality': 100},
        'products_teaserimage': {'size': (262, 174), 'crop': "scale", 'quality': 100},
        'blade_image': {'size': (458, 80), 'crop': "scale", 'quality': 100},
        'blade_image_250h': {'size': (600, 250), 'crop': "scale", 'quality': 100},
        'width_1140': {'size': (1140, 2500), 'crop': "scale", 'quality': 100},
    },
}

# Markdown Deux Settings
MARKDOWN_DEUX_STYLES = {
    "default": {
        "extras": {
            "code-friendly": None,
        },
        # Allow raw HTML (WARNING: don't use this for user-generated
        # Markdown for your site!).
        "safe_mode": False,
    },
    "nohtml": {
        "extras": {
            "code-friendly": None,
        },
        # Allow raw HTML (WARNING: don't use this for user-generated
        # Markdown for your site!).
        "safe_mode": "escape",
    },
}

# Modeltranslation settings
MODELTRANSLATION_DEFAULT_LANGUAGE = 'de'