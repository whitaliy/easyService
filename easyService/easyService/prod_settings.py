from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-bi=(0k_cdi9zzc@t!_y(v&h!dj(19uieyxzx=!*=r__@b%@m)c'


DEBUG = False

ALLOWED_HOSTS = ["127.0.0.1", "172.16.10.44"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django_db',
        'USER' : 'postgres',
        'PASSWORD' : 'postgres',
        'HOST' : 'localhost',
        'PORT' : '5432',
    }
}


# задаём адрес директории, куда командой *collectstatic* будет собрана вся статика
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_DIRS = os.path.join(BASE_DIR, "static")
STATICFILES_DIRS = [STATIC_DIR]