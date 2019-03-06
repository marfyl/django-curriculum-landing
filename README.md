[![Build Status](https://travis-ci.org/marfyl/django-curriculum-landing.svg?branch=master)](https://travis-ci.org/marfyl/django-curriculum-landing) [![Requirements Status](https://requires.io/github/marfyl/django-curriculum-landing/requirements.svg?branch=master)](https://requires.io/github/marfyl/django-curriculum-landing/requirements/?branch=master) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=marfyl_django-curriculum-landing&metric=alert_status)](https://sonarcloud.io/dashboard?id=marfyl_django-curriculum-landing)



# django-curriculum-landing

This is my personal curriculum vitae website. https://marfyl.herokuapp.com/


## Features

 - A clean, simple, curriculum vitae CV resume landing page with contact form, email delivery, continuous integration and delivery with Travis CI in Heroku Cloud Application Platform, built with Python/Django.
 - ``Google Analytics`` integration if you define environ var ``ANALYTICS_CODE``.
 - You can configure ``Sendgrid`` to deliver transactional emails. You will receive an email after ContactForm is sent correctly.
 - Amazon ``CloudFront`` CDN for serving statics. Each time you run ``collectstatic`` command, static files will be uploaded to AWS S3 bucket. If you don't set this environ var Django will serve your static files.
 - Auto deploy in ``Heroku`` Cloud Application Platform with ``Travis CI`` after ``master`` branch have changes and last build was successful.

## Environment

Create a new environment, in the WORKON_HOME.
        
        pip install virtualenvwrapper
        mkvirtualenv $VIRTUAL_ENV_NAME
        
All the private or environment-dependant settings in ``settings.py`` are kept as environmental variables. 
We need to set these variables everytime we enter this virtual environment, virtualenvwrapper does this with a postactivate script. 
Edit this file:
        
        vim $VIRTUAL_ENV_NAME/bin/postactivate

## Database

``dj-database-url`` pypi package allows you to utilize the [12factor](https://www.12factor.net/backing-services) inspired ``DATABASE_URL`` environment variable to configure your Django application.

        export DATABASE_URL='postgres://[PGUSER]:[PGPASSWORD]@localhost:5432/[DB_NAME]'
        
## Google Analytics

If you want to configure your Google Analytics account, just set environ var ``ANALYTICS_CODE``.

        export ANALYTICS_CODE="XX-000000000-1"

## Amazon CloudFront

If you want to configure your AWS CloudFront account, just configure the environ var ``AWS_S3_ACTIVE``

        export AWS_S3_ACTIVE='True'
        
and then your AWS credentials.

        export AWS_ACCESS_KEY_ID=''
        export AWS_SECRET_ACCESS_KEY=''
        export AWS_STORAGE_BUCKET_NAME=''
        export AWS_S3_CUSTOM_DOMAIN=''

## Sendgrid

If you want to configure Sendgrid to receive an email each time contact form is filled correctly. 

        export SENDGRID_USERNAME=''
        export SENDGRID_PASSWORD=''

You can configure who receive the contact information with ``ADMIN_EMAIL`` environ var.
        
        export ADMIN_EMAIL='email@example.com'
        
## Heroku

Heroku is a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud. If you have both the Heroku and Travis CI command line clients installed, you can get your key, encrypt it and add it to your ``.travis.yml`` file.

If you have branch specific options, Travis CI will automatically figure out which branches to deploy from. Otherwise, it will only deploy from your master branch. You can also explicitly specify the branch to deploy from with the ``on`` option. Alternatively, you can also configure it to deploy from all branches.
        

## Requirements

All requirements are listed in ``requirements.txt``. You can install them just running:

        pip install -r requirements.txt
        
## Tests

You can run the tests manually if you want.

        python manage.py test


### Authors

- marfyl - [github@marfyl](https://github.com/marfyl/)
