# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'RegistrationProfile'
        db.create_table('registration_registrationprofile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], unique=True)),
            ('activation_key', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('key_generated', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('registration', ['RegistrationProfile'])

        # Adding model 'securityquestions'
        db.create_table('registration_securityquestions', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('question', self.gf('django.db.models.fields.CharField')(max_length=170)),
            ('answer', self.gf('django.db.models.fields.CharField')(max_length=60)),
        ))
        db.send_create_signal('registration', ['securityquestions'])

        # Adding model 'activationcode'
        db.create_table('registration_activationcode', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('key', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('key_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('registration', ['activationcode'])

        # Adding model 'JSDetails'
        db.create_table('registration_jsdetails', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('visiblity', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('visiblepassive', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('viewcount', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('post_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('update_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('registration', ['JSDetails'])

        # Adding model 'JSPersonal'
        db.create_table('registration_jspersonal', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('JS', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['registration.JSDetails'], unique=True)),
            ('dob', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('sec_email', self.gf('django.db.models.fields.EmailField')(max_length=100, null=True, blank=True)),
            ('address1', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('address2', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('zipcode', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('lat', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('lng', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('typ', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
            ('handno', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('workno', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('homeno', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('prefertime', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('maritalstatus', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('work_expyears', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('work_expmonths', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('salaryrange', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('industry', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('functional_area', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('profileurl', self.gf('django.db.models.fields.URLField')(max_length=250, null=True, blank=True)),
        ))
        db.send_create_signal('registration', ['JSPersonal'])

        # Adding model 'JSQualification'
        db.create_table('registration_jsqualification', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('JS', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['registration.JSDetails'])),
            ('degree', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('special', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('institution', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('year', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('registration', ['JSQualification'])

        # Adding model 'JSCertificate'
        db.create_table('registration_jscertificate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('JS', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['registration.JSDetails'])),
            ('certificate', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal('registration', ['JSCertificate'])

        # Adding model 'JSProfileSummary'
        db.create_table('registration_jsprofilesummary', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('JS', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['registration.JSDetails'], unique=True)),
            ('profile_summary', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('profile_pic', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('registration', ['JSProfileSummary'])

        # Adding model 'JSSkills'
        db.create_table('registration_jsskills', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('JS', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['registration.JSDetails'])),
            ('skill', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('version', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('lastused', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('skillyear', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('skillmon', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('registration', ['JSSkills'])

        # Adding model 'JSEmployerDetails'
        db.create_table('registration_jsemployerdetails', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('JS', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['registration.JSDetails'])),
            ('employer_name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('empstatus', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('empstartdate', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('emptodate', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('designation', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('jobprofile', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('registration', ['JSEmployerDetails'])

        # Adding model 'JSProjectDetails'
        db.create_table('registration_jsprojectdetails', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('JS', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['registration.JSDetails'])),
            ('client', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('project_title', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('projstartdate', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('projtodate', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('project_loc', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('on_offsite', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('emp_type', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('project_details', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('role_desc', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('skill_used', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('role', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('teamsize', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('registration', ['JSProjectDetails'])

        # Adding model 'JSLanguage'
        db.create_table('registration_jslanguage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('JS', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['registration.JSDetails'])),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('proficiency', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('read', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('write', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('speak', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('registration', ['JSLanguage'])

        # Adding model 'JSsecurity'
        db.create_table('registration_jssecurity', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('JS', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['registration.JSDetails'], unique=True)),
            ('jssecretclear', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('jsfromdate', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('jstodate', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal('registration', ['JSsecurity'])

        # Adding model 'JSResume'
        db.create_table('registration_jsresume', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('JS', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['registration.JSDetails'])),
            ('resumeTitle', self.gf('django.db.models.fields.CharField')(max_length=275, null=True, blank=True)),
            ('resumeFile', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('resumeDate', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('registration', ['JSResume'])

        # Adding model 'JSTextResume'
        db.create_table('registration_jstextresume', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('JS', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['registration.JSDetails'], unique=True)),
            ('resumeTitle', self.gf('django.db.models.fields.CharField')(max_length=275, null=True, blank=True)),
            ('resumeFile', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('resumeDate', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('activetext_resume', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('registration', ['JSTextResume'])

        # Adding model 'JSVideoResume'
        db.create_table('registration_jsvideoresume', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('JS', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['registration.JSDetails'], unique=True)),
            ('videoresume', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('resumeDate', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('registration', ['JSVideoResume'])

        # Adding model 'JSResumeActive'
        db.create_table('registration_jsresumeactive', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('JS', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['registration.JSDetails'], unique=True)),
            ('resumeActive', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['registration.JSResume'], unique=True)),
        ))
        db.send_create_signal('registration', ['JSResumeActive'])

        # Adding model 'JSDetailOther'
        db.create_table('registration_jsdetailother', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('JS', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['registration.JSDetails'], unique=True)),
            ('emptype', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('workpermit', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('workother', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('relocate', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('telecommunicate', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('travel', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('relocatechoice', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
        ))
        db.send_create_signal('registration', ['JSDetailOther'])

        # Adding model 'EmpProfileView'
        db.create_table('registration_empprofileview', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('JS', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['registration.JSDetails'])),
            ('emp', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('viewdate', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('registration', ['EmpProfileView'])

        # Adding model 'EmployerReg_Form'
        db.create_table('registration_employerreg_form', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('companytype', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('contactno', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('contactperson', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('companyurl', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('companylogo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('companyprofile', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('registration', ['EmployerReg_Form'])

        # Adding model 'Emp_Gallery'
        db.create_table('registration_emp_gallery', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('emp', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('galpictitle', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('galpic', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('registration', ['Emp_Gallery'])

        # Adding model 'Emp_Gallery_video'
        db.create_table('registration_emp_gallery_video', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('emp', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('galvideotitle', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('galvideo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('registration', ['Emp_Gallery_video'])

        # Adding model 'jobs'
        db.create_table('registration_jobs', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('emp', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('referencecode', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('jobsummary', self.gf('django.db.models.fields.TextField')()),
            ('jobdetails', self.gf('django.db.models.fields.TextField')()),
            ('industry', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('functionalarea', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('min_exp', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('max_exp', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('address1', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('address2', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('address3', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('zipcode', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('lat', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('lng', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('typ', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
            ('ownername', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('workno', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('handno', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('fax', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('marklive', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('todate', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('jobtype', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('salary_range', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('qualification', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('empsecretclear', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('emptravel', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('emptele', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('workpermit', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('hitcount', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('viewcount', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('registration', ['jobs'])

        # Adding model 'employerkeyskills'
        db.create_table('registration_employerkeyskills', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('emp', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('job', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['registration.jobs'])),
            ('keyskills', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('registration', ['employerkeyskills'])

        # Adding model 'RecruiterFolder'
        db.create_table('registration_recruiterfolder', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('foldername', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('employer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('lastupdate', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('registration', ['RecruiterFolder'])

        # Adding model 'SaveCandidateFolder'
        db.create_table('registration_savecandidatefolder', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('folder', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['registration.RecruiterFolder'])),
            ('employer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('jobseeker', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['registration.JSDetails'])),
            ('dateupdate', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('registration', ['SaveCandidateFolder'])

        # Adding model 'RecSaveSearch'
        db.create_table('registration_recsavesearch', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('employer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('searchname', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('savedsearch', self.gf('django.db.models.fields.CharField')(max_length=400, blank=True)),
        ))
        db.send_create_signal('registration', ['RecSaveSearch'])

        # Adding model 'BlogTopics'
        db.create_table('registration_blogtopics', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('blogtopic', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('blogImgurl', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
        ))
        db.send_create_signal('registration', ['BlogTopics'])

        # Adding model 'Blog'
        db.create_table('registration_blog', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('btopic', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['registration.BlogTopics'])),
            ('btitle', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('bimage', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('bcontent', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('bposted', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('registration', ['Blog'])

        # Adding model 'BComments'
        db.create_table('registration_bcomments', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('blog', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['registration.Blog'])),
            ('comments', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('commentpost', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('registration', ['BComments'])

        # Adding model 'Interview'
        db.create_table('registration_interview', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('emp', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('JSId', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['registration.JSDetails'])),
            ('Job', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['registration.jobs'])),
            ('Denied', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('interviewpassed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('interviewfailed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('rounds', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('interviewLocation', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal('registration', ['Interview'])

        # Adding model 'Reschedule'
        db.create_table('registration_reschedule', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('interview', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['registration.Interview'], unique=True)),
            ('emp', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('JSId', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['registration.JSDetails'])),
            ('Job', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['registration.jobs'])),
            ('jsschedule_date1', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('jsschedule_time1', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('jsupdate1', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('jsschedule_date2', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('jsschedule_time2', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('jsupdate2', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('jsschedule_date3', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('jsschedule_time3', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('jsupdate3', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('jsschedule_date4', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('jsschedule_time4', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('jsupdate4', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('jsschedule_date5', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('jsschedule_time5', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('jsupdate5', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('empschedule_date1', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('empschedule_time1', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('empupdate1', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('empschedule_date2', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('empschedule_time2', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('empupdate2', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('empschedule_date3', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('empschedule_time3', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('empupdate3', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('empschedule_date4', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('empschedule_time4', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('empupdate4', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('empschedule_date5', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('empschedule_time5', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('empupdate5', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('JSconfirmation', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('Empconfirmation', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('registration', ['Reschedule'])

        # Adding model 'InterviewRounds'
        db.create_table('registration_interviewrounds', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('interview', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['registration.Interview'])),
            ('emp', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('JSId', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['registration.JSDetails'])),
            ('Job', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['registration.jobs'])),
            ('roundno', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('score', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('interviewby', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('interviewdate', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('tips', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('nextrounddate', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('status', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('registration', ['InterviewRounds'])

        # Adding model 'emp_avail_packs'
        db.create_table('registration_emp_avail_packs', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pack_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('pack_description', self.gf('django.db.models.fields.TextField')()),
            ('pack_duration', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('pack_cost', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('no_resume', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('no_jobpost', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('registration', ['emp_avail_packs'])

        # Adding model 'emp_selected_packs'
        db.create_table('registration_emp_selected_packs', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('employer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('pack', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['registration.emp_avail_packs'])),
            ('pack_activate', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('pack_expire', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('quantity', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('spack_jobpost', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('spack_resume', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('spack_cost', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('registration', ['emp_selected_packs'])

        # Adding model 'emp_selected_packs_add'
        db.create_table('registration_emp_selected_packs_add', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('employer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('pack', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['registration.emp_avail_packs'], unique=True)),
            ('pack_activate', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('pack_expire', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('spack_jobpost', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('spack_resume', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('registration', ['emp_selected_packs_add'])

        # Adding model 'js_avail_packs'
        db.create_table('registration_js_avail_packs', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pack_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('pack_description', self.gf('django.db.models.fields.TextField')()),
            ('pack_duration', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('pack_cost', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('registration', ['js_avail_packs'])

        # Adding model 'js_selected_packs'
        db.create_table('registration_js_selected_packs', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('jobseeker', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('pack', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['registration.js_avail_packs'])),
            ('pack_activate', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('pack_expire', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('quantity', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('spack_cost', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('registration', ['js_selected_packs'])

        # Adding model 'JSAppliedJobs'
        db.create_table('registration_jsappliedjobs', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('JS', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['registration.JSDetails'])),
            ('emp', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('Job', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['registration.jobs'])),
            ('applieddate', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('jsappdel', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('empappdel', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('registration', ['JSAppliedJobs'])

        # Adding model 'JSsavesearch'
        db.create_table('registration_jssavesearch', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('searchname', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('searchlink', self.gf('django.db.models.fields.CharField')(max_length=500)),
        ))
        db.send_create_signal('registration', ['JSsavesearch'])

        # Adding model 'newsletter'
        db.create_table('registration_newsletter', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('usertype', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('topics', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('content', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('sentdate', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('registration', ['newsletter'])


    def backwards(self, orm):
        # Deleting model 'RegistrationProfile'
        db.delete_table('registration_registrationprofile')

        # Deleting model 'securityquestions'
        db.delete_table('registration_securityquestions')

        # Deleting model 'activationcode'
        db.delete_table('registration_activationcode')

        # Deleting model 'JSDetails'
        db.delete_table('registration_jsdetails')

        # Deleting model 'JSPersonal'
        db.delete_table('registration_jspersonal')

        # Deleting model 'JSQualification'
        db.delete_table('registration_jsqualification')

        # Deleting model 'JSCertificate'
        db.delete_table('registration_jscertificate')

        # Deleting model 'JSProfileSummary'
        db.delete_table('registration_jsprofilesummary')

        # Deleting model 'JSSkills'
        db.delete_table('registration_jsskills')

        # Deleting model 'JSEmployerDetails'
        db.delete_table('registration_jsemployerdetails')

        # Deleting model 'JSProjectDetails'
        db.delete_table('registration_jsprojectdetails')

        # Deleting model 'JSLanguage'
        db.delete_table('registration_jslanguage')

        # Deleting model 'JSsecurity'
        db.delete_table('registration_jssecurity')

        # Deleting model 'JSResume'
        db.delete_table('registration_jsresume')

        # Deleting model 'JSTextResume'
        db.delete_table('registration_jstextresume')

        # Deleting model 'JSVideoResume'
        db.delete_table('registration_jsvideoresume')

        # Deleting model 'JSResumeActive'
        db.delete_table('registration_jsresumeactive')

        # Deleting model 'JSDetailOther'
        db.delete_table('registration_jsdetailother')

        # Deleting model 'EmpProfileView'
        db.delete_table('registration_empprofileview')

        # Deleting model 'EmployerReg_Form'
        db.delete_table('registration_employerreg_form')

        # Deleting model 'Emp_Gallery'
        db.delete_table('registration_emp_gallery')

        # Deleting model 'Emp_Gallery_video'
        db.delete_table('registration_emp_gallery_video')

        # Deleting model 'jobs'
        db.delete_table('registration_jobs')

        # Deleting model 'employerkeyskills'
        db.delete_table('registration_employerkeyskills')

        # Deleting model 'RecruiterFolder'
        db.delete_table('registration_recruiterfolder')

        # Deleting model 'SaveCandidateFolder'
        db.delete_table('registration_savecandidatefolder')

        # Deleting model 'RecSaveSearch'
        db.delete_table('registration_recsavesearch')

        # Deleting model 'BlogTopics'
        db.delete_table('registration_blogtopics')

        # Deleting model 'Blog'
        db.delete_table('registration_blog')

        # Deleting model 'BComments'
        db.delete_table('registration_bcomments')

        # Deleting model 'Interview'
        db.delete_table('registration_interview')

        # Deleting model 'Reschedule'
        db.delete_table('registration_reschedule')

        # Deleting model 'InterviewRounds'
        db.delete_table('registration_interviewrounds')

        # Deleting model 'emp_avail_packs'
        db.delete_table('registration_emp_avail_packs')

        # Deleting model 'emp_selected_packs'
        db.delete_table('registration_emp_selected_packs')

        # Deleting model 'emp_selected_packs_add'
        db.delete_table('registration_emp_selected_packs_add')

        # Deleting model 'js_avail_packs'
        db.delete_table('registration_js_avail_packs')

        # Deleting model 'js_selected_packs'
        db.delete_table('registration_js_selected_packs')

        # Deleting model 'JSAppliedJobs'
        db.delete_table('registration_jsappliedjobs')

        # Deleting model 'JSsavesearch'
        db.delete_table('registration_jssavesearch')

        # Deleting model 'newsletter'
        db.delete_table('registration_newsletter')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'companyname': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'usertype': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'registration.activationcode': {
            'Meta': {'object_name': 'activationcode'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'key_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'registration.bcomments': {
            'Meta': {'object_name': 'BComments'},
            'blog': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['registration.Blog']"}),
            'commentpost': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'comments': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'registration.blog': {
            'Meta': {'object_name': 'Blog'},
            'bcontent': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'bimage': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'bposted': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'btitle': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'btopic': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['registration.BlogTopics']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'registration.blogtopics': {
            'Meta': {'object_name': 'BlogTopics'},
            'blogImgurl': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'blogtopic': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'registration.emp_avail_packs': {
            'Meta': {'object_name': 'emp_avail_packs'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'no_jobpost': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'no_resume': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'pack_cost': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'pack_description': ('django.db.models.fields.TextField', [], {}),
            'pack_duration': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'pack_name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'registration.emp_gallery': {
            'Meta': {'object_name': 'Emp_Gallery'},
            'emp': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'galpic': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'galpictitle': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'registration.emp_gallery_video': {
            'Meta': {'object_name': 'Emp_Gallery_video'},
            'emp': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'galvideo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'galvideotitle': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'registration.emp_selected_packs': {
            'Meta': {'object_name': 'emp_selected_packs'},
            'employer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pack': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['registration.emp_avail_packs']"}),
            'pack_activate': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'pack_expire': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'spack_cost': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'spack_jobpost': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'spack_resume': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'registration.emp_selected_packs_add': {
            'Meta': {'object_name': 'emp_selected_packs_add'},
            'employer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pack': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['registration.emp_avail_packs']", 'unique': 'True'}),
            'pack_activate': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'pack_expire': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'spack_jobpost': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'spack_resume': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'registration.employerkeyskills': {
            'Meta': {'object_name': 'employerkeyskills'},
            'emp': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['registration.jobs']"}),
            'keyskills': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'registration.employerreg_form': {
            'Meta': {'object_name': 'EmployerReg_Form'},
            'companylogo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'companyprofile': ('django.db.models.fields.TextField', [], {}),
            'companytype': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'companyurl': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'contactno': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'contactperson': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'registration.empprofileview': {
            'JS': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['registration.JSDetails']"}),
            'Meta': {'object_name': 'EmpProfileView'},
            'emp': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'viewdate': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'registration.interview': {
            'Denied': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'JSId': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['registration.JSDetails']"}),
            'Job': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['registration.jobs']"}),
            'Meta': {'object_name': 'Interview'},
            'emp': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interviewLocation': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'interviewfailed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'interviewpassed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'rounds': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'registration.interviewrounds': {
            'JSId': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['registration.JSDetails']"}),
            'Job': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['registration.jobs']"}),
            'Meta': {'object_name': 'InterviewRounds'},
            'emp': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interview': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['registration.Interview']"}),
            'interviewby': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'interviewdate': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'nextrounddate': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'roundno': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tips': ('django.db.models.fields.CharField', [], {'max_length': '1000'})
        },
        'registration.jobs': {
            'Meta': {'object_name': 'jobs'},
            'address1': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'address2': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'address3': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'emp': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'empsecretclear': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'emptele': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'emptravel': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'functionalarea': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'handno': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'hitcount': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'industry': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'jobdetails': ('django.db.models.fields.TextField', [], {}),
            'jobsummary': ('django.db.models.fields.TextField', [], {}),
            'jobtype': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'lat': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'lng': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'marklive': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'max_exp': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'min_exp': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'ownername': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'qualification': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'referencecode': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'salary_range': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'todate': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'typ': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'viewcount': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'workno': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'workpermit': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'registration.js_avail_packs': {
            'Meta': {'object_name': 'js_avail_packs'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pack_cost': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'pack_description': ('django.db.models.fields.TextField', [], {}),
            'pack_duration': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'pack_name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'registration.js_selected_packs': {
            'Meta': {'object_name': 'js_selected_packs'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jobseeker': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'pack': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['registration.js_avail_packs']"}),
            'pack_activate': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'pack_expire': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'spack_cost': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'registration.jsappliedjobs': {
            'JS': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['registration.JSDetails']"}),
            'Job': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['registration.jobs']"}),
            'Meta': {'object_name': 'JSAppliedJobs'},
            'applieddate': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'emp': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'empappdel': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jsappdel': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'registration.jscertificate': {
            'JS': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['registration.JSDetails']"}),
            'Meta': {'object_name': 'JSCertificate'},
            'certificate': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'registration.jsdetailother': {
            'JS': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['registration.JSDetails']", 'unique': 'True'}),
            'Meta': {'object_name': 'JSDetailOther'},
            'emptype': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'relocate': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'relocatechoice': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'telecommunicate': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'travel': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'}),
            'workother': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'workpermit': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'registration.jsdetails': {
            'Meta': {'object_name': 'JSDetails'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post_date': ('django.db.models.fields.DateTimeField', [], {}),
            'update_date': ('django.db.models.fields.DateTimeField', [], {}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'}),
            'viewcount': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'visiblepassive': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'visiblity': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'registration.jsemployerdetails': {
            'JS': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['registration.JSDetails']"}),
            'Meta': {'object_name': 'JSEmployerDetails'},
            'designation': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'employer_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'empstartdate': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'empstatus': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'emptodate': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jobprofile': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'registration.jslanguage': {
            'JS': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['registration.JSDetails']"}),
            'Meta': {'object_name': 'JSLanguage'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'proficiency': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'read': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'speak': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'write': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'registration.jspersonal': {
            'JS': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['registration.JSDetails']", 'unique': 'True'}),
            'Meta': {'object_name': 'JSPersonal'},
            'address1': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'address2': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'dob': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'functional_area': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'handno': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'homeno': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'industry': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'lat': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'lng': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'maritalstatus': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'prefertime': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'profileurl': ('django.db.models.fields.URLField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'salaryrange': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'sec_email': ('django.db.models.fields.EmailField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'typ': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'}),
            'work_expmonths': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'work_expyears': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'workno': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'registration.jsprofilesummary': {
            'JS': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['registration.JSDetails']", 'unique': 'True'}),
            'Meta': {'object_name': 'JSProfileSummary'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'profile_pic': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'profile_summary': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'registration.jsprojectdetails': {
            'JS': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['registration.JSDetails']"}),
            'Meta': {'object_name': 'JSProjectDetails'},
            'client': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'emp_type': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'on_offsite': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'project_details': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'project_loc': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'project_title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'projstartdate': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'projtodate': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'role': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'role_desc': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'skill_used': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'teamsize': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'registration.jsqualification': {
            'JS': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['registration.JSDetails']"}),
            'Meta': {'object_name': 'JSQualification'},
            'country': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'degree': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institution': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'special': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'year': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'registration.jsresume': {
            'JS': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['registration.JSDetails']"}),
            'Meta': {'object_name': 'JSResume'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'resumeDate': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'resumeFile': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'resumeTitle': ('django.db.models.fields.CharField', [], {'max_length': '275', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'registration.jsresumeactive': {
            'JS': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['registration.JSDetails']", 'unique': 'True'}),
            'Meta': {'object_name': 'JSResumeActive'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'resumeActive': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['registration.JSResume']", 'unique': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'registration.jssavesearch': {
            'Meta': {'object_name': 'JSsavesearch'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'searchlink': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'searchname': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'registration.jssecurity': {
            'JS': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['registration.JSDetails']", 'unique': 'True'}),
            'Meta': {'object_name': 'JSsecurity'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jsfromdate': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'jssecretclear': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'jstodate': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'registration.jsskills': {
            'JS': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['registration.JSDetails']"}),
            'Meta': {'object_name': 'JSSkills'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastused': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'skill': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'skillmon': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'skillyear': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'registration.jstextresume': {
            'JS': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['registration.JSDetails']", 'unique': 'True'}),
            'Meta': {'object_name': 'JSTextResume'},
            'activetext_resume': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'resumeDate': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'resumeFile': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'resumeTitle': ('django.db.models.fields.CharField', [], {'max_length': '275', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'registration.jsvideoresume': {
            'JS': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['registration.JSDetails']", 'unique': 'True'}),
            'Meta': {'object_name': 'JSVideoResume'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'resumeDate': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'}),
            'videoresume': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'registration.newsletter': {
            'Meta': {'object_name': 'newsletter'},
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sentdate': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'topics': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'usertype': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'registration.recruiterfolder': {
            'Meta': {'object_name': 'RecruiterFolder'},
            'employer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'foldername': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastupdate': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'registration.recsavesearch': {
            'Meta': {'object_name': 'RecSaveSearch'},
            'employer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'savedsearch': ('django.db.models.fields.CharField', [], {'max_length': '400', 'blank': 'True'}),
            'searchname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        'registration.registrationprofile': {
            'Meta': {'object_name': 'RegistrationProfile'},
            'activation_key': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key_generated': ('django.db.models.fields.DateTimeField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'registration.reschedule': {
            'Empconfirmation': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'JSId': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['registration.JSDetails']"}),
            'JSconfirmation': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'Job': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['registration.jobs']"}),
            'Meta': {'object_name': 'Reschedule'},
            'emp': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'empschedule_date1': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'empschedule_date2': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'empschedule_date3': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'empschedule_date4': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'empschedule_date5': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'empschedule_time1': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'empschedule_time2': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'empschedule_time3': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'empschedule_time4': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'empschedule_time5': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'empupdate1': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'empupdate2': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'empupdate3': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'empupdate4': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'empupdate5': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interview': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['registration.Interview']", 'unique': 'True'}),
            'jsschedule_date1': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'jsschedule_date2': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'jsschedule_date3': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'jsschedule_date4': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'jsschedule_date5': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'jsschedule_time1': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'jsschedule_time2': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'jsschedule_time3': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'jsschedule_time4': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'jsschedule_time5': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'jsupdate1': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'jsupdate2': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'jsupdate3': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'jsupdate4': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'jsupdate5': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'registration.savecandidatefolder': {
            'Meta': {'object_name': 'SaveCandidateFolder'},
            'dateupdate': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'employer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'folder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['registration.RecruiterFolder']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jobseeker': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['registration.JSDetails']"})
        },
        'registration.securityquestions': {
            'Meta': {'object_name': 'securityquestions'},
            'answer': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '170'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['registration']