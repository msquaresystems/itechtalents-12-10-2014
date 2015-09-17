"""
A registration profile model and associated manager.

The RegistrationProfile model and especially its custom manager
implement nearly all the logic needed to handle user registration and
account activation, so before implementing something in a view or
form, check here to see if they can take care of it for you.

Also, be sure to see the note on RegistrationProfile about use of the
``AUTH_PROFILE_MODULE`` setting.

"""

import random
import re
import sha
from datetime import datetime, timedelta
from django.db import models
from django.template import Context, loader
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.conf import settings
from django.contrib import admin
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail, EmailMultiAlternatives
from django.db.models import Q
from django.core.validators import URLValidator
from email.mime.image import MIMEImage
from django.http import HttpResponse
# from registration.models import EmployerReg_Form


class RegistrationManager(models.Manager):
    """
    Custom manager for the RegistrationProfile model.

    The methods defined here provide shortcuts for account creation
    and activation (including generation and emailing of activation
    keys), and for cleaning out expired inactive accounts.

    """
    def activate_user(self, activation_key):
        """
        Given the activation key, makes a User's account active if the
        activation key is valid and has not expired.

        Returns the User if successful, or False if the account was
        not found or the key had expired.

        """
        # Make sure the key we're trying conforms to the pattern of a
        # SHA1 hash; if it doesn't, no point even trying to look it up
        # in the DB.
        if re.match('[a-f0-9]{40}', activation_key):
            try:
                user_profile = self.get(activation_key=activation_key)
            except self.model.DoesNotExist:
                return False
            if not user_profile.activation_key_expired():
                # Account exists and has a non-expired key. Activate it.
                user = user_profile.user
                # if user.usertype=='employer':
                #     if not emp_subscribed_packs.objects.filter(employer_id=user.id):
                #         pack_activate=datetime.now()
                #         pack_expired=pack_activate + timedelta(days=30)
                #         subscribed=emp_subscribed_packs(employer_id=user.id,pack_id=1,pack_activate=pack_activate,pack_expire=pack_expired)
                #         subscribed.save()
                #         packs=emppacks.objects.get(id=1)
                #         emppack_activation(subscribed_pack_id=subscribed.id,pack_id=1,totaljobpost=packs.no_jobpost,totalresume=packs.no_resume).save()

                user.is_active = True
                user.save()
                return user
        return False


    def create_inactive_user(self, username, password, email, send_email=True):
        """
        Creates a new User and a new RegistrationProfile for that
        User, generates an activation key, and mails it.

        Pass ``send_email=False`` to disable sending the email.

        """
        # Create the user.
        new_user = User.objects.create_user(username, email, password)

        new_user.is_active = False
        new_user.save()

        # Generate a salted SHA1 hash to use as a key.
        salt = sha.new(str(random.random())).hexdigest()[:5]
        activation_key = sha.new(salt+new_user.email).hexdigest()

        # And finally create the profile.
        new_profile = self.create(user=new_user, activation_key=activation_key)

        if send_email:
            current_domain = Site.objects.get_current().domain
            ct = Context({'site_url': 'http://%s/' % current_domain,
                          'activation_key': activation_key,
                          'expiration_days': settings.ACCOUNT_ACTIVATION_DAYS})
            msg_tpl = loader.get_template('registration/activation_email.html')
            message = msg_tpl.render(ct)
            m = EmailMultiAlternatives('Activate your account at Itechtalents',
                                       message,
                                       settings.DEFAULT_FROM_EMAIL,
                                       [new_user.email])
            m.attach_alternative(message, "text/html")
            m.send()
        return new_user

    def delete_expired_users(self):
        """
        Removes unused profiles and their associated accounts.

        This is provided largely as a convenience for maintenance
        purposes; if a RegistrationProfile's key expires without the
        account being activated, then both the RegistrationProfile and
        the associated User become clutter in the database, and (more
        importantly) it won't be possible for anyone to ever come back
        and claim the username. For best results, set this up to run
        regularly as a cron job.

        If you have a User whose account you want to keep in the
        database even though it's inactive (say, to prevent a
        troublemaker from accessing or re-creating his account), just
        delete that User's RegistrationProfile and this method will
        leave it alone.

        """
        for profile in self.all():
            if profile.activation_key_expired():
                user = profile.user
                if not user.is_active:
                    user.delete() # Removing the User will remove the RegistrationProfile, too.


