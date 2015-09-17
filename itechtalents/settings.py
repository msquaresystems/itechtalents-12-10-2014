# A tesst changed in var/wwww/userreg
# Django settings for ASKBOT enabled project.
import os.path
import logging
import sys
# import askbot
import site
import djcelery
djcelery.setup_loader()

# GEOPY Settings
GEONAMES_ORG_USERNAME = 'ilayaraja'

# this line is added so that we can import pre-packaged askbot dependencies
# ASKBOT_ROOT = os.path.abspath(os.path.dirname(askbot.__file__))
# site.addsitedir(os.path.join(ASKBOT_ROOT, 'deps'))

CURRENT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = True  # set to True to enable debugging
TEMPLATE_DEBUG = False  # DEBUG  keep false when debugging jinja2 templates
INTERNAL_IPS = ('127.0.0.1',)

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

# DATABASES = {
#  'default': {
#      'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2',
#                               # 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
#      'NAME': CURRENT_DIR+'/userreg1',
#      }
#  }


DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.mysql',
          'NAME': 'itechtalents',
          'USER': 'root',
          'PASSWORD': 'DB-4c3s5',
          'HOST': '127.0.0.1',
          'PORT': '3306'
          # 'TEST_CHARSET': 'utf8',
          # 'TEST_COLLATION': 'utf8_general_ci',
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
TIME_ZONE = 'America/New_York'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

SITE_NAME = 'www.itechtalents.com'

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
PUBLIC_DOWNLOAD_URL_BACKEND = ('filetransfers.backends.default'
                               '.public_download_url')

MEDIA_ROOT = os.path.join(CURRENT_DIR, 'media')
# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

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

STATIC_ROOT = os.path.join(CURRENT_DIR, 'static')
print STATIC_ROOT, 'STATIC_ROOT'
# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"


# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
# ADMIN_MEDIA_PREFIX = '/static/admin/'
# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(CURRENT_DIR, 'media'),
    os.path.join(CURRENT_DIR, 'media/static'),
    # ('default/media', os.path.join(ASKBOT_ROOT, 'media')),

)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
    'compressor.finders.CompressorFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'sn!qh*zy_6#ule&et()q_)d)v4*ja$ati*tnqvk7vp0@5!&5nr'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    # 'askbot.skins.loaders.Loader',
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    # 'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # 'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.cache.FetchFromCacheMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    # 'askbot.middleware.anon_user.ConnectToSessionMessagesMiddleware',
    # 'askbot.middleware.forum_mode.ForumModeMiddleware',
    # 'askbot.middleware.cancel.CancelActionMiddleware',
    # 'django.middleware.transaction.TransactionMiddleware',
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
    # 'askbot.middleware.view_log.ViewLogMiddleware',
    # 'askbot.middleware.spaceless.SpacelessMiddleware',

    'django.middleware.csrf.CsrfViewMiddleware',

    'django.middleware.locale.LocaleMiddleware',

)
# ROOT_URLCONF = 'userreg.urls'
ROOT_URLCONF = 'itechtalents.urls'


# UPLOAD SETTINGS
FILE_UPLOAD_TEMP_DIR = os.path.join(
                                CURRENT_DIR,
                                'tmp'
                            ).replace('\\', '/')

FILE_UPLOAD_HANDLERS = (
    'django.core.files.uploadhandler.MemoryFileUploadHandler',
    'django.core.files.uploadhandler.TemporaryFileUploadHandler',
)
# ASKBOT_ALLOWED_UPLOAD_FILE_TYPES = ('.jpg', '.jpeg', '.gif',
#                                    '.bmp', '.png', '.tiff')
# ASKBOT_MAX_UPLOAD_FILE_SIZE = 1024 * 1024  # result in bytes
DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'


# WSGI_APPLICATION = 'userreg.wsgi.application'

TEMPLATE_DIRS = (CURRENT_DIR+'/tagging/templates',
                 CURRENT_DIR+'/quorum/templates',
                 CURRENT_DIR+'/lettertemplate/templates',
                 CURRENT_DIR+'/video_resume/templates',
                 # Put strings here, like "/home/html/django_templates"
                 # or "C:/www/django/templates".
                 # Always use forward slashes, even on Windows.
                 # Don't forget to use absolute paths, not relative paths.
                 )

INSTALLED_APPS = (
    'longerusername',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'registration',
    'django.contrib.humanize',
    'paypal.standard.ipn',
    # 'social_auth',
    'feeds',
    'quorum',
    'crispy_forms',
    'addressbook',
    'lettertemplate',
    'django.contrib.sitemaps',
    # 'debug_toolbar',
    # Optional, to enable haystack search
    # 'haystack',
    'compressor',
    # 'askbot',
    # 'askbot.deps.django_authopenid',
    # 'askbot.importers.stackexchange', #se loader
    # 'south',
    # 'askbot.deps.livesettings',
    'keyedcache',
    'robots',
    'django_countries',
    'djcelery',
    'djkombu',
    # 'followit',
    'tinymce',
    # 'group_messaging',
    'jsprofile',
    'video_resume',
)

