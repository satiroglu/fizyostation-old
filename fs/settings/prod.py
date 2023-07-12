from fs.settings.base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'fserp',
        'USER': 'fserpdbuser',
        'PASSWORD': 'AhmoliNUZ!!;^%Fs',
        'HOST': 'localhost',
        'PORT': '',
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, "files")