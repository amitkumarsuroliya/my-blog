"""
Django settings for my_blog project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = DEBUG

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',

    'south',
    'mptt',
    'easy_thumbnails',
    'icybackup',
    'social.apps.django_app.default',

    'my_blog',
    'notes'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware'
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    'django.core.context_processors.request',

    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',

    'notes.context_processors.categories',
    'notes.context_processors.debug',
    'notes.context_processors.settings_variables'
)

AUTHENTICATION_BACKENDS = (
    'social.backends.open_id.OpenIdAuth',
    'social.backends.google.GoogleOpenId',
    'social.backends.google.GoogleOAuth2',
    'social.backends.google.GoogleOAuth',
    'social.backends.twitter.TwitterOAuth',
    'social.backends.yahoo.YahooOpenId',

    'django.contrib.auth.backends.ModelBackend',
)

ROOT_URLCONF = 'my_blog.urls'

WSGI_APPLICATION = 'my_blog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = (
    ('ru', 'Russian'),
)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'collected_static')
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.CachedStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

THUMBNAIL_ALIASES = {
    '': {
        'article': {'size': (640, 370), 'crop': True},
        'small_article': {'size': (120, 70), 'crop': True},
    },
}

SOUTH_MIGRATION_MODULES = {
    'easy_thumbnails': 'easy_thumbnails.south_migrations',
}

THUMBNAIL_SUBDIR = 'thumbs'
THUMBNAIL_QUALITY = 80

GOOGLE_ANALYTICS_ID = ''
GOOGLE_ANALYTICS_SITE = ''
YANDEX_METRIKA_ID = ''

VK_APP_ID = ''

TWITTER_ACCOUNT = ''

try:
    from local_settings import *
except:
    pass
