"""
Django settings for gojo project.

Generated by 'django-admin startproject' using Django 3.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure--zr74yfm914lr!nb9sz3y#g&#(gu!9=8csn6-)x8b77r%+7phk'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'pages.apps.PagesConfig',
    'listings.apps.ListingsConfig',
    'realtors.apps.RealtorsConfig',
    'accounts.apps.AccountsConfig',
    'contacts.apps.ContactsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'rosetta',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'gojo.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'gojo.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'gojodb',
        'USER': 'postgres',
        'PASSWORD': 'humble',
        'HOST': 'localhost'
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'gojo/static')
]
# Jet Theme
# JET_PROJECT = 'gojo'
# JET_TOKEN = 'ec66af25-443c-44a6-8a2d-fb6f2312cbed'
# Media folder Settings
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

JAZZMIN_UI_TWEAKS = {
    "theme": "simplex",
    # "dark_mode_theme": "darkly",
}
JAZZMIN_SETTINGS = {
    "site_title": "Gojo Admin",
    "site_header": "Gojo HRM",
    "site_brand": "Gojo",
    "site_logo": "img/logo white.png",
    "welcome_sign": "Welcome to the Gojo",
    "copyright": "Gojo HRM"
}
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# Messages
from django.contrib.messages import constants as messages

MESSAGE_TAGS = {
    messages.ERROR: 'danger'
}
# Email Config
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = "nuredinibrahim40@gmail.com"
EMAIL_HOST_PASSWORD = "nureboy1"
EMAIL_PORT = 587


LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale/'),
)
from django.utils.translation import gettext as gettext
from django.conf import global_settings

gettext_noop = lambda s: s
LANGUAGES = (
    ('en', gettext_noop('english')),
    ('am', gettext_noop('amharic')),
    ('tg', gettext_noop('????????????')),
    ('or', gettext_noop('Afaan Oromo')),
)

EXTRA_LANG_INFO = {
    'am': {
        'bidi': False,
        'code': 'am',
        'name': '????????????',
        'name_local': u"????????????",
    },
    'tg': {
        'bidi': False,
        'code': 'tg',
        'name': '????????????',
        'name_local': u"????????????",
    },
    'or': {
        'bidi': False,
        'code': 'or',
        'name': 'Afaan Oromo',
        'name_local': u"Afaan Oromo",
    },
}
# Add custom languages not provided by Django
import django.conf.locale

LANG_INFO = dict(django.conf.locale.LANG_INFO, **EXTRA_LANG_INFO)
django.conf.locale.LANG_INFO = LANG_INFO

# Languages using BiDi (right-to-left) layout
global_settings.LANGUAGES = global_settings.LANGUAGES + [("am", '????????????'), ("tg", '????????????'), ("or", 'Afaan Oromo')]
