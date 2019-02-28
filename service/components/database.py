import os
import dj_database_url

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {}
DATABASES['default'] = dj_database_url.parse(os.environ.get('DATABASE_URL'))
DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql'