class RegistrationProfile(models.Model):
    """
    Simple profile model for a User, storing a registration date and
    an activation key for the account.

    While it is possible to use this model as the value of the
    ``AUTH_PROFILE_MODULE`` setting, it's not recommended that you do
    so. This model is intended solely to store some data needed for
    user registration, and can do that regardless of what you set in
    ``AUTH_PROFILE_MODULE``, so if you want to use user profiles in a
    project, it's far better to develop a customized model for that
    purpose and just let this one handle registration.

    """
    user = models.ForeignKey(User, unique=True)
    activation_key = models.CharField(max_length=40)
    key_generated = models.DateTimeField()

    objects = RegistrationManager()

    class Admin:
        pass

    def save(self, *args, **kwargs):
        if not self.id:
            self.key_generated = datetime.now()
        super(RegistrationProfile, self).save(*args, **kwargs)

    def __str__(self):
        return "User profile for %s" % self.user.username

    def activation_key_expired(self):
        """
        Determines whether this Profile's activation key has expired,
        based on the value of the setting ``ACCOUNT_ACTIVATION_DAYS``.

        """
        expiration_date = timedelta(days=settings.ACCOUNT_ACTIVATION_DAYS)
        return self.key_generated + expiration_date <= datetime.now()

class securityquestions(models.Model):
    user = models.OneToOneField(User)
    question=models.CharField(max_length=170)
    answer=models.CharField(max_length=60)

class activationcode(models.Model):
    user=models.OneToOneField(User)
    key=models.CharField(max_length=50)
    key_date = models.DateTimeField(auto_now_add=True)
class checksocial_login(models.Model):
    user=models.OneToOneField(User)
    loginflag=models.BooleanField(default=False)
class JSDetails(models.Model):
    user = models.OneToOneField(User)
    visiblity = models.BooleanField(default=True)
    visiblepassive = models.BooleanField(default=False)
    viewcount=models.IntegerField(default=0)
    post_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

# in model
# field = models.TextField(validators=[URLValidator()])

class JSPersonal(models.Model):
    user = models.OneToOneField(User)
    JS = models.OneToOneField(JSDetails)
    dob = models.CharField(max_length=100, blank=True, null=True)
    sec_email = models.EmailField(max_length=100, blank=True, null=True)
    address1 = models.CharField(max_length=100, blank=True, null=True)
    address2 = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    zipcode = models.CharField(max_length=100, blank=True, null=True)
    lat=models.CharField(max_length=40,blank=True,null=True)
    lng=models.CharField(max_length=40,blank=True,null=True)
    typ=models.CharField(max_length=15,blank=True,null=True)
    handno = models.CharField(max_length=100, blank=True, null=True)
    workno = models.CharField(max_length=100, blank=True, null=True)
    homeno = models.CharField(max_length=100, blank=True, null=True)
    prefertime=models.CharField(max_length=10, blank=True, null=True)
    gender = models.CharField(max_length=100, blank=True, null=True)
    maritalstatus = models.CharField(max_length=100, blank=True, null=True)
    work_expyears = models.CharField(max_length=100, blank=True, null=True)
    work_expmonths = models.CharField(max_length=100, blank=True, null=True)
    salaryrange = models.CharField(max_length=50, blank=True, null=True)
    industry = models.CharField(max_length=100, blank=True, null=True)
    functional_area = models.CharField(max_length=100, blank=True, null=True)
    profileurl=models.URLField(max_length=250,blank=True,null=True)


class JSQualification(models.Model):
    user = models.ForeignKey(User)
    JS = models.ForeignKey(JSDetails)
    degree = models.CharField(max_length=100, blank=True, null=True)
    special = models.CharField(max_length=100, blank=True, null=True)
    institution = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    year = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)

class JSCertificate(models.Model):
    user = models.ForeignKey(User)
    JS = models.ForeignKey(JSDetails)
    certificate = models.CharField(max_length=200, blank=True, null=True)

