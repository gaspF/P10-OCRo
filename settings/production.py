
from . import *

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
