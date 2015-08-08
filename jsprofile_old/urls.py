from django.conf.urls import patterns, include, url
from jsprofile.views import UserProfileAjax

urlpatterns = patterns('jsprofile.views',   
   url(r'^profile/$', 'home',name='Jobseekerprofile'),
   url(r'^del/$','delete'),
   url(r'^update/$','update'),
   url(r'^edit_profilepic_info/$', 'edit_profilepic_info'),
   url(r'^remove_profilepic_info/$', 'remove_profilepic_info'),
   url(r'^NewProfilePictures/$','NewProfilePictures'),
   #url(r'^ajax/$', 'jsprofile.views.ajaxview'),
   url(r'^views/$', UserProfileAjax.as_view()),
   url(r'^fillcombo/(\w+)/$','fillcombo'),
  
)