class JSProfileSummary(models.Model):
    user = models.OneToOneField(User)
    JS = models.OneToOneField(JSDetails)
    profile_summary = models.TextField(blank=True, null=True)
    profile_pic = models.ImageField(upload_to='image', blank=True, null=True)

class JSSkills(models.Model):
    user = models.ForeignKey(User)
    JS = models.ForeignKey(JSDetails)
    skill = models.CharField(max_length=100, blank=True, null=True)
    version = models.CharField(max_length=100, blank=True, null=True)
    lastused = models.CharField(max_length=100, blank=True, null=True)
    skillyear = models.CharField(max_length=100, blank=True, null=True)
    skillmon = models.CharField(max_length=100, blank=True, null=True)

class JSEmployerDetails(models.Model):

    user = models.ForeignKey(User)
    JS = models.ForeignKey(JSDetails)
    employer_name = models.CharField(max_length=100, blank=True, null=True)
    empstatus = models.CharField(max_length=100, blank=True, null=True)
    empstartdate = models.CharField(max_length=100, blank=True, null=True)
    emptodate = models.CharField(max_length=100, blank=True, null=True)
    designation = models.CharField(max_length=100, blank=True, null=True)
    jobprofile = models.TextField(blank=True, null=True)

class JSProjectDetails(models.Model):
    user = models.ForeignKey(User)
    JS = models.ForeignKey(JSDetails)
    client = models.CharField(max_length=100, blank=True, null=True)
    project_title = models.CharField(max_length=100, blank=True, null=True)
    projstartdate = models.CharField(max_length=100, blank=True, null=True)
    projtodate = models.CharField(max_length=100, blank=True, null=True)
    project_loc = models.CharField(max_length=100, blank=True, null=True)
    on_offsite = models.CharField(max_length=100, blank=True, null=True)
    emp_type = models.CharField(max_length=100, blank=True, null=True)
    project_details = models.TextField(blank=True, null=True)
    role_desc = models.TextField(blank=True, null=True)
    skill_used = models.TextField(blank=True, null=True)
    role = models.CharField(max_length=100, blank=True, null=True)
    teamsize = models.CharField(max_length=100, blank=True, null=True)

class JSLanguage(models.Model):
    user = models.ForeignKey(User)
    JS = models.ForeignKey(JSDetails)
    language = models.CharField(max_length=100, blank=True, null=True)
    proficiency = models.CharField(max_length=100, blank=True, null=True)
    read = models.CharField(max_length=100,default="No")
    write = models.CharField(max_length=100,default="No")
    speak = models.CharField(max_length=100,default="No")

class empsocialnetworks(models.Model):
    emp=models.OneToOneField(User)
    facebook=models.CharField(max_length=250,blank=True, null=True)
    linkedin=models.CharField(max_length=250,blank=True, null=True)
    twitter=models.CharField(max_length=250,blank=True, null=True)

class JSsecurity(models.Model):
    user = models.OneToOneField(User, unique=False)
    JS = models.OneToOneField(JSDetails, unique=False)
    jssecretclear = models.CharField(max_length=100, blank=True, null=True)
    jsfromdate = models.DateTimeField(blank=True, null=True)
    jstodate=models.DateTimeField(blank=True, null=True)

#jsfromdate = models.CharField(blank=True, null=True)
#jstodate=models.CharField(blank=True, null=True)

class JSResume(models.Model):
    user = models.ForeignKey(User, unique=False)
    JS = models.ForeignKey(JSDetails, unique=False)
    resumeTitle = models.CharField(max_length=275, blank=True, null=True)
    resumeFile = models.FileField(upload_to='documents', blank=True, null=True)
    resumeDate=models.DateTimeField(auto_now = True)

    def delete(self, *args, **kwargs):
        self.resumeFile.delete(False)
        super(JSResume, self).delete(*args, **kwargs)

class JSTextResume(models.Model):
    user = models.OneToOneField(User)
    JS = models.OneToOneField(JSDetails)
    resumeTitle = models.CharField(max_length=275, blank=True, null=True)
    resumeFile = models.TextField(blank=True, null=True)
    resumeDate = models.DateTimeField(auto_now = True)
    activetext_resume = models.BooleanField(default=False)

