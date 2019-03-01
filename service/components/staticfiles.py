import os

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

AWS_S3_ACTIVE = eval(os.environ.get('AWS_S3_ACTIVE', 'False'))

if AWS_S3_ACTIVE:
    # CDN
    CLOUDFRONT_DOMAIN = os.environ.get('CLOUDFRONT_DOMAIN')
    CLOUDFRONT_ID = os.environ.get('CLOUDFRONT_ID')

    # AWS
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
    AWS_S3_CUSTOM_DOMAIN = CLOUDFRONT_DOMAIN
    AWS_DEFAULT_ACL = None

    # STATIC
    STATICFILES_LOCATION = 'static'
    STATIC_URL = '//{}/{}/'.format(AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)
    STATICFILES_STORAGE = 'landing.storages.StaticStorage'

    # MEDIA
    MEDIAFILES_LOCATION = 'media'
    MEDIA_URL = '//{}/{}/'.format(AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
    DEFAULT_FILE_STORAGE = 'landing.storages.MediaStorage'

else:
    # STATIC
    STATIC_URL = '/static/'
    STATIC_ROOT = 'staticfiles'

    # MEDIA
    MEDIA_URL = '/media/'
    MEDIA_ROOT = 'mediafiles'
