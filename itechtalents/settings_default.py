# Django settings for userreg.project.

import os
def relative_project_path(*x):
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), *x)

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

DEBUG = True

TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        
#Sqlite3
#------------------------------------
'ENGINE': 'django.db.backends.sqlite3','NAME': CURRENT_DIR+'/userregdb', 

#karthik
#------------------------------------
#'ENGINE': 'django.db.backends.mysql','NAME': 'userregdb',                        

# Or path to database file if using sqlite3.
'USER': 'root',                      # Not used with sqlite3.
'PASSWORD': 'Support7',                  # Not used with sqlite3.
'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
'PORT': '3306',                      # Set to empty string for default. Not used with sqlite3.

    }
}

ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Asia/Calcutta'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

SITE_NAME = 'http://192.168.0.33:80/'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.

USE_I18N = True
LOCALE_PATHS = (CURRENT_DIR+'/locale',)
# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
PREPARE_UPLOAD_BACKEND = 'filetransfers.backends.default.prepare_upload'
SERVE_FILE_BACKEND = 'filetransfers.backends.default.serve_file'
PUBLIC_DOWNLOAD_URL_BACKEND = 'filetransfers.backends.default.public_download_url'




MEDIA_ROOT = os.path.join(CURRENT_DIR, 'media')
# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL ='var/www/userreg/tagging/media/'


ADMIN_MEDIA_PREFIX = '/media/'



'''
To Change Root Password

Navigation to your project where manage.py file lies

$ python manage.py shell

Type below Scripts

from django.contrib.auth.models import User
u = User.objects.get(username__exact='root')
u.set_password('new password')
u.save()

'''
# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"

STATIC_ROOT = 'static'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
#ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(CURRENT_DIR, 'media'),
    os.path.join(CURRENT_DIR, 'media/static'),
       
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'sn!qh*zy_6#ule&et()q_)d)v4*ja$ati*tnqvk7vp0@5!&5nr'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
)

ROOT_URLCONF = 'userreg.urls'

WSGI_APPLICATION = 'userreg.wsgi.application'


