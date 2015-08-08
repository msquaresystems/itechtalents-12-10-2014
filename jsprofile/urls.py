from django.conf.urls import patterns, include, url
from jsprofile.views import UserProfileAjax

urlpatterns = patterns('jsprofile.views',   
   url(r'^(?P<link>\w+)/$', 'home',name='Jobseekerprofile'),
   url(r'^del/$','delete'),
   url(r'^update/$','update'),
   url(r'^views/$', UserProfileAjax.as_view()),
   # url(r'^fillcombo/(\w+)/$','fillcombo'),
)
