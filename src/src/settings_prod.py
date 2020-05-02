from .settings_base import *

from dotenv import load_dotenv

load_dotenv()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'rinvio_gdp',
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PWD'),
        'HOST': 'localhost',
        'PORT': '',
    }
}

# indirizzo del server da dove saranno serviti i file statici
STATIC_URL = "https://cdn.rinviogdp.it/"

# percorso della cartella dove saranno salvati i file statici
STATIC_ROOT = "/home/cdn/public_html"

# indirizzo del server da dove saranno serviti i file media
MEDIA_URL = "https://cdn.rinviogdp.it/uploads/"

# indirizzo della cartella dove saranno salvati i file media
MEDIA_ROOT = "/home/cdn/public_html/uploads"

ALLOWED_HOSTS = ['*']

CORS_ORIGIN_ALLOW_ALL = True
