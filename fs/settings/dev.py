from fs.settings.base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, "files")
STATICFILES_DIRS = [os.path.join(BASE_DIR, "files_cdn")]