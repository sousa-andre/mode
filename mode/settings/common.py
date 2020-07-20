import os

from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

SECRET_KEY = 'qrsuqan%n%z85-cw+8#0o=sa3x5$_ms32pjxxye2b_eibn*fu^'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.auth',

    'accounts.apps.AccountsConfig',
    'classes',
    'courses',
    'faq',
    'klass',
    'forum',
    'events',
    'polls',
    'studygroups',
    'subjects',
    'notifications',

    'mode',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'classes.middleware.LatestClass',
    'notifications.middleware.NotificationMiddleware',
]

ROOT_URLCONF = 'mode.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
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

WSGI_APPLICATION = 'mode.wsgi.application'

AUTHENTICATION_BACKENDS = [
    'accounts.backends.Backend'
]

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases


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

LANGUAGE_CODE = 'pt'
LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]
LANGUAGES = [
    ('pt', _('Portuguese'))
]

TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

DEFAULT_FROM_EMAIL = 'example@example.com'

AUTH_USER_MODEL = 'accounts.User'
LOGIN_URL = reverse_lazy('login')
LOGIN_REDIRECT_URL = LOGOUT_REDIRECT_URL = reverse_lazy('home')

MEDIA_URL = '/media/'
MEDIA_ROOT = 'media'