PAYPAL_RECEIVER_EMAIL = "ekarthikkumar@gmail.com"

TEMPLATE_CONTEXT_PROCESSORS = (
    # 'askbot.context.application_settings',
    # 'django.core.context_processors.i18n',
    # 'askbot.user_messages.context_processors.user_messages',  # mst b b4 auth

    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
    'django.core.context_processors.csrf',
    )

SOCIALACCOUNT_QUERY_EMAIL = True
SOCIALACCOUNT_AUTO_SIGNUP = True
SITE_URL = 'http://www.itechtalents.com'
ACCOUNT_ACTIVATION_DAYS = 3

DEFAULT_FROM_EMAIL = 'dariemph@msquaresystems.com'
EMAIL_HOST = 'in-v3.mailjet.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'f74717f5c1d12f07112bbc10ae17843c'
EMAIL_HOST_PASSWORD = 'e3cf5c763cb150840fba317fdeb99dff'
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.

# LOGGING = {
#    'version': 1,
#    'disable_existing_loggers': False,
#    'filters': {
#        'require_debug_false': {
#            '()': 'django.utils.log.RequireDebugFalse'
#        }
#    },
#    'handlers': {
#        'mail_admins': {
#            'level': 'ERROR',
#            'filters': ['require_debug_false'],
#            'class': 'django.utils.log.AdminEmailHandler'
#        }
#    },
#    'loggers': {
#        'django.request': {
#            'handlers': ['mail_admins'],
#            'level': 'ERROR',
#            'propagate': True,
#        },
#    }
# }
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        # Include the default Django email handler for errors
        # This is what you'd get without configuring logging at all.
        'mail_admins': {
            'class': 'django.utils.log.AdminEmailHandler',
            'level': 'ERROR',
            # But the emails are plain text by default - HTML is nicer
            'include_html': True,
        },
        # Log to a text file that can be rotated by logrotate
        'logfile': {
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': CURRENT_DIR + '/log/itechtalents.log'
        },
    },
    'loggers': {
        # Again, default Django configuration to email unhandled exceptions
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        # Might as well log any errors anywhere else in Django
        'django': {
            'handlers': ['logfile'],
            'level': 'ERROR',
            'propagate': False,
        },
        # Your own app - this assumes all your logger names start with "myapp."
        'itechtalents': {
           'handlers': ['logfile'],
           'level': 'WARNING',  # Or maybe INFO or DEBUG
           'propagate': False
        },
    },
}
# LOG_FILENAME = 'askbot.log'
# logging.basicConfig(
#     filename=os.path.join(CURRENT_DIR, 'log', LOG_FILENAME),
#     level=logging.CRITICAL,
#     format=('%(pathname)s TIME: %(asctime)s '
#             'MSG: %(filename)s:%(funcName)s:%(lineno)d %(message)s'),
# )
CACHE_BACKEND = 'locmem://'
CACHE_TIMEOUT = 6000
LIVESETTINGS_CACHE_TIMEOUT = CACHE_TIMEOUT
# CACHE_PREFIX = 'askbot'  # make this unique
CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True
AUTHENTICATION_BACKENDS = (
    # 'social_auth.backends.twitter.TwitterBackend',
    # 'social_auth.backends.facebook.FacebookBackend',
    # 'social_auth.backends.google.GoogleOAuthBackend',
    # 'social_auth.backends.google.GoogleOAuth2Backend',
    # 'social_auth.backends.google.GoogleBackend',
    # 'social_auth.backends.yahoo.YahooBackend',
    # 'social_auth.backends.browserid.BrowserIDBackend',
    # 'social_auth.backends.contrib.linkedin.LinkedinBackend',
    # 'social_auth.backends.contrib.disqus.DisqusBackend',
    # 'social_auth.backends.contrib.livejournal.LiveJournalBackend',
    # 'social_auth.backends.contrib.orkut.OrkutBackend',
    # 'social_auth.backends.contrib.foursquare.FoursquareBackend',
    # 'social_auth.backends.contrib.github.GithubBackend',
    # 'social_auth.backends.contrib.vk.VKOAuth2Backend',
    # 'social_auth.backends.contrib.live.LiveBackend',
    # 'social_auth.backends.contrib.skyrock.SkyrockBackend',
    # 'social_auth.backends.contrib.yahoo.YahooOAuthBackend',
    # 'social_auth.backends.contrib.readability.ReadabilityBackend',
    # 'social_auth.backends.contrib.fedora.FedoraBackend',
    # 'social_auth.backends.OpenIDBackend',
    'django.contrib.auth.backends.ModelBackend',
    # 'askbot.deps.django_authopenid.backends.AuthBackend',
)