TEMPLATE_DIRS = ('tagging/templates', 'allauth/templates'
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    'registration',
    'django.contrib.humanize',
    'paypal.standard.ipn',
    #'allauth',
    #'allauth.account',
    #'allauth.socialaccount',
    #'allauth.socialaccount.providers.facebook',
    #'allauth.socialaccount.providers.google',
    #'allauth.socialaccount.providers.linkedin',
    #'allauth.socialaccount.providers.twitter',
    'social_auth',
    'feeds',
    'quorum',
    'crispy_forms',
    'addressbook',
    'lettertemplate',
    'django.contrib.markup',
    'djcelery',
    #'south',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)

PAYPAL_RECEIVER_EMAIL = "gomathi-facilitator@capsone.com"

TEMPLATE_CONTEXT_PROCESSORS=(
    'django.contrib.auth.context_processors.auth', 
    'django.core.context_processors.debug', 
    'django.core.context_processors.i18n', 
    'django.core.context_processors.media', 
    'django.core.context_processors.static', 
    'django.core.context_processors.tz', 
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
   

    )




SOCIALACCOUNT_QUERY_EMAIL =True
SOCIALACCOUNT_AUTO_SIGNUP =True


FACEBOOK_APP_ID = '425549954205027'
FACEBOOK_API_KEY = '425549954205027'
FACEBOOK_API_SECRET = '63ddf8e6142057950a51a557ff9527eb'
FACEBOOK_REDIRECT_URI = 'http://192.168.0.32:2002/accounts/SocialPassReset/'
FACEBOOK_LOGIN_DEFAULT_REDIRECT = 'http://192.168.0.32:2002/accounts/SocialPassReset/'

LOGIN_REDIRECT_URL = 'http://192.168.0.32:2002/accounts/SocialPassReset/'

EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = 'http://192.168.0.32:2002/accounts/login/'


SITE_URL='http://ec2-50-17-89-5.compute-1.amazonaws.com/'
ACCOUNT_ACTIVATION_DAYS=3
PASSWORDRESET_ACTIVATION_DAYS=1
EMAIL_HOST='mail.capsone.com'
EMAIL_PORT=25
EMAIL_HOST_USER='karthik@capsone.com'
EMAIL_HOST_PASSWORD='19jan1988'
EMAIL_USE_TLS=True

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

AUTHENTICATION_BACKENDS = (
    'social_auth.backends.twitter.TwitterBackend',
    'social_auth.backends.facebook.FacebookBackend',
    'social_auth.backends.google.GoogleOAuthBackend',
    'social_auth.backends.google.GoogleOAuth2Backend',
    'social_auth.backends.google.GoogleBackend',
    #'social_auth.backends.yahoo.YahooBackend',
    #'social_auth.backends.browserid.BrowserIDBackend',
    'social_auth.backends.contrib.linkedin.LinkedinBackend',
    #'social_auth.backends.contrib.disqus.DisqusBackend',
    #'social_auth.backends.contrib.livejournal.LiveJournalBackend',
    #'social_auth.backends.contrib.orkut.OrkutBackend',
    #'social_auth.backends.contrib.foursquare.FoursquareBackend',
    #'social_auth.backends.contrib.github.GithubBackend',
    #'social_auth.backends.contrib.vk.VKOAuth2Backend',
    'social_auth.backends.contrib.live.LiveBackend',
    #'social_auth.backends.contrib.skyrock.SkyrockBackend',
    #'social_auth.backends.contrib.yahoo.YahooOAuthBackend',
    #'social_auth.backends.contrib.readability.ReadabilityBackend',
    #'social_auth.backends.contrib.fedora.FedoraBackend',
    #'social_auth.backends.OpenIDBackend',
    'django.contrib.auth.backends.ModelBackend',
)

#FACEBOOK_APP_ID = '425549954205027'
#FACEBOOK_API_KEY = '425549954205027'
#FACEBOOK_API_SECRET = '63ddf8e6142057950a51a557ff9527eb'
#FACEBOOK_REDIRECT_URI = 'http://107.20.40.154/accounts/Profile/'


#FACEBOOK_REDIRECT_URI  http://192.168.0.34:2005/socialauth/complete/facebook


#Client ID-    fcd321fd035e7222093b
#Client Secret-  329ffbb67ca69fe5abab6539901c7aaa62204e64
#GitHub  http://192.168.0.34:2005/socialauth/complete/github

TWITTER_CONSUMER_KEY         = 'oYJ7HIUoCXR6luGOF6M5NQ'
TWITTER_CONSUMER_SECRET      = 'c7EBWJkEQATKasVWLa83HvWmRuPYtOa2900feNRi40'
FACEBOOK_APP_ID              = '425549954205027'
FACEBOOK_API_SECRET          = '63ddf8e6142057950a51a557ff9527eb'
LINKEDIN_CONSUMER_KEY        = 'n36y45tfip7i'
LINKEDIN_CONSUMER_SECRET     = 'px3cE9NlgrhDSTkp'
ORKUT_CONSUMER_KEY           = ''
ORKUT_CONSUMER_SECRET        = ''
GOOGLE_CONSUMER_KEY          = '750553941644.apps.googleusercontent.com'
GOOGLE_CONSUMER_SECRET       = 'MXE9thlzUPISUbyl594gplZr'
GOOGLE_OAUTH2_CLIENT_ID      = ''
GOOGLE_OAUTH2_CLIENT_SECRET  = ''
FOURSQUARE_CONSUMER_KEY      = ''
FOURSQUARE_CONSUMER_SECRET   = ''
VK_APP_ID                    = ''
VK_API_SECRET                = ''
LIVE_CLIENT_ID               = '000000004C0F8E28'
LIVE_CLIENT_SECRET           = '75uS5WBYHZ9xCZGECbjXktHPlKmd7E7t'
SKYROCK_CONSUMER_KEY         = ''
SKYROCK_CONSUMER_SECRET      = ''
YAHOO_CONSUMER_KEY           = 'dj0yJmk9RXZLMVdVNTF1MVF1JmQ9WVdrOVNqRXlRM2xZTjJzbWNHbzlNVFEyTURFNE5qazJNZy0tJnM9Y29uc3VtZXJzZWNyZXQmeD1kYw--'
YAHOO_CONSUMER_SECRET        = '964ee9ee1d65615c8a784bb69c632a5089308c39'
READABILITY_CONSUMER_SECRET  = ''
READABILITY_CONSUMER_SECRET  = ''
GITHUB_APP_ID = 'fcd321fd035e7222093b'
GITHUB_API_SECRET = '329ffbb67ca69fe5abab6539901c7aaa62204e64'


#FACEBOOK_EXTENDED_PERMISSIONS = ['email']
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/accounts/Profile/'
SOCIAL_AUTH_NEW_USER_REDIRECT_URL = '/accounts/sociallogin/'

import djcelery
djcelery.setup_loader()
BROKER_URL = 'amqp://guest:guest@localhost:5672/'
