from django.conf.urls import patterns, include, url, handler404, handler500
from django.contrib.auth.views import (password_reset, password_reset_done,
                                       password_change, password_change_done)

# from django.views.generic.simple import direct_to_template
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# from django.views.generic.base import TemplateView
from django.conf import settings
# from registration.views import activate, register
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from registration.views import iTechTalents
from django.conf.urls.static import static
from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^video-resume/v1/record/demo/',
        TemplateView.as_view(template_name='video-resume-v1-record.html'),
        name='video-resume-record'),
    url(r'^video-resume/v1/playback/demo/',
        TemplateView.as_view(template_name='video-resume-v1-playback.html'),
        name='video-resume-playback'),

    # Examples:
    # url(r'^$', 'views.home', name='home'),
    # url(r'^userreg/', include('foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    #    urlpatterns = patterns('',
    # (r'^admin/', include('django.contrib.admin.urls')),
    url(r'^video_resume/', include('video_resume.urls')),
    url(r'^accounts/', include('registration.urls')),
    url(r'^filesave/$', 'jsprofile.views.filesave'),
    url(r'^resumeactivation/$', 'jsprofile.views.resumeactivation'),
    url(r'^$', iTechTalents),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    # url(r'^forum/%s' % settings.ASKBOT_URL, include('askbot.urls')),
    # url(r'^followit/', include('followit.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^robots.txt$', include('robots.urls')),
    url(r'^js/', include('jsprofile.urls')),
    url(r'^deleteResume/$', 'jsprofile.views.deleteuserdetails'),
    url(r'^deleteEducation/$', 'jsprofile.views.deleteuserdetails'),
    url(r'^deleteSkill/$', 'jsprofile.views.deleteuserdetails'),
    url(r'^deleteEmp/$', 'jsprofile.views.deleteuserdetails'),
    url(r'^deleteProject/$', 'jsprofile.views.deleteuserdetails'),
    url(r'^deleteLanguage/$', 'jsprofile.views.deleteuserdetails'),
    url(r'^editresume/$', 'jsprofile.views.editresume'),
    url(r'^editpersonal/$', 'jsprofile.views.editpersonal'),
    url(r'^editsummary/$', 'jsprofile.views.editsummary'),
    url(r'^editotherdetails/$', 'jsprofile.views.editotherdetails'),
    url(r'^editsecret/$', 'jsprofile.views.editsecret'),
    url(r'^editedu/$', 'jsprofile.views.editedu'),
    url(r'^editemp/$', 'jsprofile.views.editemp'),
    url(r'^editskill/$', 'jsprofile.views.editskill'),
    url(r'^editproject/$', 'jsprofile.views.editproject'),
    url(r'^editlanguage/$', 'jsprofile.views.editlanguage'),
    url(r'^updateedu/$', 'jsprofile.views.update'),
    url(r'^updateskill/$', 'jsprofile.views.update'),
    url(r'^updateemp/$', 'jsprofile.views.update'),
    url(r'^updateproject/$', 'jsprofile.views.update'),
    url(r'^updatelanguage/$', 'jsprofile.views.update'),
    url(r'^fillcombo/(\w+)/$', 'jsprofile.views.fillcombo'),
    url(r'^remove_profilepic_info/$',
        'jsprofile.views.remove_profilepic_info'),
    url(r'^NewProfilePictures/$', 'jsprofile.views.NewProfilePictures'),
    url(r'^Edit_Profilepic/$', 'jsprofile.views.edit_profilepic_info'),
    url(r'^check_SecEmail/$', 'jsprofile.views.check_SecEmail'),


    url(  # TODO: replace with django.conf.urls.static ?
        r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:],
        'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT.replace('\\', '/')},
    ),

    url(r'^forum/account/signin/$',
        'registration.views.js_login', name='user_signin'),
    # (r'^login/$', 'django.contrib.auth.views.login'),

    # url(r'^paypal/$',
    #        'registration.views.paypal', name='paypal-ipn'),
    url(r'^paypal/notify/', include('paypal.standard.ipn.urls')),

    # urlpatterns += patterns('',
    # (r'^accounts/profile/$',
    #    TemplateView, {'template': 'registration/profile.html'}),
    (r'^accounts/password_reset/$', password_reset,
        {'template_name': 'registration/password_reset.html'}),
    (r'^accounts/password_reset_done/$', password_reset_done,
        {'template_name': 'registration/password_reset_done.html'}),
    (r'^accounts/password_change/$', password_change,
        {'template_name': 'registration/password_change.html'}),
    (r'^accounts/password_change_done/$', password_change_done,
        {'template_name': 'registration/password_change_done.html'}),

    # (r'^activate/(?P<activation_key>\w+)/$', activate),
    # (r'^login/$', login, {'template_name': 'registration/login.html'}),
    # (r'^logout/$', logout, {'template_name': 'registration/logout.html'}),
    # (r'^register/$', register),
    # (r'^register/complete/$', direct_to_template,
    #   {'template': 'registration/registration_complete.html'}),


)
# from django.contrib.restful_model_views.restful_urls
#       import get_restful_patterns
# urlpatterns += get_restful_patterns()


urlpatterns += patterns('quorum.views',
                        url(r'^quorum/$', 'home'),
                        url(r'^quorum/question/add/$', 'add_question'),
                        url(r'^quorum/topic/(\d+)/$', 'questions'),
                        url(r'^quorum/question/all/$', 'questions'),
                        url(r'^quorum/question/(\d+)/$', 'question'),

                        # url(r'^quorum/question/(\d+)/deleteans/(\d+)/$',
                        #     'delete_answer'),
                        url(r'^quorum/question/markfav/$', 'mark_as_favorite'),
                        url(r'^quorum/topic/follow/$', 'mark_follow'),
                        url(r'^quorum/user/(?P<username>\w+)/$', 'quorumuser'),
                        url(r'^quorum/users/$', 'quorumusers'),
                        )

urlpatterns += patterns('feeds.views',
                        url(r'^feeds/$', 'home'),
                        url(r'^feeds/guest/$', 'guest'),
                        )

urlpatterns += patterns('lettertemplate.views',
                        url(r'^employer/manageletters/$', 'home'),
                        url(r'^employer/manageletters/(add|del|edit)/$',
                            'templateAddEditDel'),
                        url(r'^employer/createtemplate/$', 'createtemplate'),
                        url(r'^employer/composeletter/$', 'composeletter'),
                        url(r'^employer/sendletter/$', 'sendletter'),
                        # url(r'^employer/manageletters/jquerymodel/$',
                        #    direct_to_template,
                        #    {'template':'employer/pages/lettertemplates/modal_window.htm'}),
                        )

urlpatterns += patterns('addressbook.views',
                        url(r'^employer/addressbook/$', 'addressbk'),
                        )

urlpatterns += patterns('',
                        # url(r'^socialauth/', include('social_auth.urls')),
                        url(r'^settrans/$', 'feeds.views.settrans'),
                        # feeds.views.transhindi()
                        )
urlpatterns += staticfiles_urlpatterns()