# ASKBOT_URL = ''  # no leading slash, default = '' empty string
# ASKBOT_TRANSLATE_URL = True  # translate specific URLs
_ = lambda v: v  # fake translation function for the login url
LOGIN_URL = ''  # '/%s%s%s' % (ASKBOT_URL,_('account/'),_('signin/'))
# LOGIN_REDIRECT_URL = ASKBOT_URL  # adjust, if needed
ALLOW_UNICODE_SLUGS = False
# ASKBOT_USE_STACKEXCHANGE_URLS = False  # mimic url scheme of stackexchange
# Celery Settings
BROKER_TRANSPORT = "djkombu.transport.DatabaseTransport"
CELERY_ALWAYS_EAGER = True

DOMAIN_NAME = ''

CSRF_COOKIE_NAME = '_csrf'
# https://docs.djangoproject.com/en/1.3/ref/contrib/csrf/
# CSRF_COOKIE_DOMAIN = DOMAIN_NAME


# FACEBOOK_APP_ID = '425549954205027'
# FACEBOOK_API_KEY = '425549954205027'
# FACEBOOK_API_SECRET = '63ddf8e6142057950a51a557ff9527eb'
# FACEBOOK_REDIRECT_URI = 'http://107.20.40.154/accounts/Profile/'
# FACEBOOK_REDIRECT_URI  http://192.168.0.34:2005/socialauth/complete/facebook
# Client ID-    fcd321fd035e7222093b
# Client Secret-  329ffbb67ca69fe5abab6539901c7aaa62204e64
# GitHub  http://192.168.0.34:2005/socialauth/complete/github

TWITTER_CONSUMER_KEY = 'oYJ7HIUoCXR6luGOF6M5NQ'
TWITTER_CONSUMER_SECRET = 'c7EBWJkEQATKasVWLa83HvWmRuPYtOa2900feNRi40'
FACEBOOK_APP_ID = '670203932991388'
FACEBOOK_API_SECRET = 'e7d8a4dcfdb33c57a83cda67b8286c23'
LINKEDIN_CONSUMER_KEY = 'n36y45tfip7i'
LINKEDIN_CONSUMER_SECRET = 'px3cE9NlgrhDSTkp'
# ORKUT_CONSUMER_KEY           = ''
# ORKUT_CONSUMER_SECRET        = ''
GOOGLE_CONSUMER_KEY = ('745969792560-d1e9mp61digh86gt0865o8ijpdmq5dba'
                       '.apps.googleusercontent.com')
GOOGLE_CONSUMER_SECRET = 'jCUOGa1qGmHLnnRR_0r4pCvZ'
GOOGLE_OAUTH2_CLIENT_ID = ('745969792560-d1e9mp61digh86gt0865o8ijpdmq5dba'
                           '.apps.googleusercontent.com')
GOOGLE_OAUTH2_CLIENT_SECRET = 'jCUOGa1qGmHLnnRR_0r4pCvZ'
# FOURSQUARE_CONSUMER_KEY      = ''
# FOURSQUARE_CONSUMER_SECRET   = ''
# VK_APP_ID                    = ''
# VK_API_SECRET                = ''
# LIVE_CLIENT_ID               = '000000004C0F8E28'
# LIVE_CLIENT_SECRET           = '75uS5WBYHZ9xCZGECbjXktHPlKmd7E7t'
# SKYROCK_CONSUMER_KEY         = ''
# SKYROCK_CONSUMER_SECRET      = ''
# YAHOO_CONSUMER_KEY = ('dj0yJmk9RXZLMVdVNTF1MVF1JmQ9WVdrOVNqRXlRM2xZTjJzbWNHb'
#                     'zlNVFEyTURFNE5qazJNZy0tJnM9Y29uc3VtZXJzZWNyZXQmeD1kYw--')
# YAHOO_CONSUMER_SECRET        = '964ee9ee1d65615c8a784bb69c632a5089308c39'
# READABILITY_CONSUMER_SECRET  = ''
# READABILITY_CONSUMER_SECRET  = ''
# GITHUB_APP_ID = 'fcd321fd035e7222093b'
# GITHUB_API_SECRET = '329ffbb67ca69fe5abab6539901c7aaa62204e64'

