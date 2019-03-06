import os

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

AWS_S3_ACTIVE = eval(os.environ.get('AWS_S3_ACTIVE', 'False'))

if AWS_S3_ACTIVE:
    # AWS
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
    AWS_S3_CUSTOM_DOMAIN = os.environ.get('AWS_S3_CUSTOM_DOMAIN')
    AWS_DEFAULT_ACL = None
    AWS_IS_GZIPPED = False
    AWS_S3_OBJECT_PARAMETERS = {
        'CacheControl': 'max-age=864000',
    }

    # STATIC
    STATICFILES_LOCATION = 'static'
    STATIC_URL = 'https://{}/{}/'.format(AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)
    STATICFILES_STORAGE = 'landing.storages.StaticStorage'

    # MEDIA
    MEDIAFILES_LOCATION = 'media'
    MEDIA_URL = 'https://{}/{}/'.format(AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
    DEFAULT_FILE_STORAGE = 'landing.storages.MediaStorage'

else:
    # STATIC
    STATIC_URL = '/static/'
    STATIC_ROOT = 'staticfiles'

    # MEDIA
    MEDIA_URL = '/media/'
    MEDIA_ROOT = 'mediafiles'
