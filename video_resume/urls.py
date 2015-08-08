from django.conf.urls import patterns, include, url

urlpatterns = patterns('video_resume.views',   
   url(r'^create/$', 'create_video', name="create_video"),
   url(r'^view/(?P<id>\d+)/$','view_video', name="view_video"),
   #url(r'^remove/(?P<id>\d+)/$','remove_video', name="remove_video"),
)