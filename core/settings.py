import os
import sys

from django.utils.translation import gettext_lazy as _

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DEBUG = False

# Import SECRET_KEY and check it
try:
    from core.settings_secret import *
except ImportError:
    print(
        "[ERROR] core/settings_secret.py not found. Please create it according to the template settings_secret.py.template")
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
ALLOWED_HOSTS = ['.guhema.com', '.guhema.de', '127.0.0.1', 'localhost', '0.0.0.0']
CSRF_TRUSTED_ORIGINS = ["https://guhema.com", "https://guhema.de", "https://www.guhema.com", "https://www.guhema.de", ]
SITE_ID = 1

# Security Settings
# SECURE_CONTENT_TYPE_NOSNIFF = True
# SECURE_BROWSER_XSS_FILTER = True
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True
# CSRF_COOKIE_HTTPONLY = True
# X_FRAME_OPTIONS = "DENY"

INSTALLED_APPS = (
    'modeltranslation',
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
    'markdownify',
    'django_forms_bootstrap',

    # Own apps
    # 'login',
    'news',
    'downloads',
    'products',
    # 'contact',
    'fairs',
)
# Application definition


MIDDLEWARE = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = "core.urls"
DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

# WSGI_APPLICATION = 'core.wsgi.application'

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
LANGUAGE_CODE = 'de'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

LANGUAGES = [
    ('de', _('German')),
    ('en', _('English')),
    ('ru', _('Russian')),
]
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

STATICFILES_DIRS = (
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
                'django.template.context_processors.i18n',
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
        'fair_detail': {'size': (600, 600), 'crop': "scale", 'quality': 100},
        'products_300': {'size': (300, 200), 'crop': "scale", 'quality': 100},
        'products_clamping': {'size': (250, 80), 'crop': "scale", 'quality': 100},
        'products_teaserimage': {'size': (262, 174), 'crop': "scale", 'quality': 100},
        'blade_image': {'size': (458, 80), 'crop': "scale", 'quality': 100},
        'blade_image_250h': {'size': (600, 250), 'crop': "scale", 'quality': 100},
        'width_1140': {'size': (1140, 2500), 'crop': "scale", 'quality': 100},
    },
}

MARKDOWNIFY = {
    "default": {
        "WHITELIST_TAGS": [
            'table',
            'thead',
            'tbody',
            'th',
            'tr',
            'td',
            'a',
            'abbr',
            'acronym',
            'b',
            'blockquote',
            'em',
            'i',
            'li',
            'ol',
            'p',
            'strong',
            'ul',
            'img',
            'style',
            'h1',
            'h2',
            'h3',
            'h4',
            'h5',
            'h6',
            'br',
            'div',
            'span'
        ],
        "MARKDOWN_EXTENSIONS": [
            'markdown.extensions.fenced_code',
            'markdown.extensions.extra',
            'markdown.extensions.md_in_html'
        ],
        "WHITELIST_ATTRS": [
            'href',
            'src',
            'alt',
            'class',
            'id',
        ]
    }
}

# Modeltranslation settings
# MODELTRANSLATION_DEFAULT_LANGUAGE = 'de'
# MODELTRANSLATION_FALLBACK_LANGUAGES = ('de',)
