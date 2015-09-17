from django.conf.urls import patterns, include, url
from registration.views import iTechTalents

from django.views.generic.simple import direct_to_template
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

#from django.views.generic.base import TemplateView
from django.conf import settings
#from registration.views import activate, register
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'userreg.views.home', name='home'),
    # url(r'^userreg/', include('userreg.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
#    urlpatterns = patterns('',
   # (r'^admin/', include('django.contrib.admin.urls')),
    url(r'^accounts/', include('registration.urls')),
    url(r'^$', iTechTalents),
   # (r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^paypal/$', 'userreg.registration.views.paypal', name='paypal-ipn'),
    url(r'^feeds/tag/(?P<bits>.*)/$', 'registration.views.rss201'),
   


#urlpatterns += patterns('',
  #(r'^accounts/profile/$', TemplateView, {'template': 'registration/profile.html'}),
)
  

  #(r'^activate/(?P<activation_key>\w+)/$', activate),
  #(r'^login/$', login, {'template_name': 'registration/login.html'}),
  #(r'^logout/$', logout, {'template_name': 'registration/logout.html'}),
  #(r'^register/$', register),
  #(r'^register/complete/$', direct_to_template, {'template': 'registration/registration_complete.html'}),



#from django.contrib.restful_model_views.restful_urls import get_restful_patterns




urlpatterns += patterns('quorum.views',
    url(r'^quorum/$', 'home'),
    url(r'^quorum/question/add/$', 'add_question'),
     url(r'^quorum/topic/(\d+)/$', 'questions'),
     url(r'^quorum/question/all/$','questions'),
    url(r'^quorum/question/(\d+)/$', 'question'),
#    url(r'^quorum/question/(\d+)/(add|del|edit)ans/$', 'set_answer'),
    #url(r'^quorum/question/(\d+)/deleteans/(\d+)/$', 'delete_answer'),
    url(r'^quorum/question/markfav/$', 'mark_as_favorite'),
    url(r'^quorum/topic/follow/$', 'mark_follow'),
    url(r'^quorum/user/(?P<username>\w+)/$', 'quorumuser'),  
    url (r'^quorum/users/$', 'quorumusers'),
   )


urlpatterns += patterns('feeds.views',
    url(r'^feeds/$','home'),
    url(r'^feeds/guest/$','guest'),
)
urlpatterns += patterns('lettertemplate.views',
     url(r'^employer/manageletters/$', 'home'),
     url(r'^employer/manageletters/(add|del|edit)/$', 'templateAddEditDel'),
     url(r'^employer/createtemplate/$','createtemplate'),
     url(r'^employer/composeletter/$', 'composeletter'),
     url(r'^employer/sendletter/$', 'sendletter'),        
     #url(r'^employer/manageletters/jquerymodel/$',direct_to_template,{'template':'employer/pages/lettertemplates/modal_window.htm'}),
)


urlpatterns += patterns('addressbook.views',
    url(r'^employer/addressbook/$','addressbk'),
)
urlpatterns += patterns('',
    url(r'^socialauth/', include('social_auth.urls')),
    url(r'^settrans/$','feeds.views.settrans'),
    #feeds.views.transhindi()
)

urlpatterns+=staticfiles_urlpatterns()


