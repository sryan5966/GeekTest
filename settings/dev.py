from base import *

DEBUG = True

INSTALLED_APPS.append('debug_toolbar')

MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Paypal environment variables
SITE_URL = 'http://geekstuff.herokuapp.com'
PAYPAL_NOTIFY_URL = 'http://geekstuff.herokuapp.com'
PAYPAL_RECEIVER_EMAIL = 'geeknshtuff@outlook.com'
