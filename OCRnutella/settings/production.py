from . import *
import raven

INSTALLED_APPS += [
        'raven.contrib.django.raven_compat',
        ]


RAVEN_CONFIG = {
        'dsn': 'https://somethingverylong@sentry.io/216272',
        'release': raven.fetch_git_sha(os.path.dirname(os.pardir)),
        }


LOGGING = {
        'version': 1,
        'disable_existing_loggers': True,
        'root': {
            'level': 'INFO',
            'handlers': ['sentry'],
            },
            'formatters': {
            'verbose': {
                'format': '%(levelname)s %(asctime)s %(module)s '
                '%(process)d %(thread)d %(message)s'

            },
        },
        'handlers': {
            'sentry': {
                'level': 'INFO',
                'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
                'tags': {'custom-tag': 'x'},
            },
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'verbose'
            }
        },
        'loggers': {
            'django.db.backends': {
                'level': 'ERROR',
                'handlers': ['console'],
                'propagate': False,

            },
            'raven': {
                'level': 'DEBUG',
                'handlers': ['console'],
                'propagate': False,
            },
            'sentry.error': {
                'level': 'DEBUG',
                'handlers': ['console'],
                'propagate': False,
            },
        },
    }

SECRET_KEY = '5+(d#sh6)vxo4j2a+1tfe^0h-+hq6wdkx=a%bbx2@vxe$uv0h7'
DEBUG = False
ALLOWED_HOSTS = ['167.71.132.171']
DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'pur_beurre_projet',
            'HOST': 'localhost',
            'PORT': '5432',
            'USER': 'gaspf',
            'PASSWORD': 'motdepasse',
            }
        }