class JSVideoResume(models.Model):
    user = models.OneToOneField(User)
    JS = models.OneToOneField(JSDetails)
    videoresume = models.ImageField(upload_to='image', blank=True, null=True)
    resumeDate=models.DateTimeField(auto_now = True)

class RecordedVideos(models.Model):
    user=models.ForeignKey(User)
    filepath=models.CharField(max_length=100)
    filename=models.CharField(max_length=50)
    uploadon=models.DateTimeField(auto_now=True)


class JSResumeActive(models.Model):
    user = models.OneToOneField(User, blank=True, null=True)
    JS = models.OneToOneField(JSDetails, blank=True, null=True)
    resumeActive = models.ForeignKey(JSResume,blank=True, null=True)

class JSDetailOther(models.Model):
    user = models.OneToOneField(User)
    JS = models.OneToOneField(JSDetails)
    emptype = models.CharField(max_length=100, blank=True, null=True)
    workpermit = models.CharField(max_length=100, blank=True, null=True)
    workother = models.CharField(max_length=100, blank=True, null=True)
    relocate=models.CharField(max_length=200, default='No')
    telecommunicate=models.CharField(max_length=200, default='No')
    travel=models.CharField(max_length=200, blank=True, null=True)
    relocatechoice=models.CharField(max_length=500, blank=True, null=True)

class EmpProfileView(models.Model):
    JS=models.ForeignKey(JSDetails, unique=False)
    emp=models.ForeignKey(User, unique=False)
    viewdate=models.DateTimeField(auto_now = True)

class EmployerReg_Form(models.Model):
    user = models.OneToOneField(User)
    companytype = models.CharField(max_length=100)
    contactno = models.CharField(max_length=100)
    contactperson = models.CharField(max_length=100)
    companyurl=models.URLField()
    companyname = models.CharField(max_length=100)
    companylogo=models.ImageField(upload_to='companylogo', blank=True, null=True)
    companyprofile=models.TextField()
PREFERRED_COMPANYTYPE = (
    ('Company', 'Corporate'),
    ('Consultancy', 'Staffing'),
)

class Emp_Gallery(models.Model):
    emp = models.ForeignKey(User, unique=False)
    galpictitle = models.CharField(max_length=100)
    galpic = models.ImageField(upload_to='gallerypicture', blank=True, null=True)

class Emp_Gallery_video(models.Model):
    emp = models.ForeignKey(User, unique=False)
    galvideotitle = models.CharField(max_length=100)
    galvideo = models.ImageField(upload_to='galleryvideo', blank=True, null=True)
#------------- 1st JUNE -------------------
class jobs(models.Model):
    emp = models.ForeignKey(User, unique=False)
    title = models.CharField(max_length=100)
    referencecode = models.CharField(max_length=100)
    jobsummary = models.TextField()
    jobdetails = models.TextField()
    industry = models.CharField(max_length=100)
    functionalarea = models.CharField(max_length=100)
    min_exp = models.IntegerField(default=0)
    max_exp = models.IntegerField(default=0)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    address3 = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=10)
    lat=models.CharField(max_length=40,blank=True,null=True)
    lng=models.CharField(max_length=40,blank=True,null=True)
    typ=models.CharField(max_length=75,blank=True,null=True)
    ownername = models.CharField(max_length=100)
    workno = models.CharField(max_length=100)
    handno = models.CharField(max_length=100)
    fax = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    marklive = models.DateTimeField(blank=True,null=True)
    todate = models.DateTimeField(blank=True,null=True)
    jobtype = models.CharField(max_length=100)
    salary_range = models.CharField(max_length=100)
    qualification = models.CharField(max_length=500)
    empsecretclear = models.CharField(max_length=100)
    emptravel = models.CharField(max_length=20)
    emptele = models.BooleanField(default=False, blank=True)
    workpermit = models.CharField(max_length=100, blank=True)
    hitcount=models.IntegerField(default=0)
    viewcount=models.IntegerField(default=0)
    is_active=models.BooleanField(default=False)
    is_delete=models.BooleanField(default=False)

