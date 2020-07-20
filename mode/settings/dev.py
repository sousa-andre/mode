from .common import *

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),

        'TEST': {
            'NAME': 'test.sqlite3',
            'MIRROR': 'default'
        },
    },
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
