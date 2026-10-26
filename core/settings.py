import os
import sys

from django.utils.translation import gettext_lazy as _

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DEBUG = False
THUMBNAIL_DEBUG = False

# Import SECRET_KEY and check it
try:
    from core.settings_secret import *
except ImportError:
    print(
        "[ERROR] core/settings_secret.py not found. Please create it according to the template settings_secret.py.template")
    sys.exit(1)

if SECRET_KEY == "CHANGE_ME":
    print("[ERROR] Please change your secret key, stored in core/settings_secret.py")
    print("More information: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-SECRET_KEY")
    sys.exit(1)
elif len(SECRET_KEY) < 50:
    print("[WARNING] Your SECRET_KEY is too short. Please consider changing it.")

# SECURITY WARNING: don't run with debug turned on in production!
ALLOWED_HOSTS = ['.guhema.com', '.guhema.de', '127.0.0.1', 'localhost', '0.0.0.0']
CSRF_TRUSTED_ORIGINS = ["https://guhema.com", "https://guhema.de", "https://www.guhema.com", "https://www.guhema.de", ]
SITE_ID = 1

# TLS is terminated by Traefik, nginx forwards X-Forwarded-Proto
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SESSION_COOKIE_SECURE = not DEBUG
CSRF_COOKIE_SECURE = not DEBUG
SECURE_HSTS_SECONDS = 0 if DEBUG else 31536000
# HTTP -> HTTPS redirect is done by Traefik
SILENCED_SYSTEM_CHECKS = ["security.W008"]

# Without DEBUG, Django only mails errors to ADMINS; send them to the container log instead
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {"require_debug_false": {"()": "django.utils.log.RequireDebugFalse"}},
    "handlers": {"console": {"class": "logging.StreamHandler", "filters": ["require_debug_false"]}},
    "root": {"handlers": ["console"], "level": "WARNING"},
}

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
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = "core.urls"
DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

WSGI_APPLICATION = 'core.wsgi.application'

# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
LANGUAGE_CODE = 'de'
TIME_ZONE = 'UTC'
USE_I18N = True
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
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.i18n',
                'news.context_processors.news',
            ],
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

def _link_only_explicit_urls(attrs, new=False):
    """Autolink only text written as a URL, not names like "Co.KG" that look like domains."""
    if new and not attrs["_text"].lower().startswith(("http://", "https://", "www.")):
        return None
    return attrs


MARKDOWNIFY = {
    "default": {
        "LINKIFY_TEXT": {"PARSE_URLS": True, "CALLBACKS": [_link_only_explicit_urls]},
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
