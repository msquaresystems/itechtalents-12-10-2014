import os,sys

apache_configuration = os.path.dirname(__file__)
project = os.path.dirname(apache_configuration)
workspace = os.path.dirname(project)
sys.path.append(workspace)
sys.path.append('/var/www/userreg')
sys.path.append('/var/www')

os.environ['DJANGO_SETTINGS_MODULE'] = 'userreg.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

