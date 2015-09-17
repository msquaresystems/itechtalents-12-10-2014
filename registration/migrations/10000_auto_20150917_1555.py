# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('registration', '9999_set_site_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='activationcode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('key', models.CharField(max_length=50)),
                ('key_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BComments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comments', models.TextField(blank=True)),
                ('commentpost', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('btitle', models.CharField(max_length=250, blank=True)),
                ('bimage', models.ImageField(null=True, upload_to=b'BlogImage', blank=True)),
                ('bcontent', models.TextField(blank=True)),
                ('bposted', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='BlogTopics',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('blogtopic', models.CharField(max_length=100, blank=True)),
                ('blogImgurl', models.ImageField(upload_to=b'BlogTopicImage', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='checksocial_login',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('loginflag', models.BooleanField(default=False)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Emp_Gallery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('galpictitle', models.CharField(max_length=100)),
                ('galpic', models.ImageField(null=True, upload_to=b'gallerypicture', blank=True)),
                ('emp', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Emp_Gallery_video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('galvideotitle', models.CharField(max_length=100)),
                ('galvideo', models.ImageField(null=True, upload_to=b'galleryvideo', blank=True)),
                ('emp', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='emp_subscribed_packs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pack_activate', models.DateTimeField()),
                ('pack_expire', models.DateTimeField()),
                ('employer', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='employerkeyskills',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keyskills', models.CharField(max_length=50)),
                ('emp', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EmployerReg_Form',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('companytype', models.CharField(max_length=100)),
                ('contactno', models.CharField(max_length=100)),
                ('contactperson', models.CharField(max_length=100)),
                ('companyurl', models.URLField()),
                ('companyname', models.CharField(max_length=100)),
                ('companylogo', models.ImageField(null=True, upload_to=b'companylogo', blank=True)),
                ('companyprofile', models.TextField()),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='emppack_activation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('totaljobpost', models.IntegerField(default=0)),
                ('totalresume', models.IntegerField(default=0)),
                ('total_activated_job', models.IntegerField(default=0)),
                ('total_viewed_resume', models.IntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='emppacks',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pack_name', models.CharField(max_length=100)),
                ('pack_description', models.TextField()),
                ('pack_duration', models.IntegerField(default=0)),
                ('pack_cost', models.DecimalField(max_digits=5, decimal_places=2)),
                ('no_resume', models.IntegerField(default=0)),
                ('no_jobpost', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='EmpProfileView',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('viewdate', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='empsocialnetworks',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('facebook', models.CharField(max_length=250, null=True, blank=True)),
                ('linkedin', models.CharField(max_length=250, null=True, blank=True)),
                ('twitter', models.CharField(max_length=250, null=True, blank=True)),
                ('emp', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EmpSubscription',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pack_activate', models.DateTimeField(auto_now_add=True)),
                ('employer', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('pack', models.ForeignKey(to='registration.emppacks')),
            ],
        ),
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Denied', models.BooleanField(default=False)),
                ('interviewpassed', models.BooleanField(default=False)),
                ('interviewfailed', models.BooleanField(default=False)),
                ('rounds', models.CharField(max_length=10)),
                ('interviewLocation', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='InterviewRounds',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('roundno', models.IntegerField(default=0)),
                ('score', models.IntegerField(default=0)),
                ('interviewby', models.CharField(max_length=75)),
                ('interviewdate', models.CharField(max_length=50)),
                ('tips', models.CharField(max_length=1000)),
                ('nextrounddate', models.CharField(max_length=50)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='jobs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('referencecode', models.CharField(max_length=100)),
                ('jobsummary', models.TextField()),
                ('jobdetails', models.TextField()),
                ('industry', models.CharField(max_length=100)),
                ('functionalarea', models.CharField(max_length=100)),
                ('min_exp', models.IntegerField(default=0)),
                ('max_exp', models.IntegerField(default=0)),
                ('address1', models.CharField(max_length=100)),
                ('address2', models.CharField(max_length=100)),
                ('address3', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('zipcode', models.CharField(max_length=10)),
                ('lat', models.CharField(max_length=40, null=True, blank=True)),
                ('lng', models.CharField(max_length=40, null=True, blank=True)),
                ('typ', models.CharField(max_length=75, null=True, blank=True)),
                ('ownername', models.CharField(max_length=100)),
                ('workno', models.CharField(max_length=100)),
                ('handno', models.CharField(max_length=100)),
                ('fax', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('marklive', models.DateTimeField(null=True, blank=True)),
                ('todate', models.DateTimeField(null=True, blank=True)),
                ('jobtype', models.CharField(max_length=100)),
                ('salary_range', models.CharField(max_length=100)),
                ('qualification', models.CharField(max_length=500)),
                ('empsecretclear', models.CharField(max_length=100)),
                ('emptravel', models.CharField(max_length=20)),
                ('emptele', models.BooleanField(default=False)),
                ('workpermit', models.CharField(max_length=100, blank=True)),
                ('hitcount', models.IntegerField(default=0)),
                ('viewcount', models.IntegerField(default=0)),
                ('is_active', models.BooleanField(default=False)),
                ('is_delete', models.BooleanField(default=False)),
                ('emp', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='JSAppliedJobs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('applieddate', models.DateTimeField(auto_now=True)),
                ('jsappdel', models.BooleanField(default=True)),
                ('empappdel', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='JSCertificate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('certificate', models.CharField(max_length=200, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='JSDetailOther',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('emptype', models.CharField(max_length=100, null=True, blank=True)),
                ('workpermit', models.CharField(max_length=100, null=True, blank=True)),
                ('workother', models.CharField(max_length=100, null=True, blank=True)),
                ('relocate', models.CharField(default=b'No', max_length=200)),
                ('telecommunicate', models.CharField(default=b'No', max_length=200)),
                ('travel', models.CharField(max_length=200, null=True, blank=True)),
                ('relocatechoice', models.CharField(max_length=500, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='JSDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('visiblity', models.BooleanField(default=True)),
                ('visiblepassive', models.BooleanField(default=False)),
                ('viewcount', models.IntegerField(default=0)),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='JSEmployerDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('employer_name', models.CharField(max_length=100, null=True, blank=True)),
                ('empstatus', models.CharField(max_length=100, null=True, blank=True)),
                ('empstartdate', models.CharField(max_length=100, null=True, blank=True)),
                ('emptodate', models.CharField(max_length=100, null=True, blank=True)),
                ('designation', models.CharField(max_length=100, null=True, blank=True)),
                ('jobprofile', models.TextField(null=True, blank=True)),
                ('JS', models.ForeignKey(to='registration.JSDetails')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='JSLanguage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language', models.CharField(max_length=100, null=True, blank=True)),
                ('proficiency', models.CharField(max_length=100, null=True, blank=True)),
                ('read', models.CharField(default=b'No', max_length=100)),
                ('write', models.CharField(default=b'No', max_length=100)),
                ('speak', models.CharField(default=b'No', max_length=100)),
                ('JS', models.ForeignKey(to='registration.JSDetails')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='jspacks',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pack_name', models.CharField(max_length=100)),
                ('pack_description', models.TextField()),
                ('pack_duration', models.IntegerField()),
                ('nojob_applied', models.IntegerField()),
                ('pack_cost', models.DecimalField(max_digits=5, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='JSPersonal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dob', models.CharField(max_length=100, null=True, blank=True)),
                ('sec_email', models.EmailField(max_length=100, null=True, blank=True)),
                ('address1', models.CharField(max_length=100, null=True, blank=True)),
                ('address2', models.CharField(max_length=100, null=True, blank=True)),
                ('country', models.CharField(max_length=100, null=True, blank=True)),
                ('state', models.CharField(max_length=100, null=True, blank=True)),
                ('city', models.CharField(max_length=100, null=True, blank=True)),
                ('zipcode', models.CharField(max_length=100, null=True, blank=True)),
                ('lat', models.CharField(max_length=40, null=True, blank=True)),
                ('lng', models.CharField(max_length=40, null=True, blank=True)),
                ('typ', models.CharField(max_length=15, null=True, blank=True)),
                ('handno', models.CharField(max_length=100, null=True, blank=True)),
                ('workno', models.CharField(max_length=100, null=True, blank=True)),
                ('homeno', models.CharField(max_length=100, null=True, blank=True)),
                ('prefertime', models.CharField(max_length=10, null=True, blank=True)),
                ('gender', models.CharField(max_length=100, null=True, blank=True)),
                ('maritalstatus', models.CharField(max_length=100, null=True, blank=True)),
                ('work_expyears', models.CharField(max_length=100, null=True, blank=True)),
                ('work_expmonths', models.CharField(max_length=100, null=True, blank=True)),
                ('salaryrange', models.CharField(max_length=50, null=True, blank=True)),
                ('industry', models.CharField(max_length=100, null=True, blank=True)),
                ('functional_area', models.CharField(max_length=100, null=True, blank=True)),
                ('profileurl', models.URLField(max_length=250, null=True, blank=True)),
                ('JS', models.OneToOneField(to='registration.JSDetails')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='JSProfileSummary',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('profile_summary', models.TextField(null=True, blank=True)),
                ('profile_pic', models.ImageField(null=True, upload_to=b'image', blank=True)),
                ('JS', models.OneToOneField(to='registration.JSDetails')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='JSProjectDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('client', models.CharField(max_length=100, null=True, blank=True)),
                ('project_title', models.CharField(max_length=100, null=True, blank=True)),
                ('projstartdate', models.CharField(max_length=100, null=True, blank=True)),
                ('projtodate', models.CharField(max_length=100, null=True, blank=True)),
                ('project_loc', models.CharField(max_length=100, null=True, blank=True)),
                ('on_offsite', models.CharField(max_length=100, null=True, blank=True)),
                ('emp_type', models.CharField(max_length=100, null=True, blank=True)),
                ('project_details', models.TextField(null=True, blank=True)),
                ('role_desc', models.TextField(null=True, blank=True)),
                ('skill_used', models.TextField(null=True, blank=True)),
                ('role', models.CharField(max_length=100, null=True, blank=True)),
                ('teamsize', models.CharField(max_length=100, null=True, blank=True)),
                ('JS', models.ForeignKey(to='registration.JSDetails')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='JSQualification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('degree', models.CharField(max_length=100, null=True, blank=True)),
                ('special', models.CharField(max_length=100, null=True, blank=True)),
                ('institution', models.CharField(max_length=100, null=True, blank=True)),
                ('location', models.CharField(max_length=100, null=True, blank=True)),
                ('year', models.CharField(max_length=100, null=True, blank=True)),
                ('country', models.CharField(max_length=100, null=True, blank=True)),
                ('JS', models.ForeignKey(to='registration.JSDetails')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='JSResume',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('resumeTitle', models.CharField(max_length=275, null=True, blank=True)),
                ('resumeFile', models.FileField(null=True, upload_to=b'documents', blank=True)),
                ('resumeDate', models.DateTimeField(auto_now=True)),
                ('JS', models.ForeignKey(to='registration.JSDetails')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='JSResumeActive',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('JS', models.OneToOneField(null=True, blank=True, to='registration.JSDetails')),
                ('resumeActive', models.ForeignKey(blank=True, to='registration.JSResume', null=True)),
                ('user', models.OneToOneField(null=True, blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='JSsavesearch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('searchname', models.CharField(max_length=100)),
                ('searchlinks', models.CharField(max_length=500)),
                ('ip_address', models.CharField(max_length=500)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='JSsecurity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('jssecretclear', models.CharField(max_length=100, null=True, blank=True)),
                ('jsfromdate', models.DateTimeField(null=True, blank=True)),
                ('jstodate', models.DateTimeField(null=True, blank=True)),
                ('JS', models.OneToOneField(to='registration.JSDetails')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='JSSkills',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('skill', models.CharField(max_length=100, null=True, blank=True)),
                ('version', models.CharField(max_length=100, null=True, blank=True)),
                ('lastused', models.CharField(max_length=100, null=True, blank=True)),
                ('skillyear', models.CharField(max_length=100, null=True, blank=True)),
                ('skillmon', models.CharField(max_length=100, null=True, blank=True)),
                ('JS', models.ForeignKey(to='registration.JSDetails')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='jssubscribed_packs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pack_activate', models.DateTimeField()),
                ('pack_expire', models.DateTimeField()),
                ('jobseeker', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('pack', models.ForeignKey(to='registration.jspacks')),
            ],
        ),
        migrations.CreateModel(
            name='JSTextResume',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('resumeTitle', models.CharField(max_length=275, null=True, blank=True)),
                ('resumeFile', models.TextField(null=True, blank=True)),
                ('resumeDate', models.DateTimeField(auto_now=True)),
                ('activetext_resume', models.BooleanField(default=False)),
                ('JS', models.OneToOneField(to='registration.JSDetails')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='JSVideoResume',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('videoresume', models.ImageField(null=True, upload_to=b'image', blank=True)),
                ('resumeDate', models.DateTimeField(auto_now=True)),
                ('JS', models.OneToOneField(to='registration.JSDetails')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='newsletter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('usertype', models.CharField(max_length=50, choices=[(b'Employer', b'Employer'), (b'Jobseeker', b'Jobseeker')])),
                ('topics', models.CharField(max_length=100)),
                ('content', models.TextField(blank=True)),
                ('sentdate', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='profileviews',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('jobseeker', models.IntegerField(max_length=10)),
                ('viewDatetime', models.DateTimeField(auto_now=True)),
                ('employer', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RecordedVideos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('filepath', models.CharField(max_length=100)),
                ('filename', models.CharField(max_length=50)),
                ('uploadon', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RecruiterFolder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('foldername', models.CharField(max_length=100)),
                ('lastupdate', models.CharField(max_length=100)),
                ('employer', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RecSaveSearch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('searchname', models.CharField(max_length=100, blank=True)),
                ('savedsearch', models.CharField(max_length=400, blank=True)),
                ('employer', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RegistrationProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('activation_key', models.CharField(max_length=40)),
                ('key_generated', models.DateTimeField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reschedule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('jsschedule_date1', models.CharField(max_length=50, blank=True)),
                ('jsschedule_time1', models.CharField(max_length=50, blank=True)),
                ('jsupdate1', models.CharField(max_length=50)),
                ('jsschedule_date2', models.CharField(max_length=50, blank=True)),
                ('jsschedule_time2', models.CharField(max_length=50, blank=True)),
                ('jsupdate2', models.CharField(max_length=50)),
                ('jsschedule_date3', models.CharField(max_length=50, blank=True)),
                ('jsschedule_time3', models.CharField(max_length=50, blank=True)),
                ('jsupdate3', models.CharField(max_length=50)),
                ('empschedule_date1', models.CharField(max_length=50, blank=True)),
                ('empschedule_time1', models.CharField(max_length=50, blank=True)),
                ('empupdate1', models.CharField(max_length=50)),
                ('empschedule_date2', models.CharField(max_length=50, blank=True)),
                ('empschedule_time2', models.CharField(max_length=50, blank=True)),
                ('empupdate2', models.CharField(max_length=50)),
                ('empschedule_date3', models.CharField(max_length=50, blank=True)),
                ('empschedule_time3', models.CharField(max_length=50, blank=True)),
                ('empupdate3', models.CharField(max_length=50)),
                ('JSconfirmation', models.BooleanField(default=False)),
                ('Empconfirmation', models.BooleanField(default=False)),
                ('JSId', models.ForeignKey(to='registration.JSDetails')),
                ('Job', models.ForeignKey(to='registration.jobs')),
                ('emp', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('interview', models.OneToOneField(to='registration.Interview')),
            ],
        ),
        migrations.CreateModel(
            name='SaveCandidateFolder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dateupdate', models.DateTimeField(auto_now=True)),
                ('employer', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('folder', models.ForeignKey(to='registration.RecruiterFolder')),
                ('jobseeker', models.ForeignKey(to='registration.JSDetails')),
            ],
        ),
        migrations.CreateModel(
            name='securityquestions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.CharField(max_length=170)),
                ('answer', models.CharField(max_length=60)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='jsdetailother',
            name='JS',
            field=models.OneToOneField(to='registration.JSDetails'),
        ),
        migrations.AddField(
            model_name='jsdetailother',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='jscertificate',
            name='JS',
            field=models.ForeignKey(to='registration.JSDetails'),
        ),
        migrations.AddField(
            model_name='jscertificate',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='jsappliedjobs',
            name='JS',
            field=models.ForeignKey(to='registration.JSDetails'),
        ),
        migrations.AddField(
            model_name='jsappliedjobs',
            name='Job',
            field=models.ForeignKey(to='registration.jobs'),
        ),
        migrations.AddField(
            model_name='jsappliedjobs',
            name='emp',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='interviewrounds',
            name='JSId',
            field=models.ForeignKey(to='registration.JSDetails'),
        ),
        migrations.AddField(
            model_name='interviewrounds',
            name='Job',
            field=models.ForeignKey(to='registration.jobs'),
        ),
        migrations.AddField(
            model_name='interviewrounds',
            name='emp',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='interviewrounds',
            name='interview',
            field=models.ForeignKey(to='registration.Interview'),
        ),
        migrations.AddField(
            model_name='interview',
            name='JSId',
            field=models.ForeignKey(to='registration.JSDetails'),
        ),
        migrations.AddField(
            model_name='interview',
            name='Job',
            field=models.ForeignKey(to='registration.jobs'),
        ),
        migrations.AddField(
            model_name='interview',
            name='emp',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='empprofileview',
            name='JS',
            field=models.ForeignKey(to='registration.JSDetails'),
        ),
        migrations.AddField(
            model_name='empprofileview',
            name='emp',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='emppack_activation',
            name='pack',
            field=models.ForeignKey(to='registration.emppacks'),
        ),
        migrations.AddField(
            model_name='emppack_activation',
            name='subscribed_pack',
            field=models.ForeignKey(to='registration.emp_subscribed_packs'),
        ),
        migrations.AddField(
            model_name='employerkeyskills',
            name='job',
            field=models.ForeignKey(to='registration.jobs'),
        ),
        migrations.AddField(
            model_name='emp_subscribed_packs',
            name='pack',
            field=models.ForeignKey(to='registration.emppacks'),
        ),
        migrations.AddField(
            model_name='blog',
            name='btopic',
            field=models.ForeignKey(to='registration.BlogTopics'),
        ),
        migrations.AddField(
            model_name='blog',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bcomments',
            name='blog',
            field=models.ForeignKey(to='registration.Blog'),
        ),
        migrations.AddField(
            model_name='bcomments',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]