class employerkeyskills(models.Model):
    emp=models.ForeignKey(User, unique=False)
    job=models.ForeignKey(jobs, unique=False)
    keyskills=models.CharField(max_length=50)

class emppacks(models.Model):
    pack_name = models.CharField(max_length=100)
    pack_description = models.TextField()
    pack_duration = models.IntegerField(default=0)
    pack_cost = models.DecimalField(max_digits=5, decimal_places=2)
    no_resume = models.IntegerField(default=0)
    no_jobpost = models.IntegerField(default=0)
    def __unicode__(self):
        return self.pack_name
class emp_subscribed_packs(models.Model):
    employer = models.ForeignKey(User,unique=False)
    pack = models.ForeignKey(emppacks,unique=False)
    pack_activate = models.DateTimeField()
    pack_expire = models.DateTimeField()
    def __unicode__(self):
        return self.employer.username
        #return self.pack.pack_name
class emppack_activation(models.Model):
    subscribed_pack=models.ForeignKey(emp_subscribed_packs,unique=False)
    pack = models.ForeignKey(emppacks,unique=False)
    totaljobpost = models.IntegerField(default=0)
    totalresume = models.IntegerField(default=0)
    total_activated_job = models.IntegerField(default=0)
    total_viewed_resume = models.IntegerField(default=0)
    is_active=models.BooleanField(default=True)
    def __unicode__(self):
        return self.subscribed_packs.employer.username
        return self.subscribed_packs.pack.pack_name
class profileviews(models.Model):
    employer=models.ForeignKey(User)
    jobseeker=models.IntegerField(max_length=10)
    viewDatetime=models.DateTimeField(auto_now=True)

class SaveCandidateFolderManager(models.Manager):
    def foldercount_fname(self,*arg):
        return self.filter(employer_id=arg[0],folder=arg[1]).count()

class RecruiterFolder(models.Model):
    foldername=models.CharField(max_length=100,blank=False)
    employer=models.ForeignKey(User, unique=False)
    lastupdate= models.CharField(max_length=100)
    #lastupdate=models.DateTimeField(auto_now = True)

class SaveCandidateFolder(models.Model):
    folder=models.ForeignKey(RecruiterFolder,unique=False)
    employer=models.ForeignKey(User, unique=False)
    jobseeker=models.ForeignKey(JSDetails, unique=False)
    dateupdate=models.DateTimeField(auto_now = True)
    objects=SaveCandidateFolderManager()

class RecSaveSearch(models.Model):
    employer=models.ForeignKey(User,unique=False)
    searchname=models.CharField(max_length=100,blank=True)
    savedsearch=models.CharField(max_length=400, blank=True)

class BlogTopics(models.Model):
    blogtopic=models.CharField(max_length=100,blank=True)
    blogImgurl=models.ImageField(upload_to='BlogTopicImage', blank=True)
    def __unicode__(self):
        return self.blogtopic
class Blog(models.Model):
    user=models.ForeignKey(User,unique=False)
    btopic=models.ForeignKey(BlogTopics,unique=False)
    btitle=models.CharField(max_length=250,blank=True)
    bimage=models.ImageField(upload_to='BlogImage', blank=True, null=True)
    bcontent=models.TextField(blank=True)
    bposted=models.DateTimeField(auto_now = True)
    def __unicode__(self):
        return self.btitle
class BComments(models.Model):
    user=models.ForeignKey(User,unique=False)
    blog=models.ForeignKey(Blog,unique=False)
    comments=models.TextField(blank=True)
    commentpost=models.DateTimeField(auto_now = True)
class Interview(models.Model):
    emp=models.ForeignKey(User,unique=False)
    JSId=models.ForeignKey(JSDetails,unique=False)
    Job=models.ForeignKey(jobs, unique=False)
    Denied=models.BooleanField(default=False)
    interviewpassed=models.BooleanField(default=False)
    interviewfailed=models.BooleanField(default=False)
    rounds=models.CharField(max_length=10)
    interviewLocation = models.CharField(max_length=250)