FACEBOOK_EXTENDED_PERMISSIONS = ['email']
FACEBOOK_PROFILE_EXTRA_PARAMS = {'locale': 'ru_RU'}
LINKEDIN_SCOPE = ['r_basicprofile', 'r_emailaddress']
LINKEDIN_EXTRA_FIELD_SELECTORS = ['email-address']
LINKEDIN_EXTRA_DATA = [('id', 'id'),
                       ('first-name', 'first_name'),
                       ('last-name', 'last_name'),
                       ('email-address', 'email_address')]
TWITTER_EXTRA_DATA = [('email', 'email')]
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/js/Dashboard/'
SOCIAL_AUTH_NEW_USER_REDIRECT_URL = '/accounts/sociallogin/'
SOCIAL_AUTH_ASSOCIATE_BY_MAIL = True
SOCIAL_AUTH_PIPELINE = (
    'social_auth.backends.pipeline.social.social_auth_user',
    'social_auth.backends.pipeline.associate.associate_by_email',
    'social_auth.backends.pipeline.user.get_username',
    'social_auth.backends.pipeline.user.create_user',
    'social_auth.backends.pipeline.social.associate_user',
    'social_auth.backends.pipeline.social.load_extra_data',
    'social_auth.backends.pipeline.user.update_user_details',
    'social_auth.backends.pipeline.misc.save_status_to_session',
    # 'app.pipeline.redirect_to_basic_user_data_form'
)


RECAPTCHA_USE_SSL = True
# HAYSTACK_SETTINGS
ENABLE_HAYSTACK_SEARCH = False
# Uncomment for multilingual setup:
# HAYSTACK_ROUTERS = ['askbot.search.haystack.routers.LanguageRouter',]

# Uncomment if you use haystack
# More info in http://django-haystack.readthedocs.org/en/latest/settings.html
# HAYSTACK_CONNECTIONS = {
#            'default': {
#                    'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
#            }
# }
TINYMCE_COMPRESSOR = True
TINYMCE_SPELLCHECKER = False
TINYMCE_JS_ROOT = os.path.join(STATIC_ROOT, 'default/media/js/tinymce/')
# TINYMCE_JS_URL = STATIC_URL + 'default/media/js/tinymce/tiny_mce.js'
TINYMCE_DEFAULT_CONFIG = {
    'plugins': 'askbot_imageuploader,askbot_attachment',
    'convert_urls': False,
    'theme': 'advanced',
    'content_css': STATIC_URL + 'default/media/style/tinymce/content.css',
    'force_br_newlines': True,
    'force_p_newlines': False,
    'forced_root_block': '',
    'mode': 'textareas',
    'oninit': "TinyMCE.onInitHook",
    'plugins': 'askbot_imageuploader,askbot_attachment',
    'theme_advanced_toolbar_location': 'top',
    'theme_advanced_toolbar_align': 'left',
    'theme_advanced_buttons1': ('bold,italic,underline,|,bullist,numlist,'
                                '|,undo,redo,|,link,unlink,'
                                'askbot_imageuploader,askbot_attachment'),
    'theme_advanced_buttons2': '',
    'theme_advanced_buttons3': '',
    'theme_advanced_path': False,
    'theme_advanced_resizing': True,
    'theme_advanced_resize_horizontal': False,
    'theme_advanced_statusbar_location': 'bottom',
    'width': '730',
    'height': '250'
}

# delayed notifications, time in seconds, 15 mins by default
NOTIFICATION_DELAY_TIME = 60 * 15

GROUP_MESSAGING = {
    'BASE_URL_GETTER_FUNCTION': 'askbot.models.user_get_profile_url',
    'BASE_URL_PARAMS': {'section': 'messages', 'sort': 'inbox'}
}

ASKBOT_MULTILINGUAL = False

ASKBOT_CSS_DEVEL = False
if 'ASKBOT_CSS_DEVEL' in locals() and ASKBOT_CSS_DEVEL:
    COMPRESS_PRECOMPILERS = (
        ('text/less', 'lessc {infile} {outfile}'),
    )

COMPRESS_JS_FILTERS = []
COMPRESS_PARSER = 'compressor.parser.HtmlParser'
JINJA2_EXTENSIONS = ('compressor.contrib.jinja2ext.CompressorExtension',)

# Use syncdb for tests instead of South migrations. Without this, some tests
# fail spuriously in MySQL.
SOUTH_TESTS_MIGRATE = False
VERIFIER_EXPIRE_DAYS = 3
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# Video Resume Settings
NIMBB = {
    "PUBLIC_KEY": "45fda06c6d",
    "PRIVATE_KEY": "43ab05019d",
    "WIDTH": 540,
    "HEIGHT": 420,
    "RECORD_TIME": 60,  # 1 minute
}
