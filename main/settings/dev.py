from .base import * 

INSTALLED_APPS += [
    'debug_toolbar',
]

DEBUG = True

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

# SQLite:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db_test.sqlite3',
    }
}


INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]