class Reschedule(models.Model):
    interview=models.OneToOneField(Interview)
    emp=models.ForeignKey(User, unique=False)
    JSId=models.ForeignKey(JSDetails,unique=False)
    Job=models.ForeignKey(jobs, unique=False)
    jsschedule_date1=models.CharField(max_length=50, blank=True)
    jsschedule_time1=models.CharField(max_length=50, blank=True)
    jsupdate1=models.CharField(max_length=50)
    jsschedule_date2=models.CharField(max_length=50, blank=True)
    jsschedule_time2=models.CharField(max_length=50, blank=True)
    jsupdate2=models.CharField(max_length=50)
    jsschedule_date3=models.CharField(max_length=50, blank=True)
    jsschedule_time3=models.CharField(max_length=50, blank=True)
    jsupdate3=models.CharField(max_length=50)
    empschedule_date1=models.CharField(max_length=50, blank=True)
    empschedule_time1=models.CharField(max_length=50, blank=True)
    empupdate1=models.CharField(max_length=50)
    empschedule_date2=models.CharField(max_length=50, blank=True)
    empschedule_time2=models.CharField(max_length=50, blank=True)
    empupdate2=models.CharField(max_length=50)
    empschedule_date3=models.CharField(max_length=50, blank=True)
    empschedule_time3=models.CharField(max_length=50, blank=True)
    empupdate3=models.CharField(max_length=50)
    JSconfirmation=models.BooleanField(default=False)
    Empconfirmation=models.BooleanField(default=False)
class InterviewRounds(models.Model):
    interview=models.ForeignKey(Interview,unique=False)
    emp=models.ForeignKey(User, unique=False)
    JSId=models.ForeignKey(JSDetails,unique=False)
    Job=models.ForeignKey(jobs, unique=False)
    roundno=models.IntegerField(default=0)
    score=models.IntegerField(default=0)
    interviewby=models.CharField(max_length=75)
    interviewdate=models.CharField(max_length=50)
    tips=models.CharField(max_length=1000)
    nextrounddate=models.CharField(max_length=50)
    status=models.BooleanField(default=False)
class jspacks(models.Model):
    pack_name = models.CharField(max_length=100)
    pack_description = models.TextField()
    pack_duration = models.IntegerField()
    nojob_applied = models.IntegerField()
    pack_cost = models.DecimalField(max_digits=5, decimal_places=2)
    def __unicode__(self):
        return self.pack_name
class jssubscribed_packs(models.Model):
    jobseeker = models.ForeignKey(User)
    pack = models.ForeignKey(jspacks)
    pack_activate = models.DateTimeField()
    pack_expire = models.DateTimeField()
    def __unicode__(self):
        return self.jobseeker.username
        #return self.pack.pack_name
class JSAppliedJobs(models.Model):
    JS=models.ForeignKey(JSDetails, unique=False)
    emp=models.ForeignKey(User, unique=False)
    Job=models.ForeignKey(jobs, unique=False)
    applieddate=models.DateTimeField(auto_now=True)
    jsappdel=models.BooleanField(default=True)
    empappdel=models.BooleanField(default=True)
class JSsavesearch(models.Model):
    user=models.ForeignKey(User, unique=False)
    searchname=models.CharField(max_length=100)
    searchlinks=models.CharField(max_length=500)
    ip_address=models.CharField(max_length=500)
class newsletter(models.Model):
    USERTYPES = (
        ('Employer', 'Employer'),
        ('Jobseeker', 'Jobseeker'),
    )
    usertype=models.CharField(max_length=50,choices=USERTYPES)
    topics=models.CharField(max_length=100)
    content=models.TextField(blank=True)
    sentdate=models.DateTimeField(auto_now = True)



class EmpSubscription(models.Model):
    employer = models.ForeignKey(User)
    pack = models.ForeignKey(emppacks)
    pack_activate = models.DateTimeField(auto_now_add=True)
    #pack_expire = models.DateTimeField()
    def __unicode__(self):
        return self.employer.username


from paypal.standard.ipn.signals import payment_was_successful
def show_me_the_money(sender, **kwargs):
    ipn_obj = sender
    EmpSubscription(employer_id=ipn_obj.custom,pack_id=ipn_obj.item_number).save()
payment_was_successful.connect(show_me_the_money)
