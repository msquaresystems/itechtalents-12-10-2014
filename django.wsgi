import os
import os.path
import sys
import site

current_directory = os.path.dirname(__file__)
homedir = os.path.dirname(current_directory)
site.addsitedir(os.path.join(homedir,
                             '.virtualenvs/itechtalents/local/'
                             'lib/python2.7/site-packages'))

os.environ['DJANGO_SETTINGS_MODULE'] = 'itechtalents.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
