"""
Views which allow users to create and activate accounts.

"""

from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from models import RegistrationProfile
from forms import *
from django.contrib.auth.decorators import login_required
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse,Http404
from django.contrib.auth import logout
from registration.models import *
from django.template.loader import get_template
from django.contrib.auth.models import User
import random, re, sha,time
from django.contrib.sites.models import Site
from django.template import Context, loader
from django.core.mail import send_mail, EmailMessage,EmailMultiAlternatives
from django.core.context_processors import csrf
from django.db.models import Q
from datetime import datetime,timedelta
from django.db.models import Count
from django.contrib.auth import authenticate,login
#------- 1st JUNE -------------
import os
from subprocess import call
from settings import MEDIA_URL
from django.contrib import messages
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import user_passes_test
from urlparse import urlparse,parse_qs
from math import sin, cos, radians, degrees, acos
from geopy import geocoders
gn = geocoders.GeoNames()
from email.mime.image import MIMEImage

def recordvideo(request):

    #class RecordedVideos(models.Model):
    #user=models.ForeignKey(User)
    #filepath=models.CharField(max_length=100)
    #filename=models.CharField(max_length=50)
    #uploadon=models.DateTimeField(auto_now=True)
    #if created:img = pjoin(settings.MEDIA_URL,"nopicture.jpg")

    if 'filename' in request.GET:
        rvideo, created = RecordedVideos.objects.get_or_create(user=request.user)
        rvideo.filename=request.GET['filename']
        rvideo.filepath='/static/videoresume/'
        rvideo.save()
        return HttpResponseRedirect('/accounts/Profile')

    return render(request,'registration/recordvideoform.html')


def miles(request):
    now=datetime.now()
    d1=datetime(now.year, now.month, now.day)
    d2=datetime(now.year, now.month, now.day-2)
    fd=d1.strftime('%m-%d-%Y')
    td=d2.strftime('%m-%d-%Y')
    query=Q(marklive__lte=fd) & Q(todate__gte=fd)
    query1=Q(marklive__gte=td) & Q(marklive__lte=fd)
    
    for i in JSsavesearch.objects.all():
        urls=i.searchlink
        fname=i.user.first_name
        tomail=i.user.email
        searchname=i.searchname
        lastupdate=i.user.jsdetails.update_date
        p=parse_qs(urlparse(urls).query)
        list_result=[]
        for search in p['keywords'][0].split(','):
            if search=='':break
            for res in jobs.objects.filter(query,query1,Q(employerkeyskills__keyskills__icontains=search) | Q(title__icontains=search) | Q(city__icontains=search) | Q(state__icontains=search) | Q(country__icontains=search) | Q(zipcode__icontains=search) & Q(is_active=True)):
                if not res in list_result:
                    list_result.append(res)
        #d=[]       
        
        contxt=Context({'d':list_result,'fname':fname,'searchname':searchname,'now':now,'lastupdate':lastupdate})            
        message_template = loader.get_template('registration/job_alert_mail.html')    
        message=message_template.render(contxt)
        msg=EmailMultiAlternatives('iTechTalents.com Job Alerts',message,'itechtalentalerts@itechtalents.com',[tomail])
        msg.attach_alternative(message, "text/html")
        image_file = open('/home/capsone-system7/Karthik/Git/tt/19jun/userreg/media/images/itechtalentslogo.jpg', 'rb')
        msg_image = MIMEImage(image_file.read())
        image_file.close()
        msg_image.add_header('Content-ID', '<image1>')
        msg.attach(msg_image)
        msg.send()
    #print datetime.strptime(i.marklive, '%m-%d-%Y')
    #lat_a = radians(13.0147757)
    #lat_b = radians(11.1013051)
    #long_diff = radians(80.2045137 - 76.99076749999995)
    #distance = (sin(lat_a) * sin(lat_b) + cos(lat_a) * cos(lat_b) * cos(long_diff))
    #miles=degrees(acos(distance)) * 69.09
    #return HttpResponse(miles)

def rss201(request,bits):
    from django.utils.feedgenerator import Rss201rev2Feed
    list_result=[]
    for res in jobs.objects.filter(Q(employerkeyskills__keyskills__icontains=bits) | Q(title__icontains=bits) | Q(city__icontains=bits) | Q(state__icontains=bits) | Q(country__icontains=bits) | Q(zipcode__icontains=bits)):
            if not res in list_result:
                list_result.append(res)
    object_list=list_result
    feedtitle=u"Showing the RSS Feeds on %s" % bits
    site_link = u'http://192.168.1.33:8001/'
    feed = Rss201rev2Feed( title=u"Italentss Job Search.com",
        link=site_link,
        description=feedtitle,
        language=u"en")

    for object in object_list:        
        link = site_link + unicode(object.id)
        desc = u"Job Summary: %s, Key Skills:, City: %s, Salary: %s, Qualification: %s" % (object.jobsummary,  object.city, object.salary_range, object.qualification)
        feed.add_item( title=object.title, link=link,
            description=desc)
    response = HttpResponse(mimetype='application/xml')
    feed.write(response, 'utf-8')
    return response


def createnew(request):
    newuser=User.objects.get(pk=request.user.pk)
    newuser.usertype='jobseeker'
    newuser.save()
    return HttpResponseRedirect('/accounts/Profile/')

def activate(request, activation_key):
    activation_key = activation_key.lower() # Normalize before trying anything with it.
    account = RegistrationProfile.objects.activate_user(activation_key)
    return render(request,'registration/activate.html',{'account': account,'expiration_days': settings.ACCOUNT_ACTIVATION_DAYS })
def register(request):
    if request.method == 'POST':
        #form = RegistrationForm(request.POST)
        #if form.is_valid():
        new_user = RegistrationProfile.objects.create_inactive_user(username=request.POST['username'],
                                                                        password=request.POST['password1'],
                                                                        email=request.POST['email'])
        new_user.first_name = request.POST['first_name']
        new_user.last_name = request.POST['last_name']
        new_user.usertype = request.POST['usertype']
        new_user.save()
        securityquestions(user_id=new_user.id,question=request.POST['question'],answer=request.POST['answer']).save()
        return HttpResponseRedirect('/accounts/registercomplete/')

    else:
        import json
        if 'param1' in request.GET:
            param1=request.GET['param1']
            valz= request.GET['param2']
            if param1=='username':
                already_exist=User.objects.filter(username=valz).exists()
            
            elif param1=='email':already_exist=User.objects.filter(email=valz).exists()
            
            return HttpResponse(json.dumps({'already':already_exist,'fname':param1}), mimetype="application/json")
    #else:
    #    form = RegistrationForm()
    #return render_to_response('registration/registration_form.html',{'form': form },context_instance=RequestContext(request))

def empreg(request):
    if request.method == 'POST':
        form = EmpRegistrationForm(request.POST)
        if form.is_valid():
            new_user = RegistrationProfile.objects.create_inactive_user(username=form.cleaned_data['username'],
                                                                        password=form.cleaned_data['password1'],
                                                                        email=form.cleaned_data['email'])
            new_user.companyname = form.cleaned_data['companyname']
            new_user.usertype = form.cleaned_data['usertype']
            new_user.save()           
            e=EmployerReg_Form(user_id=new_user.id, companytype=form.cleaned_data['companytype'],contactno=form.cleaned_data['contactno'],contactperson=form.cleaned_data['contactperson'],companyurl=form.cleaned_data['companyurl'],companylogo="",companyprofile="")
            e.save()
            securityquestions(user_id=new_user.id,question=request.POST['question'],answer=request.POST['answer']).save()
            return HttpResponseRedirect('/accounts/EmpReg_Complete/')
    else:
        import json
        if 'param1' in request.GET:
            param1=request.GET['param1']
            valz= request.GET['param2']
            if param1=='username':
                already_exist=User.objects.filter(username=valz).exists()
            elif param1=='companyurl':
                already_exist=User.objects.filter(employerreg_form__companyurl__icontains=valz).exists()
            elif param1=='email':already_exist=User.objects.filter(email=valz).exists()
            elif param1=='companyname':already_exist=User.objects.filter(companyname=valz).exists()
            return HttpResponse(json.dumps({'already':already_exist,'fname':param1}), mimetype="application/json")
    return render_to_response('registration/empregform.html', context_instance=RequestContext(request))

        #empavailpack = emp_avail_packs.objects.all()
    #return render_to_response('registration/empregform.html', { 'form': form }, context_instance=RequestContext(request))
def home(request):
    now=datetime.now()
    d=datetime(now.year, now.month, now.day)
    d1= d.strftime('%m-%d-%Y')
    
    latest = jobs.objects.filter(marklive__lte=d1,todate__gte=d1).order_by('-marklive')
    trending = jobs.objects.filter(marklive__lte=d1,todate__gte=d1).order_by('-hitcount')
    details2 = User.objects.filter(jobs__isnull=False).annotate(job_count=Count('jobs')).order_by('-job_count')
    demand = jobs.objects.values('state').annotate(count=Count('state')).order_by('-hitcount')
    startdate = datetime.strptime(d1, "%m-%d-%Y")
    enddate1 = startdate - timedelta(days=30)
    d2=enddate1.strftime('%m-%d-%Y')
    totalcount=jobs.objects.all().count()
    monthcount=jobs.objects.filter(Q(marklive__lte=d1)&Q(marklive__gte=d2)).count()
    daycount=jobs.objects.filter(marklive=d1).count()
    #return HttpResponse(daycount)
    return render(request,'registration/home.html', {'latest': latest,'trending':trending,'details2':details2,'demand':demand,'monthcount':monthcount,'totalcount':totalcount,'daycount':daycount})

def HotJobs(request):
    now=datetime.now()
    d=datetime(now.year, now.month, now.day)
    d1= d.strftime('%m-%d-%Y')
    hotjobs = jobs.objects.filter(marklive__lte=d1,todate__gte=d1).order_by('-hitcount')
    return render(request,'registration/HotJobs.html', {'hotjobs':hotjobs})

def SecretClearedJobs(request):
    now=datetime.now()
    d=datetime(now.year, now.month, now.day)
    d1= d.strftime('%m-%d-%Y')
    scjobs = jobs.objects.filter(~Q(empsecretclear='Not Need'),marklive__lte=d1,todate__gte=d1).order_by('-marklive')
    return render(request,'registration/SecretClearedJobs.html', {'scjobs':scjobs})

def adv_search(request):
   return render(request,'registration/advanced_search.html')

def search_result(request):
    if request.method == 'POST':
        saveurl=request.POST.get("savesearch")
        searchname=request.POST.get("JSsavejob")
        savesearch=JSsavesearch(user_id=request.user.id,searchname=searchname,searchlink=saveurl)
        savesearch.save()
        messages.success(request, 'Search agent saved successfully')
        return HttpResponseRedirect(saveurl)
    else:
        query1=Q(marklive__lte=datetime.now().date()) & Q(todate__gte=datetime.now().date())
        query3= Q(is_active=True)
        cleaned_query=request.GET['keywords'].strip()[:-1] if request.GET['keywords'].strip()[-1] == ',' else request.GET['keywords'].strip()
        searchresult = cleaned_query.split(',')        
        #searchresult = request.GET['keywords'].split(',')
        list_result=[]
        query=Q(todate__lte=datetime.now().date())
        for search in searchresult:
            for res in jobs.objects.filter(Q(employerkeyskills__keyskills__icontains=search) | Q(title__icontains=search) | Q(city__icontains=search) | Q(state__icontains=search) | Q(country__icontains=search) | Q(zipcode__icontains=search),query1,query3):
                if not res in list_result:
                    list_result.append(res)
        details=list_result
        details2 = User.objects.filter(jobs__isnull=False).annotate(job_count=Count('jobs')).order_by('-job_count')
        details3 = jobs.objects.values('state').annotate(count=Count('state')).order_by('-count')
        details4 = jobs.objects.values('industry').annotate(count=Count('industry')).order_by('-count')
        savecount=JSsavesearch.objects.filter(user_id=request.user.id).count()
        msg=5-savecount
        return render(request,'registration/searchresult.html', {'details': details,'details2':details2,'details3':details3,'details4':details4,'msg':msg,})

def companyjoblist(request,user_id):
    userid=user_id
    query=Q(emp__companyname=userid) | Q(state=userid) | Q(industry=userid)
    details=jobs.objects.filter(query)
    details2 = User.objects.filter(jobs__isnull=False).annotate(job_count=Count('jobs')).order_by('-job_count')
    details3 = jobs.objects.values('state').annotate(count=Count('state')).order_by('-count')
    details4 = jobs.objects.values('industry').annotate(count=Count('industry')).order_by('-count')
    savecount=JSsavesearch.objects.filter(user_id=request.user.id).count()
    msg=5-savecount
    return render(request,'registration/searchresult.html', {'details': details,'details2':details2,'details3':details3,'details4':details4,'msg':msg})
def jobfulldescription(request,job_id):
    vcount=jobs.objects.get(id=job_id)
    count=vcount.viewcount
    count=count+1
    vcount.viewcount=count
    vcount.save()
    emps=jobs.objects.get(id=job_id)
    empid=emps.emp_id
    applied=''
    try:
        applied=JSAppliedJobs.objects.filter(JS_id=request.user.jsdetails.id,Job_id=job_id,emp_id=empid)
        description=jobs.objects.filter(id=job_id)
    except:
        description=jobs.objects.filter(id=job_id)
    return render(request,'registration/jobs_description.html',{'applied':applied,'description':description})
@login_required(login_url='/accounts/EmpReg/')
def jobfulldescriptionemp(request,job_id):
    jobid=job_id
    description=jobs.objects.filter(id=jobid)
    keyskills=employerkeyskills.objects.filter(job_id=jobid,emp_id=request.user.id)
    cmpdetails = EmployerReg_Form.objects.filter(user_id=request.user.id)
    return render(request,'registration/jobs_descriptionemp.html',{'description':description,'keyskills':keyskills,'cmpdetails':cmpdetails})
@login_required(login_url='/accounts/EmpReg/')
def EmployerProfile(request):
    details = User.objects.filter(id=request.user.id)
    details1 = EmployerReg_Form.objects.filter(user_id=request.user.id)
    empsavesearch=RecSaveSearch.objects.filter(employer_id=request.user.id)
    folder=RecruiterFolder.objects.filter(employer_id=request.user.id)
    for i in folder:
        i.fcount=SaveCandidateFolder.objects.foldercount_fname(request.user.id,i)
    return render(request,'registration/emp_profile.html',{'folders':folder,'savesearch':empsavesearch,'details':details,'details1':details1})
@login_required(login_url='/accounts/EmpReg/')
def JobsEmp(request):
    import json
    if 'param1' in request.GET:
        param1=request.GET['param1']
        valz= request.GET['param2']
        if param1=='foldername':
            already_exist=RecruiterFolder.objects.filter(foldername=valz,employer_id=request.user.id).exists()        
        return HttpResponse(json.dumps({'already':already_exist,'fname':param1}), mimetype="application/json")
    msg=""
    job = jobs.objects.filter(emp_id=request.user.id).count()
    remaining = 5-job
    msg = "You Have Posted %s Jobs and "% job 
    msg1 = "You Have %s Job Posts Remaining"% remaining
    query1=Q(emp_id=request.user.id)
    query2=Q(marklive__gt=datetime.now())
    query3=Q(todate__gte=datetime.now())
    query4=Q(todate__lt=datetime.now())
    query5=Q(marklive__lte=datetime.now())
    query6=Q(is_active=True)
    query7=Q(is_active=False)
    PendingJobList=jobs.objects.filter(query1,query2,query6)
    ActJobList=jobs.objects.filter(query1,query3,query5,query6)
    InactJobList=jobs.objects.filter(query1,query4,query7)
    query = Q(emp_id=request.user.id)
    return render(request,'registration/jobs_emp.html', {'msg': msg,'msg1':msg1,'remaining':remaining,'ActJobList':ActJobList, 'InactJobList':InactJobList})
@login_required(login_url='/accounts/EmpReg/')
def UpdateEmployerProfile(request):
    if request.method == "POST":
        user = request.POST.get('user_id')
        companyurl = request.POST.get('companyurl')
        companytype = request.POST.get('companytype')
        contactperson = request.POST.get('contactperson')
        contactno = request.POST.get('contactno')
        companylogo = request.FILES.get('companylogo')
        companyprofile = request.POST.get('companyprofile')
        try:
            if companylogo:
                edit = EmployerReg_Form.objects.get(user_id=user)
                cmplogo = edit.companylogo
                if cmplogo:
                    os.remove(settings.CURRENT_DIR+"/media/"+str(cmplogo))                
                edit.companyurl=companyurl
                edit.companytype=companytype
                edit.contactperson=contactperson
                edit.contactno=contactno
                edit.companylogo=companylogo
                edit.companyprofile=companyprofile
                edit.save()
            else:
                edit = EmployerReg_Form.objects.get(user_id=user)
                edit.companyurl=companyurl
                edit.companytype=companytype
                edit.contactperson=contactperson
                edit.contactno=contactno
                edit.companyprofile=companyprofile
                edit.save()
            messages.success(request, 'Profile updated successfully')
            return HttpResponseRedirect('/accounts/RecruiterDashboard/')
        except:
            p = EmployerReg_Form(user_id=user,companyurl=companyurl,companytype=companytype,contactperson=contactperson,contactno=contactno,companylogo=companylogo,companyprofile=companyprofile)
            p.save()
            messages.success(request, 'Profile updated successfully')
            return HttpResponseRedirect('/accounts/RecruiterDashboard/')
    else:
        details = User.objects.filter(id=request.user.id)
        details1 = EmployerReg_Form.objects.filter(user_id=request.user.id)
        return render(request,'registration/update_emp_profile.html', {"details":details, "details1":details1}, context_instance=RequestContext(request))
@login_required(login_url='/accounts/EmpReg/')
def AddEmpGallery(request):
    if request.method == "POST":
        empid = request.POST.get('user_id')
        galpic = request.FILES.get('galpic')
        galpictitle = request.POST.get('galpictitle') 
        p = Emp_Gallery(emp_id=empid,galpic=galpic,galpictitle=galpictitle)
        p.save()
        messages.success(request, 'Gallery updated successfully')
        return HttpResponseRedirect('/accounts/RecruiterDashboard/')    
@login_required(login_url='/accounts/EmpReg/')
def AddEmpGalleryVideo(request):
    if request.method == "POST":
        empid = request.POST.get('user_id')
        galvideo = request.FILES.get('galvideo')
        galvideotitle = request.POST.get('galvideotitle')
        p = Emp_Gallery_video(emp_id=empid,galvideo=galvideo,galvideotitle=galvideotitle)
        p.save()
        messages.success(request, 'Gallery updated successfully')
        return HttpResponseRedirect('/accounts/RecruiterDashboard/')
@login_required(login_url='/accounts/EmpReg/')
def ViewEmpGallery(request):
    picgallery = Emp_Gallery.objects.filter(emp_id=request.user.id)
    videogallery = Emp_Gallery_video.objects.filter(emp_id=request.user.id)
    return render(request,'registration/EmpGallery_view.html', {"picgallery":picgallery,"videogallery":videogallery})
@login_required(login_url='/accounts/EmpReg/')
def DeleteEmpGallery(request):
    if request.method == "POST":
        galid = request.POST.get('galid')
        picturegallery = Emp_Gallery.objects.get(id=galid)
        picturefile=picturegallery.galpic
        os.remove(settings.CURRENT_DIR+"/media/"+str(picturefile))
        picturegallery.delete()
        messages.success(request, 'Picture Deleted successfully')
        return HttpResponseRedirect('/accounts/RecruiterDashboard/')
@login_required(login_url='/accounts/EmpReg/')
def DeleteEmpGalleryVideo(request):
    if request.method == "POST":
        galid = request.POST.get('galid')
        videogallery = Emp_Gallery_video.objects.get(id=galid)
        videofile=videogallery.galvideo
        os.remove(settings.CURRENT_DIR+"/media/"+str(videofile))
        videogallery.delete()
        messages.success(request, 'Video Deleted successfully')
        return HttpResponseRedirect('/accounts/RecruiterDashboard/')


#############################################################################

@csrf_exempt
@login_required(login_url='/accounts/login/')
def addresume(request):
    details = User.objects.filter(id=request.user.id)
    details1 = JSResume.objects.filter(user_id=request.user.id)

    if request.method == "POST":
        user_id = request.POST.get('userid')
        resume = request.FILES.get('resume')

        name, fileExtension = os.path.splitext(str(resume))
        resume_title = request.POST.get('resume_title')
        
        JS=JSDetails.objects.get(user_id=user_id)
        JS_id=JS.id
        rescount= JSResume.objects.filter(user_id=user_id).count()
        if rescount is 1:
            res=JSResume.objects.get(user_id=request.user.id)
            if not res.resumeFile:
                addres=JSResume.objects.get(user_id=user_id)
                addres.resumeTitle=resume_title
                addres.resumeFile=resume
                addres.save()

                resu=JSResume.objects.get(user_id=request.user.id)
                resumefile=resu.resumeFile
                call(["unoconv","-f","html","-o",settings.CURRENT_DIR+"/tagging/templates/documents/",settings.CURRENT_DIR+"/media/"+str(resumefile)])
                messages.success(request, '1 resume added successfully')
                return HttpResponseRedirect("/accounts/Profile/")
            else:

                addresume=JSResume(user_id=user_id,JS_id=JS_id,resumeTitle=resume_title,resumeFile=resume)
                addresume.save()
                messages.success(request, '1 resume added successfully')
                return HttpResponseRedirect("/accounts/Profile/")
        else:
            addresume=JSResume(user_id=user_id,JS_id=JS_id,resumeTitle=resume_title,resumeFile=resume)
            addresume.save()
            messages.success(request, '1 resume added successfully')
            return HttpResponseRedirect("/accounts/Profile/")
        

    else:
        if not details1:
            msg1 = "To add resumes you need to register your details"
            msg2 ="Here"
            return render_to_response('registration/add_new_resume.html',{'msg1': msg1, 'msg2':msg2},context_instance=RequestContext(request))
        else:
            rescount= JSResume.objects.filter(user_id=request.user.id).count()
            rem=5-rescount
            if rescount is 1:
                res=JSResume.objects.get(user_id=request.user.id)
                if res.resumeFile:
                    
                    msg='You had upload %s resume(s) only %s resume(s) remaining' %(rescount,rem)
                    return render_to_response('registration/add_new_resume.html', {'msg': msg,'counting':rem}, context_instance=RequestContext(request))
                    
                else:

                    counting=rescount

                    msg='You had upload 0 Resume only 5 Resume remaining'
                    return render_to_response('registration/add_new_resume.html', {'msg': msg,'counting':rem}, context_instance=RequestContext(request))
            elif rescount is 5:
                counting=rescount
                msg='You had upload %s resume(s) only %s resume(s) remaining' %(rescount,rem)
                return render_to_response('registration/add_new_resume.html', {'msg': msg,'counting':rem}, context_instance=RequestContext(request))
            else:
                
                counting=rescount
                msg='You had upload %s resume(s) only %s resume(s) remaining' %(rescount,rem)
                return render_to_response('registration/add_new_resume.html', {'msg': msg,'counting':rem}, context_instance=RequestContext(request))



@login_required(login_url='/accounts/login/')
def Updateresume(request):
        
        if request.method == "POST":
            user = request.POST.get('user_id')
            textTitle = request.POST.get('textResumeTitle')
            textFile = request.POST.get('textResumeFile')
            editTextResume=JSTextResume.objects.get(user_id=user)
            editTextResume.resumeTitle=textTitle
            editTextResume.resumeFile=textFile
            editTextResume.save()

            videoresume = request.FILES.get('videoresume')
            if videoresume:
                editvideores = JSVideoResume.objects.get(user_id=user)
                editvideores.videoresume = videoresume
                editvideores.save()

            for i in range(1,6):
                jsresid= request.POST.get('jsResumeID'+str(i),'')
                if not jsresid:break
                resid=JSResume.objects.get(user_id=user,pk=int(jsresid))
                resid.resumeTitle=request.POST.get('jsResumeTitle'+str(i))
                
                if request.FILES.get('jsResumeFile'+str(i)):
                    resufile=resid.resumeFile
                    #return HttpResponse(str(resufile))
                    if resufile:
                        #return HttpResponse('hliuj')
                        name, fileExtension = os.path.splitext(str(resufile))
                        os.remove(settings.CURRENT_DIR+"/media/"+str(resufile))
                        try:
                            os.remove(settings.CURRENT_DIR+"/tagging/templates/%s.html"%name)
                            resid.resumeFile=request.FILES.get('jsResumeFile'+str(i))
                            resid.save()
                        except:
                            resid.resumeFile=request.FILES.get('jsResumeFile'+str(i))
                            resid.save()
                    else:
                        resid=JSResume.objects.get(user_id=user,pk=int(jsresid))
                        resid.resumeTitle=request.POST.get('jsResumeTitle'+str(i))
                        resid.resumeFile=request.FILES.get('jsResumeFile'+str(i))
                        resid.save()
                resid.save()
                if JSResume.objects.filter(user_id=user).count() is 1:
                    resFile = JSResume.objects.get(user_id=user)
                    resumefile=resFile.resumeFile
                    call(["unoconv","-f","html","-o",settings.CURRENT_DIR+"/tagging/templates/documents/",settings.CURRENT_DIR+"/media/"+str(resumefile)])

            messages.success(request, 'Resume edited successfully')
            return HttpResponseRedirect('/accounts/Profile/')
           
        else:
            details = User.objects.get(id=request.user.id)
            details1 = JSResume.objects.filter(user_id=request.user.id)

            if details1:
                details = User.objects.filter(id=request.user.id)
                rescount = JSResume.objects.filter(user_id=request.user.id).count()
                details1 = JSResume.objects.filter(user_id=request.user.id)
                details2 = JSTextResume.objects.filter(user_id=request.user.id)
                videoresume = JSVideoResume.objects.filter(user_id=request.user.id)
                return render_to_response('registration/update_resume.html', {"rescount":rescount,"details":details,"details1":details1,"details2":details2,'videoresume':videoresume}, context_instance=RequestContext(request))
            else:

                msg = "U have not added any resumes To add resume "
                msg1 ="Click Here"
                
                return render_to_response('registration/update_resume.html', {'msg': msg, 'msg1':msg1}, context_instance=RequestContext(request))

@login_required(login_url='/accounts/login/')
def DeleteResume(request,res_id):
    userid = request.user.id
    resid = res_id
    deleteResume=JSResume.objects.get(id=resid)
    drid=deleteResume.id
    try:
        activateresume = JSResumeActive.objects.get(user_id=userid)
        arid = activateresume.resumeActive_id
        #return HttpResponse(arid)
        if drid==arid:
            resumefile=deleteResume.resumeFile

            name, fileExtension = os.path.splitext(str(resumefile))
            os.remove(settings.CURRENT_DIR+"/media/"+str(resumefile))
            os.remove(settings.CURRENT_DIR+"/tagging/templates/%s.html"%name)
            deleteResume.delete()
        else:
            #else HttpResponse('sdgs')
            resumefile=deleteResume.resumeFile
            os.remove(settings.CURRENT_DIR+"/media/"+str(resumefile))
            deleteResume.delete()

    except:
        #return HttpResponse('sdg')
        #deleteResume=JSResume.objects.get(id=resid)
        resumefile=deleteResume.resumeFile
        os.remove(settings.CURRENT_DIR+"/media/"+str(resumefile))
        deleteResume.delete()


    counts=JSResume.objects.filter(user_id=request.user.id).count()

    if counts is 0:
        js=JSDetails.objects.get(user_id=request.user.id)
        JSid=js.id
        res=JSResume(user_id=request.user.id,JS_id=JSid)
        res.save()
        actres=JSResume.objects.get(user_id=request.user.id)
        resid=actres.id
        act=JSResumeActive(user_id=request.user.id,JS_id=JSid,resumeActive_id=resid)
        act.save()
        tres=JSTextResume.objects.get(user_id=request.user.id)
        tresfile=tres.resumeFile
        if tresfile:
            tres.activetext_resume=True
            tres.save()

    messages.success(request, 'Resume deleted successfully')
    return HttpResponseRedirect('/accounts/Profile/')


@login_required(login_url='/accounts/login/')
def DeleteVideoResume(request,vs_id):
    vsid = vs_id
    deleteResume=JSVideoResume.objects.get(id=vsid)
    deleteResume.delete()

    js=JSDetails.objects.get(user_id=request.user.id)
    jsid=js.id
    addvideores = JSVideoResume(user_id=request.user.id,JS_id=jsid)
    addvideores.save()

    messages.success(request, 'Video resume deleted successfully')
    return HttpResponseRedirect('/accounts/Profile/')

@login_required(login_url='/accounts/login/')
def resume_activation(request):
    if request.method == "POST":
        resume = request.POST.get('res_act_title')

        userid = request.POST.get('userid')
        tresume = request.POST.get('acttext_resume')
        JS=JSDetails.objects.get(user_id=userid)
        JS_id=JS.id
       
        if resume:
            
            query=Q(id=resume) & Q(user_id=userid)
            details = JSResume.objects.get(query)
            resumeid=details.id
            resumefile=details.resumeFile
	    #os.system("unoconv -f html -o /var/www/userreg/tagging/templates/documents /var/www/userreg/media/documents/resume_2.doc")
	    call(["unoconv","-f","html","-o",settings.CURRENT_DIR+"/tagging/templates/documents/",settings.CURRENT_DIR+"/media/"+str(resumefile)])

            try:
                resact=JSResumeActive.objects.get(user_id=userid)
                resact.resumeActive_id=resumeid
                resact.save()
                textresact=JSTextResume.objects.get(user_id=userid)
                textresact.activetext_resume=False
                textresact.save()
                JS=JSDetails.objects.get(user_id=userid)
                JS.update_date=datetime.now()
                JS.save()
                messages.success(request, 'Resume has been activated')
                return HttpResponseRedirect('/accounts/Profile/')
            except:
                resact=JSResumeActive(user_id=userid,JS_id=JS_id,resumeActive_id=resumeid)
                resact.save()
                textresact=JSTextResume.objects.get(user_id=userid)
                textresact.activetext_resume=False
                textresact.save()
                JS=JSDetails.objects.get(user_id=userid)
                JS.update_date=datetime.now()
                JS.save()
                messages.success(request, 'Resume has been activated')
                return HttpResponseRedirect('/accounts/Profile/')
        else:
            query1=Q(resumeTitle=tresume) & Q(user_id=userid)
            tres=JSTextResume.objects.get(query1)
            tres.activetext_resume=True
            tres.save()
            JS=JSDetails.objects.get(user_id=userid)
            JS.update_date=datetime.now()
            JS.save()
            messages.success(request, 'Resume has been activated')
            return HttpResponseRedirect('/accounts/Profile/')
    else:
        user=request.user.id
        textresume=JSTextResume.objects.filter(user_id=user)
        profile_detail=JSResume.objects.filter(user_id=user)
        try:

            txtres=JSTextResume.objects.get(user_id=user)
            if not txtres.activetext_resume:
                actres=JSResumeActive.objects.get(user_id=user)
                restitle=actres.resumeActive.resumeTitle

                return render(request,'registration/resume_activation.html', {'profile_detail':profile_detail,'textresume':textresume,'restitle':restitle}, context_instance=RequestContext(request))
            else:
                restitle=txtres.resumeTitle

                return render(request,'registration/resume_activation.html', {'profile_detail':profile_detail,'textresume':textresume,'restxttitle':restitle}, context_instance=RequestContext(request))
        except:

            return render(request,'registration/resume_activation.html', {'profile_detail':profile_detail,'textresume':textresume}, context_instance=RequestContext(request))



'''
@login_required
def visibility(request):
    details = User.objects.filter(id=request.user.id)
    details1 = js_details.objects.filter(user_id=request.user.id)
    return render_to_response('registration/profile_visibility.html',{"details":details,"details1":details1}, context_instance=RequestContext(request))
'''

@login_required(login_url='/accounts/login/')
def visibility(request):
        details1 = JSDetails.objects.filter(user_id=request.user.id)
        if not details1:
            msg="To configure your visibility settings, you must want to add your details. Click "
            msg1="here"
            return render(request,'registration/profile_visibility.html',{"msg":msg,"msg1":msg1}, context_instance=RequestContext(request))
        else:

            return render(request,'registration/profile_visibility.html',{"details1":details1}, context_instance=RequestContext(request))


@login_required(login_url='/accounts/login/')
def Visibility_page(request):
    users=request.user.id
    detail=JSDetails.objects.get(user_id=users)
    if request.method == "POST":
        jsstatus = request.POST.get('status')
        if jsstatus=="active":
            edit = JSDetails.objects.get(user_id=users)
            edit.visiblity=True
            edit.visiblepassive=False
            edit.update_date=datetime.now()
            edit.save()
        elif jsstatus=="inactive":
            edit = JSDetails.objects.get(user_id=users)
            edit.visiblity=False
            edit.visiblepassive=False
            edit.update_date=datetime.now()
            edit.save()
        else:
            edit = JSDetails.objects.get(user_id=users)
            edit.visiblity=False
            edit.visiblepassive=True
            edit.update_date=datetime.now()
            edit.save()
        return HttpResponseRedirect('/accounts/ProfileVisibility/')


@login_required(login_url='/accounts/login/')
def editresume(request):
    users = User.objects.filter(id=request.user.id)
    detail = JSDetails.objects.filter(user_id=request.user.id)
    personal = JSPersonal.objects.filter(user_id=request.user.id)
    qualification = JSQualification.objects.filter(user_id=request.user.id)
    profilesum = JSProfileSummary.objects.filter(user_id=request.user.id)
    skills = JSSkills.objects.filter(user_id=request.user.id)
    employer = JSEmployerDetails.objects.filter(user_id=request.user.id)
    project = JSProjectDetails.objects.filter(user_id=request.user.id)
    other = JSDetailOther.objects.filter(user_id=request.user.id)
    extra = JSExtra.objects.filter(user_id=request.user.id)
    videoresume = JSVideoResume.objects.filter(user_id=request.user.id)
    jssecurity = JSsecurity.objects.filter(user_id=request.user.id)

    
    if not detail:
            return HttpResponseRedirect("/accounts/ProfileDetails/")

    else:
        
        text=JSTextResume.objects.get(user_id=request.user.id)
        act=text.activetext_resume
        tresume=JSTextResume.objects.filter(user_id=request.user.id)
        try:
            res=JSResumeActive.objects.get(user_id=request.user.id)
            resactid=res.resumeActive_id
            resume=JSResume.objects.filter(id=resactid)
            
            if act:

                return render_to_response('registration/profile_edit_view.html', {"users":users,'detail':detail,'personal':personal,'qualification':qualification,'profilesum':profilesum,'skills':skills,'employer':employer,'project':project,'other':other,'resume':tresume,'extra':extra,'videoresume':videoresume,'jssecurity':jssecurity}, context_instance=RequestContext(request))
            else:
                return render_to_response('registration/profile_edit_view.html', {"users":users,'detail':detail,'personal':personal,'qualification':qualification,'profilesum':profilesum,'skills':skills,'employer':employer,'project':project,'other':other,'resume':resume,'extra':extra,'videoresume':videoresume,'jssecurity':jssecurity}, context_instance=RequestContext(request))
        except:

            if act:

                return render_to_response('registration/profile_edit_view.html', {"users":users,'detail':detail,'personal':personal,'qualification':qualification,'profilesum':profilesum,'skills':skills,'employer':employer,'project':project,'other':other,'resume':tresume,'extra':extra,'videoresume':videoresume,'jssecurity':jssecurity}, context_instance=RequestContext(request))
            else:
                return render_to_response('registration/profile_edit_view.html', {"users":users,'detail':detail,'personal':personal,'qualification':qualification,'profilesum':profilesum,'skills':skills,'employer':employer,'project':project,'other':other,'extra':extra,'videoresume':videoresume,'jssecurity':jssecurity}, context_instance=RequestContext(request))


@login_required(login_url='/accounts/login/')
def edit_personal_info(request):
    
    if request.method == "POST":
        userid = request.POST.get('user_id')
        jsid = request.POST.get('jsid')
        fname= request.POST.get('fname')
        lastname= request.POST.get('lastname')
        dob = request.POST.get('dob')
        sec_email = request.POST.get('sec_email')
        address1 = request.POST.get('address1')
        address2 = request.POST.get('address2')
        country = request.POST.get('country')
        state = request.POST.get('state')
        city = request.POST.get('city')
        zipcode = request.POST.get('zipcode')
        ltn=request.POST.get('latitude')
        lng=request.POST.get('longitude')
        typ=request.POST.get('type')
        handno=request.POST.get('handno')
        homeno=request.POST.get('homeno')
        workno=request.POST.get('workno')
        prefertime=request.POST.get('prefertime')
        gender = request.POST.get('gender')
        maritalstatus = request.POST.get('maritalstatus')
        work_expyears= request.POST.get('work_expyears')
        work_expmonths= request.POST.get('work_expmonths')
        salaryrange= request.POST.get('salary')
        industry= request.POST.get('industry')
        functional_area= request.POST.get('functional_area')
        profileurl=request.POST.get('profileurl')
        
        edit1 = User.objects.get(id=userid)
        edit1.first_name =fname
        edit1.last_name = lastname
        edit1.save()
        
        try:
            editper = JSPersonal.objects.get(user_id=userid)
            editper.dob = dob
            editper.sec_email=sec_email
            editper.address1=address1
            editper.address2=address2
            editper.country=country
            editper.state=state
            editper.city=city
            editper.zipcode=zipcode
            editper.lat=ltn
            editper.lng=lng
            editper.typ=typ
            editper.handno=handno
            editper.homeno=homeno
            editper.workno=workno
            editper.prefertime=prefertime
            editper.gender=gender
            editper.maritalstatus=maritalstatus

            editper.work_expyears=work_expyears
            editper.work_expmonths=work_expmonths

            editper.salaryrange=salaryrange

            editper.industry=industry

            editper.functional_area=functional_area
            editper.profileurl=profileurl
            editper.save()
            

            detailedit=JSDetails.objects.get(user_id=userid)
            detailedit.update_date=datetime.now()
            
            detailedit.save()
            messages.success(request, 'Your profile updated successfully')
            return HttpResponseRedirect('/accounts/Profile/')
            

        except:
            
            jsdetail=JSDetails(user_id=userid,post_date=datetime.now(),update_date=datetime.now())
            jsdetail.save()

            JS=JSDetails.objects.get(user_id=userid)
            JS_id=JS.id
            
            p = JSPersonal(user_id=userid,JS_id=JS_id,dob=dob,sec_email=sec_email,address1=address1,address2=address2,country=country,state=state,city=city,zipcode=zipcode,handno=handno,homeno=homeno,workno=workno,prefertime=prefertime,gender=gender,maritalstatus=maritalstatus,work_expyears=work_expyears,work_expmonths=work_expmonths,salaryrange=salaryrange,industry=industry,functional_area=functional_area,profileurl=profileurl)
            p.save()

            messages.success(request, 'Your profile updated successfully')
            return HttpResponseRedirect('/accounts/Profile/')
    else:
        details = User.objects.filter(id=request.user.id)
        details1 = JSPersonal.objects.filter(user_id=request.user.id)
        return render_to_response('registration/edit_personal_info.html', {"details":details, "details1":details1}, context_instance=RequestContext(request))


    
@login_required(login_url='/accounts/login/')
def edit_education_info(request):
    if request.method == "POST":
        #return HttpResponse("sdfdfgd")

        user = request.POST.get('user_id')
        js=JSDetails.objects.get(user_id=user)
        JS_id=js.id
        delcer=JSCertificate.objects.filter(user_id=user)
        delcer.delete()
        
        cert_textboxes=request.POST.get('certificatecounter')
        for i in range(int(cert_textboxes)):

            
            cert=request.POST.get('certificate%s' %int(i+1))
            JSCertificate(user_id=user,JS_id=JS_id, certificate=cert).save()

        deledu=JSQualification.objects.filter(user_id=user)
        deledu.delete()

        edu_textboxes=request.POST.get('educationcounter')

        for i in range(int(edu_textboxes)):
            degree=request.POST.get('degree%s' %int(i+1))
            special=request.POST.get('special%s' %int(i+1))
            institution=request.POST.get('institution%s' %int(i+1))
            location=request.POST.get('location%s' %int(i+1))
            year=request.POST.get('year%s' %int(i+1))
            country=request.POST.get('country%s' %int(i+1))
            
            JSQualification(user_id=user,JS_id=JS_id, degree=degree, special=special, institution=institution, location=location, year=year, country=country).save()

        js.update_date=datetime.now()
        js.save()

        messages.success(request, 'Your profile updated successfully')
        return HttpResponseRedirect('/accounts/Profile/')
    else:
        edudetail = JSQualification.objects.filter(user_id=request.user.id)
        cerdetail = JSCertificate.objects.filter(user_id=request.user.id)
        return render_to_response('registration/edit_education_info.html', {"edudetail":edudetail, "cerdetail":cerdetail}, context_instance=RequestContext(request))

@login_required(login_url='/accounts/login/')
def edit_profile_info(request):
    if request.method == "POST":

        user = request.POST.get('user_id')
        
        profile_summary = request.POST.get('profile_summary')
        try:
            edit = JSProfileSummary.objects.get(user_id=user)
            edit.profile_summary=profile_summary
            edit.save()
            edit1=JSDetails.objects.get(user_id=user)
            edit1.update_date=datetime.now()
            edit1.save()
            messages.success(request, 'Your profile updated successfully')
            return HttpResponseRedirect('/accounts/Profile/')
        except:
            jsdetail=JSDetails(user_id=user,post_date=datetime.now(),update_date=datetime.now())
            jsdetail.save()

            JS=JSDetails.objects.get(user_id=user)
            JS_id=JS.id
            
            p = JSProfileSummary(user_id=user,JS_id=JS_id,profile_summary=profile_summary,update_date=datetime.now())
            p.save()
            messages.success(request, 'Your profile updated successfully')
            return HttpResponseRedirect('/accounts/Profile/')
    else:
        details = User.objects.filter(id=request.user.id)
        details1 = JSProfileSummary.objects.filter(user_id=request.user.id)
        return render_to_response('registration/edit_profile_info.html', {"details":details, "details1":details1}, context_instance=RequestContext(request))

@login_required(login_url='/accounts/login/')
def edit_jssecurity(request):
    if request.method == "POST":
        user = request.POST.get('user_id')
        secretclear = request.POST.get('jssecretclear')
        fromdate = request.POST.get('jsfromdate')
        todate = request.POST.get('jstodate')
        if fromdate:
            fromdate=datetime.strptime(fromdate, '%m-%d-%Y')
        if todate:
            todate=datetime.strptime(todate, '%m-%d-%Y')

        #fromdate1=datetime.strptime(str(fromdate),'%m-%d-%Y')
        #todate1=datetime.strptime(str(todate),'%m-%d-%Y')
        #fdate=datetime.strptime(fromdate , '%m-%d-%Y')
        #tdate=datetime.strptime(todate , '%m-%d-%Y')
        try:
            edit = JSsecurity.objects.get(user_id=user)
            if fromdate and todate:
                edit.jssecretclear=secretclear
                edit.jsfromdate=fromdate
                edit.jstodate=todate
                
            elif fromdate:
                edit.jssecretclear=secretclear
                edit.jsfromdate=fromdate
                edit.jstodate=todate
            elif todate:
                edit.jssecretclear=secretclear
                edit.jsfromdate=fromdate
                edit.jstodate=todate
            else:
                edit.jssecretclear=secretclear
                edit.jstodate="00-00-0000"
                edit.jsfromdate="00-00-0000"
            edit.save()

            edit1=JSDetails.objects.get(user_id=user)
            edit1.update_date=datetime.now()
            edit1.save()
            messages.success(request, 'Your profile updated successfully')
            return HttpResponseRedirect('/accounts/Profile/')

        except:
            jsdetail=JSDetails(user_id=user,post_date=datetime.now(),update_date=datetime.now())
            jsdetail.save()

            JS=JSDetails.objects.get(user_id=user)
            JS_id=JS.id
            
            p = JSsecurity(user_id=user,JS_id=JS_id,jssecretclear=jssecretclear,jsfromdate=jsfromdate,jstodate=jstodate)
            p.save()
            messages.success(request, 'Your profile updated successfully')
            return HttpResponseRedirect('/accounts/Profile/')
    else:
        details = User.objects.filter(id=request.user.id)
        details1 = JSsecurity.objects.filter(user_id=request.user.id)
        return render_to_response('registration/edit_jssecurity_info.html', {"details":details, "details1":details1}, context_instance=RequestContext(request))



@login_required(login_url='/accounts/login/')
def edit_employment_info(request):
    if request.method == "POST":

        dele=JSEmployerDetails.objects.filter(user_id=request.user.id)
        dele.delete()
        js=JSDetails.objects.get(user_id=request.user.id)
        JS_id=js.id

        emp_textboxes=request.POST.get('empcounter')

        for i in range(int(emp_textboxes)):

            employer_name=request.POST.get('employer_name%s' %int(i+1))
            empstatus=request.POST.get('empstatus%s' %int(i+1))
            empstartdate=request.POST.get('empstartdate%s' %int(i+1))
            emptodate=request.POST.get('emptodate%s' %int(i+1))
            designation=request.POST.get('designation%s' %int(i+1))
            jobprofile=request.POST.get('jobprofile%s' %int(i+1))

            JSEmployerDetails(user_id=request.user.id,JS_id=JS_id,employer_name=employer_name,empstatus=empstatus,empstartdate=empstartdate,emptodate=emptodate,designation=designation,jobprofile=jobprofile).save()


        js.update_date=datetime.now()
        js.save()
        messages.success(request, 'Your profile updated successfully')
        return HttpResponseRedirect('/accounts/Profile/')
    else:
        details = User.objects.filter(id=request.user.id)
        details1 = JSEmployerDetails.objects.filter(user_id=request.user.id)
        return render_to_response('registration/edit_employment_info.html', {"details":details, "details1":details1}, context_instance=RequestContext(request))


@login_required(login_url='/accounts/login/')
def edit_project_info(request):
    if request.method == "POST":

        user = request.POST.get('user_id')
        delproj=JSProjectDetails.objects.filter(user_id=user)
        delproj.delete()

        js=JSDetails.objects.get(user_id=user)
        JS_id=js.id

        proj_textboxes=request.POST.get('projcounter')

        for i in range(int(proj_textboxes)):
            
            client=request.POST.get('client%s' %int(i+1))
            project_title=request.POST.get('project_title%s' %int(i+1))
            projstartdate=request.POST.get('projstartdate%s' %int(i+1))
            projtodate=request.POST.get('projtodate%s' %int(i+1))
            project_loc=request.POST.get('project_loc%s' %int(i+1))
            on_offsite=request.POST.get('on_offsite%s' %int(i+1))
            emp_type=request.POST.get('emp_type%s' %int(i+1))
            project_details=request.POST.get('project_details%s' %int(i+1))
            role_desc=request.POST.get('role_desc%s' %int(i+1))
            skill_used=request.POST.get('skill_used%s' %int(i+1))
            role=request.POST.get('role%s' %int(i+1))
            teamsize=request.POST.get('teamsize%s' %int(i+1))
            JSProjectDetails(user_id=user,JS_id=JS_id,client=client,project_title=project_title,projstartdate=projstartdate,projtodate=projtodate,project_loc=project_loc,on_offsite=on_offsite,emp_type=emp_type,project_details=project_details,role_desc=role_desc,skill_used=skill_used,role=role,teamsize=teamsize).save()

        js.update_date=datetime.now()
        js.save()

        messages.success(request, 'Your profile updated successfully')
        return HttpResponseRedirect('/accounts/Profile/')
    else:
        details = User.objects.filter(id=request.user.id)
        details1 = JSProjectDetails.objects.filter(user_id=request.user.id)
        return render_to_response('registration/edit_project_info.html', {"details":details, "details1":details1}, context_instance=RequestContext(request))

@login_required(login_url='/accounts/login/')
def edit_other_info(request):
    if request.method == "POST":
        user = request.POST.get('user_id')        
        emptype = request.POST.get('emptype')
        workpermit = request.POST.get('workpermit')
        datas_qual=''
        for i in request.POST.getlist('workother'):
            datas_qual+=i+', '
        workother=datas_qual[:-2]
        relocate = request.POST.get('relocate')
        telecommunicate = request.POST.get('telecommunicate')
        travel = request.POST.get('travel')
        choice=''
        for i in request.POST.getlist('relocatechoice'):
            choice+=i+', '
        relocatechoice=choice[:-2]
        
        #return HttpResponse(relocate)

        if relocate == "None" and telecommunicate == "None":
            edit1=JSDetailOther.objects.get(user_id=user)
            edit1.relocate="No"
            edit1.telecommunicate="No"
            edit1.travel=travel
            edit1.relocatechoice=relocatechoice
            edit1.emptype=emptype
            edit1.workpermit=workpermit
            edit1.workother=workother
            edit1.save()

        elif telecommunicate == "None":
            edit1=JSDetailOther.objects.get(user_id=user)
            edit1.relocate=relocate
            edit1.telecommunicate="No"
            edit1.travel=travel
            edit1.relocatechoice=relocatechoice
            edit1.emptype=emptype
            edit1.workpermit=workpermit
            edit1.workother=workother
            edit1.save()

        elif relocate == "None":
            edit1=JSDetailOther.objects.get(user_id=user)
            edit1.relocate="No"
            edit1.telecommunicate=telecommunicate
            edit1.travel=travel
            edit1.relocatechoice=relocatechoice
            edit1.emptype=emptype
            edit1.workpermit=workpermit
            edit1.workother=workother
            edit1.save()
        else:
            edit1=JSDetailOther.objects.get(user_id=user)
            edit1.relocate=relocate
            edit1.telecommunicate=telecommunicate
            edit1.travel=travel
            edit1.relocatechoice=relocatechoice
            edit1.emptype=emptype
            edit1.workpermit=workpermit
            edit1.workother=workother
            edit1.save()

        

        dellang=JSLanguage.objects.filter(user_id=user)
        dellang.delete()

        js=JSDetails.objects.get(user_id=user)
        JS_id=js.id

        lang_textboxes=request.POST.get('langcounter')

        for i in range(int(lang_textboxes)):
            language = request.POST.get('language%s' %int(i+1))
            proficiency = request.POST.get('proficiency%s' %int(i+1))
            read = request.POST.get('read%s' %int(i+1))
            write = request.POST.get('write%s' %int(i+1))
            speak = request.POST.get('speak%s' %int(i+1))

            language=JSLanguage(user_id=user,JS_id=JS_id,language=language,proficiency=proficiency,read=read,write=write,speak=speak).save()

        js.update_date=datetime.now()
        js.save()

        messages.success(request, 'Your profile updated successfully')
        return HttpResponseRedirect('/accounts/Profile/')

        
    else:
        language = JSLanguage.objects.filter(user_id=request.user.id)
        other = JSDetailOther.objects.filter(user_id=request.user.id)
        return render_to_response('registration/edit_other_info.html', {"language":language, "other":other}, context_instance=RequestContext(request))

@login_required(login_url='/accounts/login/')
def edit_resume_info(request):
    if request.method == "POST":

        user = request.POST.get('user_id')
        textTitle = request.POST.get('textResumeTitle')
        textFile = request.POST.get('textResumeFile')

        editTextResume=JSTextResume.objects.get(user_id=user)
        editTextResume.resumeTitle=textTitle
        editTextResume.resumeFile=textFile
        editTextResume.save()
        try:

            videoresume = request.FILES.get('videoresume')

            if videoresume:
                editvideores = JSVideoResume.objects.get(user_id=user)
                editvideores.videoresume = videoresume
                editvideores.save()

            for i in range(1,6):
                jsresid= request.POST.get('jsResumeID'+str(i),'')
                if not jsresid:break
                resid=JSResume.objects.get(user_id=user,pk=int(jsresid))
                resid.resumeTitle=request.POST.get('jsResumeTitle'+str(i))
                if request.FILES.get('jsResumeFile'+str(i)):
                    resid.resumeFile=request.FILES.get('jsResumeFile'+str(i))
                resid.save()
            messages.success(request, 'Your profile updated successfully')
            return HttpResponseRedirect('/accounts/Profile/')

        except:
           
            for i in range(1,6):
                jsresid= request.POST.get('jsResumeID'+str(i),'')
                if not jsresid:break
                resid=JSResume.objects.get(user_id=user,pk=int(jsresid))
                resid.resumeTitle=request.POST.get('jsResumeTitle'+str(i))
                if request.FILES.get('jsResumeFile'+str(i)):
                    resid.resumeFile=request.FILES.get('jsResumeFile'+str(i))
                resid.save()
            messages.success(request, 'Your profile updated successfully')
            return HttpResponseRedirect('/accounts/Profile/')

            
    else:
        details = User.objects.filter(id=request.user.id)
        rescount = JSResume.objects.filter(user_id=request.user.id).count()
        details1 = JSResume.objects.filter(user_id=request.user.id)
        details2 = JSTextResume.objects.filter(user_id=request.user.id)
        videoresume = JSVideoResume.objects.filter(user_id=request.user.id)

        return render_to_response('registration/edit_resume_info.html', {"rescount":rescount,"details":details,"details1":details1,"details2":details2,"videoresume":videoresume}, context_instance=RequestContext(request))


@login_required(login_url='/accounts/login/')
def edit_profilepic_info(request):
    if request.method == "POST":
        userid = request.POST.get('user_id')
        profile_pics= request.FILES.get('profile_pic')
        try:
            edit = JSProfileSummary.objects.get(user_id=request.user.id)
            if edit.profile_pic:
                picture=edit.profile_pic
                os.remove(settings.CURRENT_DIR+"/media/"+str(picture))
                edit.profile_pic=profile_pics
                edit.save()
                edit1 = JSDetails.objects.get(user_id=userid)
                edit1.update_date=datetime.now()
                edit1.save()
            else:
                edit.profile_pic=profile_pics
                edit.save()
                edit1 = JSDetails.objects.get(user_id=userid)
                edit1.update_date=datetime.now()
                edit1.save()
            messages.success(request, 'Your profile updated successfully')
            return HttpResponseRedirect('/accounts/Profile/')
        except:
            if profile_pics:
                p = JSProfileSummary(user_id=userid,profile_pic=profile_pics)
                p.save()
                d = JSDetails(user_id=userid,visiblity=True,post_date=datetime.now(),update_date=datetime.now())
            messages.success(request, 'Your profile updated successfully')
            return HttpResponseRedirect('/accounts/Profile/')
    else:
        details = User.objects.filter(id=request.user.id)
        details1 = JSProfileSummary.objects.filter(user_id=request.user.id)
        return render(request,'registration/js_profilepic_update.html', {"details":details, "details1":details1})

@login_required(login_url='/accounts/login/')
def edit_itskills_info(request):
    if request.method == "POST":
        user=request.user.id
        delskill=JSSkills.objects.filter(user_id=user)
        delskill.delete()
        js=JSDetails.objects.get(user_id=user)
        JS_id=js.id
        skill_textboxes=request.POST.get('skillcounter')
        for i in range(int(skill_textboxes)):
            skill=request.POST.get('skill%s' %int(i+1))
            version=request.POST.get('version%s' %int(i+1))
            lastused=request.POST.get('lastused%s' %int(i+1))
            skillyear=request.POST.get('skillyear%s' %int(i+1))
            skillmon=request.POST.get('skillmon%s' %int(i+1))
                    
            JSSkills(user_id=user,JS_id=JS_id, skill=skill, version=version, lastused=lastused, skillyear=skillyear, skillmon=skillmon).save()

        js.update_date=datetime.now()
        js.save()
        messages.success(request, 'Your profile updated successfully')
        return HttpResponseRedirect('/accounts/Profile/')
    else:
        details = User.objects.filter(id=request.user.id)
        details1 = JSSkills.objects.filter(user_id=request.user.id)
        return render_to_response('registration/edit_itskills_info.html', {"details":details, "details1":details1}, context_instance=RequestContext(request))

        


@login_required(login_url='/accounts/login/')
def logout_page(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return HttpResponseRedirect('/accounts/login/')
@login_required(login_url='/accounts/EmpReg/')
def emplogout_page(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return HttpResponseRedirect('/accounts/EmpReg/')

@login_required(login_url='/accounts/login/')
def newpost(request):

    if request.method == "POST":
            user_id = request.POST.get('user_id')

            fname= request.POST.get('fname')
            lastname= request.POST.get('lastname')
            dob = request.POST.get('dob')
            sec_email = request.POST.get('sec_email')
            address1 = request.POST.get('address1')
            address2 = request.POST.get('address2')
            country = request.POST.get('country')
            state = request.POST.get('state')
            city = request.POST.get('city')
            zipcode = request.POST.get('zipcode')
            ltn=request.POST.get('latitude')
            lng=request.POST.get('longitude')
            typ=request.POST.get('type')
            handno= request.POST.get('handno')
            homeno= request.POST.get('homeno')
            workno= request.POST.get('workno')
            prefertime=request.POST.get('prefertime')
            gender = request.POST.get('gender')
            profileurl = request.POST.get('profileurl')
            maritalstatus = request.POST.get('maritalstatus')

            work_expyears= request.POST.get('work_expyears')
            work_expmonths= request.POST.get('work_expmonths')
            salaryrange= request.POST.get('salary')
            industry= request.POST.get('industry')
            functional_area= request.POST.get('functional_area')
            profileurl=request.POST.get('profileurl')
        
            

            profile_summary = request.POST.get('profile_summary')
            profile_pic = request.FILES.get('profile_pic')

           
            jssecretclear = request.POST.get('jssecretclear')
            fdate = request.POST.get('jsfromdate')
            tdate = request.POST.get('jstodate')

            if fdate:
                fdate=datetime.strptime(fdate, '%m-%d-%Y')
            if tdate:
                tdate=datetime.strptime(tdate, '%m-%d-%Y')
            
            emptype = request.POST.get('job_type')
            workpermit = request.POST.get('workpermit')
            datas_qual=''
            for i in request.POST.getlist('workother'):
                datas_qual+=i+', '
            workother=datas_qual[:-2]
            
            resumeTitle = request.POST.get('resumeTitle')
            resumeFile= request.FILES.get('resumeFile')
            text_resume = request.POST.get('text_resume')
            videoresume = request.FILES.get('videoresume')

            relocate = request.POST.get('relocate')
            telecommunicate = request.POST.get('telecommute')
            travel = request.POST.get('travel')
            relocatechoice=','.join(request.POST.getlist('relocatechoice'))
            #    rechoice+=i+', '
            #=rechoice[:-2]

            edit1 = User.objects.get(id=user_id)
            edit1.first_name =fname
            edit1.last_name = lastname
            edit1.save()

            jsdetail=JSDetails(user_id=user_id,post_date=datetime.now(),update_date=datetime.now())
            jsdetail.save()

            JS=JSDetails.objects.get(user_id=user_id)
            JS_id=JS.id

            cert_textboxes=request.POST.get('certificatecounter')
            #print request.POST.items()
            #if 'certificatecounter' in request.POST:
            for i in range(int(cert_textboxes)):

                
                cert=request.POST.get('certificate%s' %int(i+1))
                JSCertificate(user_id=user_id,JS_id=JS_id, certificate=cert).save()
            #else:JSCertificate(user_id=user_id,JS_id=JS_id, certificate=request.POST['certificate1']).save()


            edu_textboxes=request.POST.get('educationcounter')

            #print request.POST.items()
            for i in range(int(edu_textboxes)):
                degree=request.POST.get('degree%s' %int(i+1))
                special=request.POST.get('special%s' %int(i+1))
                institution=request.POST.get('institution%s' %int(i+1))
                location=request.POST.get('location%s' %int(i+1))
                year=request.POST.get('year%s' %int(i+1))
                country=request.POST.get('country%s' %int(i+1))
                
                JSQualification(user_id=user_id,JS_id=JS_id, degree=degree, special=special, institution=institution, location=location, year=year, country=country).save()

            skill_textboxes=request.POST.get('skillcounter')

            for i in range(int(skill_textboxes)):
                skill=request.POST.get('skill%s' %int(i+1))
                version=request.POST.get('version%s' %int(i+1))
                lastused=request.POST.get('lastused%s' %int(i+1))
                skillyear=request.POST.get('skillyear%s' %int(i+1))
                skillmon=request.POST.get('skillmon%s' %int(i+1))
                                
                JSSkills(user_id=user_id,JS_id=JS_id, skill=skill, version=version, lastused=lastused, skillyear=skillyear, skillmon=skillmon).save()

            emp_textboxes=request.POST.get('empcounter')

            for i in range(int(emp_textboxes)):
                employer_name=request.POST.get('employer_name%s' %int(i+1))
                empstatus=request.POST.get('empstatus%s' %int(i+1))
                empstartdate=request.POST.get('empstartdate%s' %int(i+1))
                emptodate=request.POST.get('emptodate%s' %int(i+1))
                designation=request.POST.get('designation%s' %int(i+1))
                jobprofile=request.POST.get('jobprofile%s' %int(i+1))

                JSEmployerDetails(user_id=user_id,JS_id=JS_id,employer_name=employer_name,empstatus=empstatus,empstartdate=empstartdate,emptodate=emptodate,designation=designation,jobprofile=jobprofile).save()


            proj_textboxes=request.POST.get('projcounter')

            for i in range(int(proj_textboxes)):
                
                client=request.POST.get('client%s' %int(i+1))
                project_title=request.POST.get('project_title%s' %int(i+1))
                projstartdate=request.POST.get('projstartdate%s' %int(i+1))
                projtodate=request.POST.get('projtodate%s' %int(i+1))
                project_loc=request.POST.get('project_loc%s' %int(i+1))
                on_offsite=request.POST.get('on_offsite%s' %int(i+1))
                emp_type=request.POST.get('emp_type%s' %int(i+1))
                project_details=request.POST.get('project_details%s' %int(i+1))
                role_desc=request.POST.get('role_desc%s' %int(i+1))
                skill_used=request.POST.get('skill_used%s' %int(i+1))
                role=request.POST.get('role%s' %int(i+1))
                teamsize=request.POST.get('teamsize%s' %int(i+1))

                JSProjectDetails(user_id=user_id,JS_id=JS_id,client=client,project_title=project_title,projstartdate=projstartdate,projtodate=projtodate,project_loc=project_loc,on_offsite=on_offsite,emp_type=emp_type,project_details=project_details,role_desc=role_desc,skill_used=skill_used,role=role,teamsize=teamsize).save()




            videoresume=JSVideoResume(user_id=user_id,JS_id=JS_id,videoresume=videoresume,resumeDate=datetime.now())
            videoresume.save()

            personal=JSPersonal(user_id=user_id,JS_id=JS_id,dob=dob,sec_email=sec_email,address1=address1,address2=address2,country=country,state=state,city=city,zipcode=zipcode,lat=ltn,lng=lng,typ=typ,handno=handno,workno=workno,homeno=homeno,prefertime=prefertime,gender=gender,maritalstatus=maritalstatus,work_expyears=work_expyears,work_expmonths=work_expmonths,salaryrange=salaryrange,industry=industry,functional_area=functional_area,profileurl=profileurl)
            personal.save()

            profile=JSProfileSummary(user_id=user_id,JS_id=JS_id,profile_summary=profile_summary,profile_pic=profile_pic)
            profile.save()

       
            lang_textboxes=request.POST.get('langcounter')

            for i in range(int(lang_textboxes)):
                language = request.POST.get('language%s' %int(i+1))
                proficiency = request.POST.get('proficiency%s' %int(i+1))
                read = request.POST.get('read%s' %int(i+1))
                write = request.POST.get('write%s' %int(i+1))
                speak = request.POST.get('speak%s' %int(i+1))

                language=JSLanguage(user_id=user_id,JS_id=JS_id,language=language,proficiency=proficiency,read=read,write=write,speak=speak).save()

            if relocate==None and telecommunicate==None:
                otherDetails=JSDetailOther(user_id=user_id,JS_id=JS_id,emptype=emptype,workpermit=workpermit,workother=workother,relocate="No",telecommunicate="No",travel=travel,relocatechoice=relocatechoice)
                otherDetails.save()
            elif relocate==None:
                otherDetails=JSDetailOther(user_id=user_id,JS_id=JS_id,emptype=emptype,workpermit=workpermit,workother=workother,relocate="No",telecommunicate=telecommunicate,travel=travel,relocatechoice=relocatechoice)
                otherDetails.save()

            elif telecommunicate==None:
                otherDetails=JSDetailOther(user_id=user_id,JS_id=JS_id,emptype=emptype,workpermit=workpermit,workother=workother,relocate=relocate,telecommunicate="No",travel=travel,relocatechoice=relocatechoice)
                otherDetails.save()
            else:
                otherDetails=JSDetailOther(user_id=user_id,JS_id=JS_id,emptype=emptype,workpermit=workpermit,workother=workother,relocate=relocate,telecommunicate=telecommunicate,travel=travel,relocatechoice=relocatechoice)
                otherDetails.save()

            #for t in relocatechoice.split(','): extra.tags.add(t)
            #extra.save_m2m()

            if fdate and tdate:
                jssecurity=JSsecurity(user_id=user_id,JS_id=JS_id,jssecretclear=jssecretclear,jsfromdate=fdate,jstodate=tdate)
                jssecurity.save()
            elif fdate:
                jssecurity=JSsecurity(user_id=user_id,JS_id=JS_id,jssecretclear=jssecretclear,jsfromdate=fdate)
                jssecurity.save()
            elif tdate:
                jssecurity=JSsecurity(user_id=user_id,JS_id=JS_id,jssecretclear=jssecretclear,jstodate=tdate)
                jssecurity.save()
            else:
                jssecurity=JSsecurity(user_id=user_id,JS_id=JS_id,jssecretclear=jssecretclear)
                jssecurity.save()

            if text_resume:
                text=JSTextResume(user_id=user_id,JS_id=JS_id,resumeTitle=resumeTitle,resumeFile=text_resume,activetext_resume=True)
                text.save()
                resume=JSResume(user_id=user_id,JS_id=JS_id)
                resume.save()

                res=JSTextResume.objects.get(user_id=user_id)
                Resumeid=res.id
                activateresume=JSResumeActive(user_id=user_id,JS_id=JS_id,resumeActive_id=Resumeid)
                activateresume.save()

            else:
                resume=JSResume(user_id=user_id,JS_id=JS_id,resumeTitle=resumeTitle,resumeFile=resumeFile)
                resume.save()
                text=JSTextResume(user_id=user_id,JS_id=JS_id,activetext_resume=False)
                text.save()
                rescount=JSResume.objects.filter(user_id=user_id).count()
                if rescount is 1:
                    res=JSResume.objects.get(user_id=user_id)
                    Resumeid=res.id
                    resumefile=res.resumeFile
                    call(["unoconv","-f","html","-o",settings.CURRENT_DIR+"/tagging/templates/documents/",settings.CURRENT_DIR+"/media/"+str(resumefile)])


                    activateresume=JSResumeActive(user_id=user_id,JS_id=JS_id,resumeActive_id=Resumeid)
                    activateresume.save()
                    
            messages.success(request, 'Your profile updated successfully')
            return HttpResponseRedirect('/accounts/Profile/')
    else:
        return render_to_response('registration/personal_information.html',context_instance=RequestContext(request))

'''
def js_reg_complete(request):
    return render_to_response('registration/registration_complete.html',context_instance=RequestContext(request))
'''

def JSRegComplete(request):
    return render_to_response('registration/registration_complete.html',context_instance=RequestContext(request))


def empreg_complete(request):
    return render_to_response('registration/empregistration_complete.html',context_instance=RequestContext(request))

def emp_activate(request):
    return render_to_response('registration/empactivate.html',context_instance=RequestContext(request))

def emp_activation(request, activation_key):

    activation_key = activation_key 
    emp=EmployerReg_Form.objects.get(activation_key=activation_key)
    emp.is_active=1
    emp.save()
    return HttpResponseRedirect('/accounts/Home/')

def emp_login(request):
    msg=""
    if request.method=='POST':

        un=request.POST.get('username')
        pw=request.POST.get('password')
        ut=request.POST.get('usertype')

        user =authenticate(username=un, password=pw)
        if user is not None:
    # the password verified for the user
            if user.is_active:
                if user.usertype == ut:
                    login(request, user)
                    messages.success(request, 'Logged in successfully')
                    return HttpResponseRedirect('/accounts/RecruiterDashboard/')
                else:
                    messages.error(request, 'Enter valid username and password')
                    return HttpResponseRedirect('/accounts/EmpReg/')
            else:
                messages.error(request, 'Please Activate your Account')
                return HttpResponseRedirect('/accounts/EmpReg/')
        else:
            messages.error(request, 'Enter valid username and password')
            return HttpResponseRedirect('/accounts/EmpReg/')
 
#------------ 1st JUNE ---------------------------------

@login_required(login_url='/accounts/EmpReg/')   
def jobpost(request):
    msg=""
    if request.method=='POST':
        emp_id=request.POST.get('user_id')
        title=request.POST.get('title')
        referencecode=request.POST.get('ref_code')
        jobsummary=request.POST.get('jobsummary')
        jobdetails=request.POST.get('jobdetails')
        min_exp=request.POST.get('min_exp')
        max_exp=request.POST.get('max_exp')
        address1=request.POST.get('address1')
        address2=request.POST.get('address2')
        city=request.POST.get('city')
        state=request.POST.get('state')
        country=request.POST.get('country')
        zipcode=request.POST.get('zipcode')
        ltn=request.POST.get('latitude')
        lng=request.POST.get('longitude')
        typ=request.POST.get('type')
        industry = request.POST.get('industry')
        functionalarea=request.POST.get('functionalarea')
        ownername=request.POST.get('ownername')
        workno=request.POST.get('workno')
        handno=request.POST.get('handno')
        fax=request.POST.get('fax')
        email=request.POST.get('email')
        companyprofile=request.POST.get('companyprofile')
        marklive=request.POST.get('marklive')
        todate=request.POST.get('todate')
        jobtype=request.POST.get('jobtype')
        salary_range=request.POST.get('salary_range')
        empsecretclear=request.POST.get('empsecretclear')
        emptravel = request.POST.get('emptravel')
        emptele = request.POST.get('emptele')
        workpermit = request.POST.get('workpermit')
        datas_qual=''
        for i in request.POST.getlist('qualification'):
            datas_qual+=i+', '
        qualification=datas_qual[:-2]
        if emptele:
            s=jobs(emp_id=emp_id,title=title,referencecode=referencecode,jobsummary=jobsummary,jobdetails=jobdetails,min_exp=min_exp,max_exp=max_exp,address1=address1,address2=address2,city=city,state=state,country=country,zipcode=zipcode,lat=ltn,lng=lng,typ=typ,industry=industry,functionalarea=functionalarea,ownername=ownername,workno=workno,handno=handno,fax=fax,email=email,marklive=marklive,todate=todate,jobtype=jobtype,salary_range=salary_range,qualification=qualification,empsecretclear=empsecretclear,emptravel=emptravel,emptele=True,workpermit=workpermit)
            a=EmployerReg_Form.objects.get(user_id=emp_id)
            a.companyprofile=companyprofile
            a.save()
        else:
            s=jobs(emp_id=emp_id,title=title,referencecode=referencecode,jobsummary=jobsummary,jobdetails=jobdetails,min_exp=min_exp,max_exp=max_exp,address1=address1,address2=address2,city=city,state=state,country=country,zipcode=zipcode,lat=ltn,lng=lng,typ=typ,industry=industry,functionalarea=functionalarea,ownername=ownername,workno=workno,handno=handno,fax=fax,email=email,marklive=marklive,todate=todate,jobtype=jobtype,salary_range=salary_range,qualification=qualification,empsecretclear=empsecretclear,emptravel=emptravel,emptele=False,workpermit=workpermit)
            a=EmployerReg_Form.objects.get(user_id=emp_id)
            a.companyprofile=companyprofile
            a.save()
        s.save()
        jobid=s.id
        for skills in [i.strip() for i in request.POST.get('key_skills').split(',')]:
            ks=employerkeyskills(emp_id=emp_id,job_id=jobid,keyskills=skills)
            ks.save()
        messages.success(request, 'Job has been posted successfully')
        return HttpResponseRedirect('/accounts/JobsEmp/')
    else:
        if urlparse(request.user.employerreg_form.companyurl).hostname.split('.')[1] =='msquaresystems':
            remaining=1
            cmpdetails=EmployerReg_Form.objects.filter(user_id=request.user.id)
            return render(request,'registration/Post_Job.html', {'remaining':remaining,'cmpdetails':cmpdetails})

        else:

            job = jobs.objects.filter(emp_id=request.user.id).count()
            remaining = 5-job
            cmpdetails=EmployerReg_Form.objects.filter(user_id=request.user.id)
            if remaining is 0:
                msg = "NOTE : Your not allow to post job. Already you had post 5 jobs."
                return render(request,'registration/Post_Job.html', {'msg': msg,'remaining':remaining,'cmpdetails':cmpdetails})
            else:
                msg = "NOTE : You Have Only %s Job Post Remaining"% remaining
                return render(request,'registration/Post_Job.html', {'msg': msg,'remaining':remaining,'cmpdetails':cmpdetails})


@login_required(login_url='/accounts/EmpReg/')   
def repost(request,job_id):
    '''
    jobid=job_id
    description=jobs.objects.filter(id=jobid)
    '''
    msg=""
    if request.method=='POST':
        emp_id=request.POST.get('user_id')
        title=request.POST.get('title')
        referencecode=request.POST.get('ref_code')
        jobsummary=request.POST.get('jobsummary')
        jobdetails=request.POST.get('jobdetails')
        min_exp=request.POST.get('min_exp')
        max_exp=request.POST.get('max_exp')
        address1=request.POST.get('address1')
        address2=request.POST.get('address2')
        city=request.POST.get('city')
        state=request.POST.get('state')
        country=request.POST.get('country')
        zipcode=request.POST.get('zipcode')
        ltn=request.POST.get('latitude')
        lng=request.POST.get('longitude')
        typ=request.POST.get('type')
        industry = request.POST.get('industry')
        functionalarea=request.POST.get('functionalarea')
        ownername=request.POST.get('ownername')
        workno=request.POST.get('workno')
        handno=request.POST.get('handno')
        fax=request.POST.get('fax')
        email=request.POST.get('email')
        companyprofile=request.POST.get('companyprofile')
        marklive=request.POST.get('marklive')
        todate=request.POST.get('todate')
        jobtype=request.POST.get('jobtype')
        salary_range=request.POST.get('salary_range')
        empsecretclear=request.POST.get('empsecretclear')
        emptravel = request.POST.get('emptravel')
        emptele = request.POST.get('emptele')
        workpermit = request.POST.get('workpermit')
        datas_qual=''
        for i in request.POST.getlist('qualification'):
            datas_qual+=i+', '
        qualification=datas_qual[:-2]
        if emptele:
            s=jobs(emp_id=emp_id,title=title,referencecode=referencecode,jobsummary=jobsummary,jobdetails=jobdetails,min_exp=min_exp,max_exp=max_exp,address1=address1,address2=address2,city=city,state=state,country=country,zipcode=zipcode,lat=ltn,lng=lng,typ=typ,industry=industry,functionalarea=functionalarea,ownername=ownername,workno=workno,handno=handno,fax=fax,email=email,marklive=marklive,todate=todate,jobtype=jobtype,salary_range=salary_range,qualification=qualification,empsecretclear=empsecretclear,emptravel=emptravel,emptele=True,workpermit=workpermit)
            a=EmployerReg_Form.objects.get(user_id=emp_id)
            a.companyprofile=companyprofile
            a.save()
        else:
            s=jobs(emp_id=emp_id,title=title,referencecode=referencecode,jobsummary=jobsummary,jobdetails=jobdetails,min_exp=min_exp,max_exp=max_exp,address1=address1,address2=address2,city=city,state=state,country=country,zipcode=zipcode,lat=ltn,lng=lng,typ=typ,industry=industry,functionalarea=functionalarea,ownername=ownername,workno=workno,handno=handno,fax=fax,email=email,marklive=marklive,todate=todate,jobtype=jobtype,salary_range=salary_range,qualification=qualification,empsecretclear=empsecretclear,emptravel=emptravel,emptele=False,workpermit=workpermit)
            a=EmployerReg_Form.objects.get(user_id=emp_id)
            a.companyprofile=companyprofile
            a.save()
        s.save()
        jobid=s.id
        for skills in [i.strip() for i in request.POST.get('key_skills').split(',')]:
            ks=employerkeyskills(emp_id=emp_id,job_id=jobid,keyskills=skills)
            ks.save()
        messages.success(request, '1 job reposted successfully')
        return HttpResponseRedirect('/accounts/JobsEmp/')
    else:
        jobid=job_id
        description=jobs.objects.filter(id=jobid)
        keyskills=employerkeyskills.objects.filter(job_id=jobid)
        cmpdetails=EmployerReg_Form.objects.filter(user_id=request.user.id)
        job = jobs.objects.filter(emp_id=request.user.id).count()
        if urlparse(request.user.employerreg_form.companyurl).hostname.split('.')[1] =='msquaresystems':
            remaining=1
        else:
            remaining = 5-job
        if remaining is 0:
            if urlparse(request.user.employerreg_form.companyurl).hostname.split('.')[1] =='msquaresystems':
                return render_to_response('registration/RePost_Job.html', {'remaining':remaining,'description':description,'keyskills':keyskills,'cmpdetails':cmpdetails}, context_instance=RequestContext(request))
            else:
                msg = "NOTE : Your not allow to Post Job.Already You Post 5 jobs."
                return render_to_response('registration/RePost_Job.html', {'msg': msg,'remaining':remaining,'description':description,'keyskills':keyskills,'cmpdetails':cmpdetails}, context_instance=RequestContext(request))
        else:
            if urlparse(request.user.employerreg_form.companyurl).hostname.split('.')[1] =='msquaresystems':
                return render_to_response('registration/RePost_Job.html', {'remaining':remaining,'description':description,'keyskills':keyskills,'cmpdetails':cmpdetails}, context_instance=RequestContext(request))
            else:
                msg = "NOTE : You Have Only %s Job Post Remaining"% remaining
                return render_to_response('registration/RePost_Job.html', {'msg': msg,'remaining':remaining,'description':description,'keyskills':keyskills,'cmpdetails':cmpdetails}, context_instance=RequestContext(request))



@login_required(login_url='/accounts/EmpReg/')   
def edit_jobpost(request,job_id):
    if request.method == "POST":
        jobid=request.POST.get('id')
        empid=request.POST.get('empid')
        title=request.POST.get('title')
        referencecode=request.POST.get('ref_code')
        jobsummary=request.POST.get('jobsummary')
        jobdetails=request.POST.get('jobdetails')
        keyskills=request.POST.get('key_skills').split(',')
        min_exp=request.POST.get('min_exp')
        max_exp=request.POST.get('max_exp')
        address1=request.POST.get('address1')
        address2=request.POST.get('address2')
        city=request.POST.get('city')
        state=request.POST.get('state')
        country=request.POST.get('country')
        zipcode=request.POST.get('zipcode')
        ltn=request.POST.get('latitude')
        lng=request.POST.get('longitude')
        typ=request.POST.get('type')
        industry = request.POST.get('industry')
        functionalarea=request.POST.get('functionalarea')
        ownername=request.POST.get('ownername')
        workno=request.POST.get('workno')
        handno=request.POST.get('handno')
        fax=request.POST.get('fax')
        email=request.POST.get('email')

        companyprofile=request.POST.get('companyprofile')
        marklive=request.POST.get('marklive')
        todate=request.POST.get('todate')
        if marklive:
            marklive=datetime.strptime(marklive , '%m-%d-%Y')
        if todate:
            todate=datetime.strptime(todate , '%m-%d-%Y')
        jobtype=request.POST.get('jobtype')
        salary_range=request.POST.get('salary_range')
        empsecretclear=request.POST.get('empsecretclear')
        emptravel = request.POST.get('emptravel')
        emptele = request.POST.get('emptele')
        workpermit = request.POST.get('workpermit')

        datas_qual=''
        for i in request.POST.getlist('qualification'):
            datas_qual+=i+', '
        qualification=datas_qual[:-2]
        
        edit = jobs.objects.get(id=jobid)

        edit.title=title
        edit.referencecode=referencecode
        edit.jobsummary=jobsummary
        edit.jobdetails=jobdetails
        edit.min_exp=min_exp
        edit.max_exp=max_exp
        edit.address1=address1
        edit.address2=address2
        edit.city=city
        edit.state=state
        edit.country=country
        edit.zipcode=zipcode
        edit.lat=ltn
        edit.lng=lng
        edit.typ=typ
        edit.industry=industry
        edit.functionalarea=functionalarea
        edit.ownername=ownername
        edit.workno=workno
        edit.handno=handno
        edit.fax=fax
        edit.email=email
        edit.marklive=marklive
        edit.todate=todate
        edit.jobtype=jobtype
        edit.salary_range=salary_range
        edit.qualification=qualification
        edit.empsecretclear=empsecretclear
        edit.emptravel=emptravel
        edit.workpermit=workpermit
        if emptele:
            edit.emptele=True
        else:
            edit.emptele=False
        edit.save()

        a=EmployerReg_Form.objects.get(user_id=empid)
        a.companyprofile=companyprofile
        a.save()

        delskill=employerkeyskills.objects.filter(job_id=jobid)
        delskill.delete()

        for skills in [i.strip() for i in keyskills]:
            ks=employerkeyskills(emp_id=empid,job_id=jobid,keyskills=skills)
            ks.save()

        messages.success(request, '1 job edited successfully')
        return HttpResponseRedirect('/accounts/JobsEmp/')
        
    else:
        jobid=job_id
        cmpdetails=EmployerReg_Form.objects.filter(user_id=request.user.id)
        description=jobs.objects.filter(id=jobid)
        keyskills=employerkeyskills.objects.filter(job_id=jobid)
        return render_to_response('registration/Post_job_edit.html',{'cmpdetails':cmpdetails,'description':description,'keyskills':keyskills},context_instance=RequestContext(request))


@login_required(login_url='/accounts/EmpReg/')   
def inactive_jobpost(request):
    if request.method == "POST":
        jobid=request.POST.get('jobid')
        empid=request.POST.get('user_id')
        edit=jobs.objects.get(id=jobid,emp_id=empid)
        edit.is_active=False
        edit.save()
        return HttpResponseRedirect('/accounts/JobsEmp/')
    else:
        jobid=job_id
        description=jobs.objects.filter(id=jobid)
        keyskills=employerkeyskills.objects.filter(job_id=jobid)
        return render(request,'registration/RecruiterDashboardjobs.html',{'description':description,'keyskills':keyskills})


@login_required(login_url='/accounts/EmpReg/')   
def active_jobpost(request):
    if request.method == "POST":
        jobid=request.POST.get('jobid')
        empid=request.POST.get('user_id')
        todate=request.POST.get('todate')
        fromdate=request.POST.get('marklive')
      
        edit = jobs.objects.get(id=jobid)
        edit.marklive=fromdate
        edit.todate=todate
        edit.save()

        return HttpResponseRedirect('/accounts/JobsEmp/')
    else:
        jobid=job_id
        description=jobs.objects.filter(id=jobid)
        keyskills=employerkeyskills.objects.filter(job_id=jobid)
        return render_to_response('registration/RecruiterDashboardjobs.html',{'description':description,'keyskills':keyskills},context_instance=RequestContext(request))


@login_required(login_url='/accounts/EmpReg/')   
def activatetoday_jobpost(request):
    if request.method == "POST":
        jobid=request.POST.get('jobid')
        empid=request.POST.get('user_id')
        todate=request.POST.get('todate')

        now=datetime.now()
        #pd=now-timedelta(1)
        d=datetime(now.year, now.month, now.day)
        d1= d.strftime('%m-%d-%Y')
        
        edit = jobs.objects.get(id=jobid)
        edit.marklive=d1
        edit.todate=todate
        edit.save()

        return HttpResponseRedirect('/accounts/JobsEmp/')
    else:
        jobid=job_id
        description=jobs.objects.filter(id=jobid)
        keyskills=employerkeyskills.objects.filter(job_id=jobid)
        return render(request,'registration/RecruiterDashboardjobs.html',{'description':description,'keyskills':keyskills})

@login_required(login_url='/accounts/EmpReg/')   
def delete_searchagent(request):
    if request.method=='POST':
        empid=request.POST.get('empid')
        for sa in request.POST.get('saveresultid').split(','):
            recdet=RecSaveSearch.objects.get(id=sa,employer_id=empid)
            recdet.delete()
        messages.success(request, 'Search agent deleted successfully')
        return HttpResponseRedirect('/accounts/JobsEmp/')


@login_required(login_url='/accounts/EmpReg/')   
def delete_jobpost(request):
    if request.method == "POST":
        jobid=request.POST.get('jobid')
        empid=request.POST.get('user_id')
        #todate=request.POST.get('todate')

    a = jobs.objects.get(id=jobid)
    a.delete()
    messages.success(request, '1 jobpost deleted successfully')
    return HttpResponseRedirect('/accounts/JobsEmp/')

#---------------------------------------------------------------

def js_login(request):
    if request.user.is_authenticated():
        if request.user.usertype=='jobseeker':return HttpResponseRedirect('/accounts/Profile/')
    
    msg=""
    if request.method=='POST':
        un=request.POST.get('username')
        pw=request.POST.get('password')
        ut=request.POST.get('usertype')
        user =authenticate(username=un, password=pw)
        if user is not None:
    # the password verified for the user
            if user.is_active:
                if user.usertype == ut:
                    login(request, user)
                    messages.success(request, 'Logged in successfully')
                    return HttpResponseRedirect('/accounts/Profile/')
                else:
                    msg="Enter valid username and password"
                    #return render_to_response('registration/login.html', {'msg':msg}, context_instance=RequestContext(request))
            else:
                msg="Please Activate your Account"
                #return render_to_response('registration/login.html', {'msg':msg}, context_instance=RequestContext(request))
        else:
            msg="Enter valid username and password"
            #return render_to_response('registration/login.html', {'msg':msg}, context_instance=RequestContext(request))

    return render_to_response('registration/login.html', {'msg':msg}, context_instance=RequestContext(request))

#****************************************************************

@login_required(login_url='/accounts/EmpReg/')
def RecruiterHome(request):
    if request.method=='POST':
        form = RecruiterFolders(request.POST)
        if form.is_valid():
            foldername=request.POST.get('foldername')
            now=datetime.now()
            d=datetime(now.year, now.month, now.day)
            d1= d.strftime('%m-%d-%Y')
            s=RecruiterFolder(employer_id=request.user.id,foldername=foldername,lastupdate=d1)
            s.save()

            folderid=s.id
            messages.success(request, '1 folder created successfully')
            return HttpResponseRedirect('/accounts/RecruiterFolder/%s/' %folderid)

    else:
        try:

            empselpack= emp_selected_packs_add.objects.filter(employer_id=request.user.id).order_by('-pack_activate')

            emppack=emp_selected_packs_add.objects.filter(employer_id=request.user.id).count()

            msgpack="You have subscribed %s packs."%emppack

            now=datetime.now()
            d=datetime(now.year, now.month, now.day)
            d1= d.strftime('%m-%d-%Y')

            query = Q(employer_id=request.user.id) & Q(pack_expire__gte=d1)
            msgtime=emp_selected_packs.objects.filter(query).count()

            msg1="In Trial Pack You can post upto 5 Jobs."
            empsavesearch=RecSaveSearch.objects.filter(employer_id=request.user.id)
            sacount=RecSaveSearch.objects.filter(employer_id=request.user.id).count()
            msg = 5-sacount

            
            job = jobs.objects.filter(emp_id=request.user.id).count()
            folder=RecruiterFolder.objects.filter(employer_id=request.user.id)
            for i in folder:
                i.fcount=SaveCandidateFolder.objects.foldercount_fname(request.user.id,i)
            remaining = 5-job
            msg2 = "You have posted %s Jobs."% job
            msg3 = "At Maximum you have %s Jobs Post Remaining"% remaining
            return render_to_response('registration/RecruiterHome.html',{'empselpack':empselpack,'msgtime':msgtime,'msgpack':msgpack,'msg1': msg1, 'msg2':msg2, 'msg3':msg3,'folders':folder,'savesearch':empsavesearch },context_instance=RequestContext(request))

        except:
            msgpack="You have not subscribed any packs."
            msgtime="0"
            now=datetime.now()
            d=datetime(now.year, now.month, now.day)
            d1= d.strftime('%m-%d-%Y')

            query = Q(employer_id=request.user.id) & Q(pack_expire__gte=d1)

            
            

            msg1="Totally You have allow to Post 5 Jobs."
            empsavesearch=RecSaveSearch.objects.filter(employer_id=request.user.id)
            sacount=RecSaveSearch.objects.filter(employer_id=request.user.id).count()
            msg = 5-sacount

            
            job = jobs.objects.filter(emp_id=request.user.id).count()
            folder=RecruiterFolder.objects.filter(employer_id=request.user.id)
            for i in folder:
                i.fcount=SaveCandidateFolder.objects.foldercount_fname(request.user.id,i)
            remaining = 5-job
            msg2 = "You have posted %s Jobs."% job
            msg3 = "At Maximum you have %s Jobs Post Remaining"% remaining
            return render_to_response('registration/RecruiterHome.html',{'msgtime':msgtime,'msgpack':msgpack,'msg1': msg1, 'msg2':msg2, 'msg3':msg3,'folders':folder,'savesearch':empsavesearch },context_instance=RequestContext(request))


@login_required(login_url='/accounts/EmpReg/')
def RecruiterDashboard(request):
    d=dict()
    if request.method=='POST':
        form = RecruiterFolders(request.POST)

        if form.is_valid():
            foldername=request.POST.get('foldername')
            #return HttpResponse(foldername)
            now=datetime.now()
            d=datetime(now.year, now.month, now.day)
            d1= d.strftime('%m-%d-%Y')
            s=RecruiterFolder(employer_id=request.user.id,foldername=foldername,lastupdate=d1)
            s.save()

            folderid=s.id
            messages.success(request, '1 folder created successfully')
            return HttpResponseRedirect('/accounts/RecruiterFolder/%s/' %folderid)
    else:
        form = RecruiterFolders()
    activatedpacks=emppack_activation.objects.filter(subscribed_pack__employer_id=request.user.id)        
    empsavesearch=RecSaveSearch.objects.filter(employer_id=request.user.id)
    folder=RecruiterFolder.objects.filter(employer_id=request.user.id)
    for i in folder:
        i.fcount=SaveCandidateFolder.objects.foldercount_fname(request.user.id,i)
    query = Q(emp_id=request.user.id)
    query0 = Q(marklive__gt=datetime.now())
    query1 = Q(todate__gte=datetime.now())
    query11 = Q(marklive__lte=datetime.now())
    query2 = Q(todate__lt=datetime.now())
    PendingJobList=jobs.objects.filter(query,query0)
    ActJobList=jobs.objects.filter(query,query1,query11)
    InactJobList=jobs.objects.filter(query,query2)
    d= {'activatedpacks':activatedpacks,'ActJobList':ActJobList, 'InactJobList':InactJobList, 'PendingJobList':PendingJobList,'folders':folder,'savesearch':empsavesearch,'form':form}
    return render(request,'registration/RecruiterDashboard.html',d)        
@login_required(login_url='/accounts/EmpReg/')
def CandidateSearchResult(request):
    now=datetime.now()
    d=datetime(now.year, now.month, now.day)
    d1= d.strftime('%m-%d-%Y')
    if request.method=='POST':
        savesearch=request.POST.get('savesearch')
        searchname=request.POST.get('searchname')
        empid=request.user.id        
        s=RecSaveSearch(employer_id=empid,savedsearch=savesearch,searchname=searchname)
        s.save()
        messages.success(request, 'One search agent added successfully')
        return HttpResponseRedirect('/accounts/JobsEmp/')

    else:
        query_visibility = Q(jsdetails__visiblity=True) | Q(jsdetails__visiblepassive=True)
        searchresult=''
        s_query=request.GET['keywords'].strip()
        if s_query:searchresult=s_query[:-1].split(',') if s_query[-1] == ',' else s_query.split(',')
        list_result= []
        for search in searchresult:
            for res in User.objects.filter(Q(jsskills__skill__icontains=search) | Q(jspersonal__zipcode__icontains=search) | Q(jspersonal__country__icontains=search) | Q(jspersonal__state__icontains=search) | Q(jspersonal__city__icontains=search) | Q(jsdetailother__relocatechoice__icontains=search),query_visibility):
                if not res in list_result:
                    list_result.append(res)
        users = list_result    
        sacount=RecSaveSearch.objects.filter(employer_id=request.user.id).count()
        msg = 5-sacount
        empsavesearch=RecSaveSearch.objects.filter(employer_id=request.user.id)
        employers=jobs.objects.filter(emp_id=request.user.id)
        return render(request,'registration/CandidateSearchResult.html', {'empsavesearch':empsavesearch,'msg':msg,'details':users,'employers':employers})
@login_required(login_url='/accounts/EmpReg/')
def SearchResume(request):
    return render(request,'registration/search_resume.html')
@login_required(login_url='/accounts/EmpReg/')
def SearchResumeAdvanced(request):
    return render(request,'registration/searchresume_advanced.html')
def advsearch_result(request):
    if request.method == 'POST':
        saveurl=request.POST.get("savesearch")
        searchname=request.POST.get("JSsavejob")
        savesearch=JSsavesearch(user_id=request.user.id,searchname=searchname,searchlink=saveurl)
        savesearch.save()
        messages.success(request, 'Search agent saved successfully')
        return HttpResponseRedirect(saveurl)
    else:
        query1=Q(marklive__lte=datetime.now().date()) & Q(todate__gte=datetime.now().date())
        query2= Q(is_active=True)
        searchresult='null'
        s_query=request.GET['key_skills'].strip()
        if s_query:searchresult=s_query[:-1].split(',') if s_query[-1] == ',' else s_query.split(',')
        industry = request.GET['industry']
        functionalarea = request.GET['functionalarea']
        jobtype = request.GET['jobtype']
        workpermit = request.GET['workpermit']
        qualification = request.GET['qualification']
        salary_range = request.GET['salary_range']
        min_exp = request.GET['min_exp']
        max_exp = request.GET['max_exp']
        city = request.GET['city']
        radius=request.GET['miles']
        query_location=Q(city__icontains=city) | Q(state__icontains=city) | Q(country__icontains=city) | Q(zipcode__icontains=city)
        list_result=[]
        if max_exp and min_exp:
            for search in searchresult:
                for res in jobs.objects.filter(Q(employerkeyskills__keyskills__icontains=search) | Q(title__icontains=search),query1,query2,query_location,industry__icontains=industry,functionalarea__icontains=functionalarea,jobtype__icontains=jobtype,workpermit__icontains=workpermit,qualification__icontains=qualification,salary_range__icontains=salary_range,min_exp__gte=int(min_exp),max_exp__lte=int(max_exp)):
                    if not res in list_result:
                        list_result.append(res)
            details=list_result
        elif min_exp:
            for search in searchresult:
                for res in jobs.objects.filter(Q(employerkeyskills__keyskills__icontains=search) | Q(title__icontains=search),query1,query2,query_location,industry__icontains=industry,functionalarea__icontains=functionalarea,jobtype__icontains=jobtype,workpermit__icontains=workpermit,qualification__icontains=qualification,salary_range__icontains=salary_range,min_exp__gte=int(min_exp)):
                    if not res in list_result:
                        list_result.append(res)
            details=list_result
        elif max_exp:
            for search in searchresult:
                for res in jobs.objects.filter(Q(employerkeyskills__keyskills__icontains=search) | Q(title__icontains=search),query1,query2,query_location,industry__icontains=industry,functionalarea__icontains=functionalarea,jobtype__icontains=jobtype,workpermit__icontains=workpermit,qualification__icontains=qualification,salary_range__icontains=salary_range,max_exp__lte=int(max_exp)):
                    if not res in list_result:
                        list_result.append(res)
            details=list_result
        else:
            for search in searchresult:
                for res in jobs.objects.filter(Q(employerkeyskills__keyskills__icontains=search) | Q(title__icontains=search),query1,query2,query_location,industry__icontains=industry,functionalarea__icontains=functionalarea,jobtype__icontains=jobtype,workpermit__icontains=workpermit,qualification__icontains=qualification,salary_range__icontains=salary_range):
                    if not res in list_result:
                        list_result.append(res)
            details=list_result
        if radius:
            if city:
                latlng=gn.geocode(city, exactly_one=False)[0]
                result=[]
                for i in details:
                    rlat=radians(float(i.lat))
                    slat=radians(latlng[1][0])
                    long_diff = radians(float(i.lng) - latlng[1][1])
                    distance = (sin(rlat) * sin(slat) + cos(rlat) * cos(slat) * cos(long_diff))
                    miles=degrees(acos(distance)) * 69.09
                    if miles <= int(radius):
                        result.append(i)
                details=result
        details2 = User.objects.filter(jobs__isnull=False).annotate(job_count=Count('jobs')).order_by('-job_count')
        details3 = jobs.objects.values('state').annotate(count=Count('state')).order_by('-count')
        details4 = jobs.objects.values('industry').annotate(count=Count('industry')).order_by('-count')
        savecount=JSsavesearch.objects.filter(user_id=request.user.id).count()
        msg=5-savecount
        return render(request,'registration/searchresult.html', {'details': details,'details2':details2,'details3':details3,'details4':details4,'msg':msg})
@login_required(login_url='/accounts/EmpReg/')
def SearchResumeAdvancedResult(request):
    searchresult='null'
    s_query=request.GET['key_skills'].strip()
    if s_query:searchresult=s_query[:-1].split(',') if s_query[-1] == ',' else s_query.split(',')
    functional_area = request.GET['functional_area']
    emp_type = request.GET['emp_type']
    workpermit = request.GET['workpermit']
    work_expmin = request.GET['min_exp']
    work_expmax = request.GET['max_exp']
    telecommute = request.GET['telecommute']
    state = request.GET['location']
    radius = request.GET['miles']
    list_result=[]
    query_function = Q(jspersonal__functional_area__icontains=functional_area)
    query_jobtype = Q(jsdetailother__emptype__icontains=emp_type)
    query_workpermit = Q(jsdetailother__workpermit__icontains=workpermit)
    query_loc = Q(jspersonal__state__icontains=state) | Q(jspersonal__city__icontains=state) | Q(jspersonal__country__icontains=state) | Q(jspersonal__zipcode__icontains=state) | Q(jsdetailother__relocatechoice__icontains=state)
    query_workexp = Q(jspersonal__work_expyears__gte=work_expmin) & Q(jspersonal__work_expyears__lte=work_expmax)
    query_visibility = Q(jsdetails__visiblity=True) | Q(jsdetails__visiblepassive=True)
    if work_expmin and work_expmax:
        for search in searchresult:
            for res in User.objects.filter(Q(jsskills__skill__icontains=search),query_function,query_jobtype,query_workpermit,query_workexp,query_loc,Q(jsdetailother__telecommunicate__icontains=telecommute),query_visibility):
                  if not res in list_result:
                      list_result.append(res)
        details=list_result
    elif work_expmin:
        for search in searchresult:
            for res in User.objects.filter(Q(jsskills__skill__icontains=search),query_function,query_jobtype,query_workpermit,Q(jspersonal__work_expyears__gte=work_expmin),query_loc,Q(jsdetailother__telecommunicate__icontains=telecommute),query_visibility):
                if not res in list_result:
                    list_result.append(res)
        details=list_result
    elif work_expmax:
        for search in searchresult:
            for res in User.objects.filter(Q(jsskills__skill__icontains=search),query_function,query_jobtype,query_workpermit,Q(jspersonal__work_expyears__lte=work_expmax),query_loc,Q(jsdetailother__telecommunicate__icontains=telecommute),query_visibility):
                if not res in list_result:
                    list_result.append(res)
        details=list_result
    else:
        for search in searchresult:
            for res in User.objects.filter(Q(jsskills__skill__icontains=search),query_function,query_jobtype,query_workpermit,Q(jsdetailother__telecommunicate__icontains=telecommute),query_loc,query_visibility):
                if not res in list_result:
                    list_result.append(res)
        details=list_result
    if radius:
        if state:
            latlng=gn.geocode(state, exactly_one=False)[0]
            result=[]
            for i in details:
                rlat=radians(float(i.jspersonal.lat))
                slat=radians(latlng[1][0])
                long_diff = radians(float(i.jspersonal.lng) - latlng[1][1])
                distance = (sin(rlat) * sin(slat) + cos(rlat) * cos(slat) * cos(long_diff))
                miles=degrees(acos(distance)) * 69.09
                if miles <= int(radius):
                    result.append(i)
            details=result
    return render(request,'registration/CandidateSearchResult.html', {'details': details})
@login_required(login_url='/accounts/EmpReg/')
def JSDetailsbyIndividual(request,user_id):
    user_id=user_id
    count=0
    for i in emp_subscribed_packs.objects.filter(employer_id=request.user.id):
        for j in emppack_activation.objects.filter(subscribed_pack_id=i.id):
            count=j.totalresume+count #total resumeviews remaining
    if count:
        if profileviews.objects.filter(employer_id=request.user.id,jobseeker=user_id):
            edit=profileviews.objects.get(employer_id=request.user.id,jobseeker=user_id)
            edit.save()
            folder=RecruiterFolder.objects.filter(employer_id=request.user.id)
            users=User.objects.filter(id=user_id)
            user_id=user_id
            js=JSDetails.objects.filter(user_id=user_id)
            query1= Q(emp_id=request.user.id)
            query2 = Q(todate__gte=datetime.now().date())
            query3 = Q(marklive__lte=datetime.now().date())
            joblist=jobs.objects.filter(query1,query2,query3).select_related()
            employers=jobs.objects.filter(emp_id=request.user.id)
            return render(request, 'registration/EmployerViewJSDetails.html',{'users':users,'folder':folder,'js':js,'joblist':joblist,'employers':employers})
        elif count>profileviews.objects.filter(employer_id=request.user.id).count():
            js=JSDetails.objects.get(user_id=user_id)
            vcount=js.viewcount
            vcount=vcount+1
            js.viewcount=vcount
            js.save()
            if not profileviews.objects.filter(employer_id=request.user.id,jobseeker=user_id):
                profileviews(employer_id=request.user.id,jobseeker=user_id).save()
            folder=RecruiterFolder.objects.filter(employer_id=request.user.id)
            users=User.objects.filter(id=user_id)
            user_id=user_id
            js=JSDetails.objects.filter(user_id=user_id)
            query1= Q(emp_id=request.user.id)
            query2 = Q(todate__gte=datetime.now().date())
            query3 = Q(marklive__lte=datetime.now().date())
            joblist=jobs.objects.filter(query1,query2,query3).select_related()
            employers=jobs.objects.filter(emp_id=request.user.id)
            return render(request, 'registration/EmployerViewJSDetails.html',{'users':users,'folder':folder,'js':js,'joblist':joblist,'employers':employers})
        else:
            messages.error(request, "You can't view profile. Kindly subscribed the new pack")
            return HttpResponseRedirect('/accounts/EmpPackname/')
    else:
        messages.error(request, "You can't view profile. Kindly subscribed the new pack")
        return HttpResponseRedirect('/accounts/EmpPackname/')


    
def HotResumes(request):
    hotresumes = User.objects.filter(jsdetails__visiblity=True).order_by('-jsdetails__viewcount')
    return render(request,'registration/HotResumes.html', {'hotresumes':hotresumes})

def SecretClearedResumes(request):
    scr1 = ~Q(jssecurity__jssecretclear='None')
    scr2 = ~Q(jssecurity__jssecretclear="")
    scresumes = User.objects.filter(scr1,scr2,jsdetails__visiblity=True).order_by('-jsdetails__update_date')
    return render(request,'registration/SecretClearedResumes.html',{'scresumes':scresumes})
@login_required(login_url='/accounts/EmpReg/')
def saveCandidate(request):    
    if request.method=='POST':
        now=datetime.now()
        d=datetime(now.year, now.month, now.day)
        d1= d.strftime('%m-%d-%Y')
        empid=request.POST.get('empid')
        folderid=request.POST.get('folderid')
        jsid=request.POST.get('jsid')
        userid=request.POST.get('userid')        
        if SaveCandidateFolder.objects.filter(folder_id=folderid,employer_id=empid,jobseeker_id=jsid):
            messages.error(request, 'Saved Candidate already exist')
            return HttpResponseRedirect('/accounts/JSDetails/%s/' %userid)
        sc=SaveCandidateFolder(folder_id=folderid,employer_id=empid,jobseeker_id=jsid)
        sc.save()
        edit=RecruiterFolder.objects.get(id=folderid)
        edit.lastupdate=d1
        edit.save()
        messages.success(request, 'Candidate saved successfully')
        return HttpResponseRedirect('/accounts/JSDetails/%s/' %userid)
@login_required(login_url='/accounts/EmpReg/')
def FolderCreation(request):
    if request.method=='POST':
        empid=request.POST.get('empid')
        foldername=request.POST.get('foldername')
        jsid=request.POST.get('jsid')
        userid=request.POST.get('userid')
        now=datetime.now()
        d=datetime(now.year, now.month, now.day)
        d1= d.strftime('%m-%d-%Y')
        fold,created=RecruiterFolder.objects.get_or_create(foldername=foldername,employer_id=empid)
        if SaveCandidateFolder.objects.filter(folder_id=fold.id,employer_id=empid,jobseeker_id=jsid):
            messages.success(request, 'Saved Candidate already exist')
            return HttpResponseRedirect('/accounts/JSDetails/%s/' %userid)
        sc=SaveCandidateFolder(folder_id=fold.id,employer_id=empid,jobseeker_id=jsid)
        sc.save()
        messages.success(request, 'Candidate saved successfully')
        fold.lastupdate=d1
        fold.save()
        return HttpResponseRedirect('/accounts/JSDetails/%s/' %userid)
@login_required(login_url='/accounts/EmpReg/')
def ScheduleInterviewEmp(request):
    now=datetime.now()
    d1= now.strftime('%m-%d-%Y-%H:%M')
    if request.method=='POST':
        userid=request.POST.get('userid')
        isreschedule=request.POST.get('isreschedule')
        if int(isreschedule) is 1:
            empid=request.POST.get('empid')
            jobid=request.POST.get('jobid')
            scheduledate=request.POST.get('scheduledate')
            scheduletime=request.POST.get('scheduletime')
            totalrounds=request.POST.get('totalrounds')
            interviewLocation=request.POST.get('location')
            inter=Interview(emp_id=empid,JSId_id=int(jsid),Job_id=jobid,rounds=totalrounds,interviewLocation=interviewLocation,Denied=False)
            inter.save()
            interview_id=inter.id
            res=Reschedule(interview_id=interview_id,emp_id=empid,JSId_id=jsid,Job_id=jobid,empschedule_date1=scheduledate,empschedule_time1=scheduletime,empupdate1=d1,Empconfirmation=True,JSconfirmation=False)
            res.save()
        else:
            empid=request.POST.get('empid')
            jobid=request.POST.get('jobid')
            scheduledate=request.POST.get('scheduledate')
            scheduletime=request.POST.get('scheduletime')
            totalrounds=request.POST.get('totalrounds')
            interviewLocation=request.POST.get('location')
            inter=Interview(emp_id=empid,JSId_id=int(jsid),Job_id=jobid,rounds=totalrounds,interviewLocation=interviewLocation,Denied=False)
            inter.save()
            interview_id=inter.id
            res=Reschedule(interview_id=interview_id,emp_id=empid,JSId_id=jsid,Job_id=jobid,empschedule_date1=scheduledate,empschedule_time1=scheduletime,empupdate1=d1,Empconfirmation=True,JSconfirmation=True)
            res.save()
        messages.success(request, 'Interview has been scheduled successfully')
        return HttpResponseRedirect('/accounts/MyInterviewZoneEmp')
@login_required(login_url='/accounts/EmpReg/')
def ScheduleInterviewEmp1(request):
    now=datetime.now()
    d1= now.strftime('%m-%d-%Y-%H:%M')
    if request.method=='POST':
        isreschedule=request.POST.get('isreschedule')
        if int(isreschedule) is 1:
            for jsid in request.POST.get('jsid').split(','):
                empid=request.POST.get('empid')
                jobid=request.POST.get('jobid')
                scheduledate=request.POST.get('scheduledate')
                scheduletime=request.POST.get('scheduletime')
                totalrounds=request.POST.get('totalrounds')
                interviewLocation=request.POST.get('location')
                js=JSDetails.objects.get(id=jsid)
                usid=js.user_id
                jsp=JSPersonal.objects.get(JS_id=jsid)
                sectoem=jsp.sec_email
                us=User.objects.get(id=usid)
                pritoem=us.email
                first_name=us.first_name
                last_name=us.last_name
                username=us.username
                title=jobs.objects.get(id=jobid)
                jobtitle=title.title
                jrcode=title.referencecode
                frommail=title.email
                company=title.emp.companyname
                subject="Interview sechduled for %s " %jobtitle
                current_domain = Site.objects.get_current().domain
                contxt=Context({'company': company,'jobtitle':jobtitle,'jrcode':jrcode,'first_name':first_name,'last_name':last_name,'username':username,'current_domain':current_domain})
                message_template = loader.get_template('registration/interviewschedulemail.html')    
                message=message_template.render(contxt)
                msg=EmailMultiAlternatives(subject,message,frommail,[pritoem,sectoem])
                msg.attach_alternative(message, "text/html")
                msg.send()
                inter=Interview(emp_id=empid,JSId_id=int(jsid),Job_id=jobid,rounds=totalrounds,interviewLocation=interviewLocation,Denied=False)
                inter.save()
                interview_id=inter.id
                res=Reschedule(interview_id=interview_id,emp_id=empid,JSId_id=jsid,Job_id=jobid,empschedule_date1=scheduledate,empschedule_time1=scheduletime,empupdate1=d1,Empconfirmation=True,JSconfirmation=False)
                res.save()
        else:           
            for jsid in request.POST.get('jsid').split(','):
                empid=request.POST.get('empid')
                jobid=request.POST.get('jobid')
                scheduledate=request.POST.get('scheduledate')
                scheduletime=request.POST.get('scheduletime')
                totalrounds=request.POST.get('totalrounds')
                interviewLocation=request.POST.get('location')
                js=JSDetails.objects.get(id=jsid)
                usid=js.user_id
                jsp=JSPersonal.objects.get(JS_id=jsid)
                sectoem=jsp.sec_email
                us=User.objects.get(id=usid)
                pritoem=us.email
                first_name=us.first_name
                last_name=us.last_name
                username=us.username
                title=jobs.objects.get(id=jobid)
                jobtitle=title.title
                jrcode=title.referencecode
                frommail=title.email
                company=title.emp.companyname
                subject="Interview sechduled for %s " %jobtitle
                current_domain = Site.objects.get_current().domain
                contxt=Context({'company': company,'jobtitle':jobtitle,'jrcode':jrcode,'first_name':first_name,'last_name':last_name,'username':username,'current_domain':current_domain})
                message_template = loader.get_template('registration/interviewschedulemail.html')    
                message=message_template.render(contxt)
                msg=EmailMultiAlternatives(subject,message,frommail,[pritoem,sectoem])
                msg.attach_alternative(message, "text/html")
                msg.send()
                inter=Interview(emp_id=empid,JSId_id=int(jsid),Job_id=jobid,rounds=totalrounds,interviewLocation=interviewLocation,Denied=False)
                inter.save()
                interview_id=inter.id
                res=Reschedule(interview_id=interview_id,emp_id=empid,JSId_id=jsid,Job_id=jobid,empschedule_date1=scheduledate,empschedule_time1=scheduletime,empupdate1=d1,Empconfirmation=True,JSconfirmation=True)
                res.save()
        messages.success(request, 'Interview has been scheduled successfully')
        return HttpResponseRedirect('/accounts/MyInterviewZoneEmp/')
@login_required(login_url='/accounts/EmpReg/')
def ScheduleInterviewEmp2(request):
    now=datetime.now()
    d1= now.strftime('%m-%d-%Y-%H:%M')
    if request.method=='POST':
        isreschedule=request.POST.get('isreschedule')
        if int(isreschedule) is 1:
            for jsid in request.POST.get('jsid').split(','):
                empid=request.POST.get('empid')
                jobid=request.POST.get('jobid')
                scheduledate=request.POST.get('scheduledate')
                scheduletime=request.POST.get('scheduletime')
                totalrounds=request.POST.get('totalrounds')
                interviewLocation=request.POST.get('location')
                js=JSAppliedJobs.objects.get(id=jsid)
                jsp=JSPersonal.objects.get(JS_id=js.JS.id)
                sectoem=jsp.sec_email
                us=User.objects.get(id=js.JS.user.id)
                pritoem=us.email
                first_name=us.first_name
                last_name=us.last_name
                username=us.username

                title=jobs.objects.get(id=jobid)
                jobtitle=title.title
                jrcode=title.referencecode
                frommail=title.email

                company=request.user.companyname

                subject="Interview sechduled for %s " %jobtitle
                current_domain = Site.objects.get_current().domain
                contxt=Context({'company': company,'jobtitle':jobtitle,'jrcode':jrcode,'first_name':first_name,'last_name':last_name,'username':username,'current_domain':current_domain})
                message_template = loader.get_template('registration/interviewschedulemail.html')    
                message=message_template.render(contxt)
                msg=EmailMultiAlternatives(subject,message,frommail,[pritoem,sectoem])
                msg.attach_alternative(message, "text/html")
                msg.send()
                inter=Interview(emp_id=empid,JSId_id=js.JS.id,Job_id=jobid,rounds=totalrounds,interviewLocation=interviewLocation,Denied=False)
                inter.save()
                interview_id=inter.id
                res=Reschedule(interview_id=interview_id,emp_id=empid,JSId_id=js.JS.id,Job_id=jobid,empschedule_date1=scheduledate,empschedule_time1=scheduletime,empupdate1=d1,Empconfirmation=True,JSconfirmation=False)
                res.save()
        else:
           
            for jsid in request.POST.get('jsid').split(','):
                
                empid=request.POST.get('empid')
                jobid=request.POST.get('jobid')
                scheduledate=request.POST.get('scheduledate')
                scheduletime=request.POST.get('scheduletime')
                totalrounds=request.POST.get('totalrounds')
                interviewLocation=request.POST.get('location')
                js=JSAppliedJobs.objects.get(id=jsid)
                jsp=JSPersonal.objects.get(JS_id=js.JS.id)
                sectoem=jsp.sec_email
                us=User.objects.get(id=js.JS.user.id)
                pritoem=us.email
                first_name=us.first_name
                last_name=us.last_name
                username=us.username
                title=jobs.objects.get(id=jobid)
                jobtitle=title.title
                jrcode=title.referencecode
                frommail=title.email
                company=title.emp.companyname
                subject="Interview sechduled for %s " %jobtitle
                current_domain = Site.objects.get_current().domain
                contxt=Context({'company': company,'jobtitle':jobtitle,'jrcode':jrcode,'first_name':first_name,'last_name':last_name,'username':username,'current_domain':current_domain})
                message_template = loader.get_template('registration/interviewschedulemail.html')    
                message=message_template.render(contxt)
                msg=EmailMultiAlternatives(subject,message,frommail,[pritoem,sectoem])
                msg.attach_alternative(message, "text/html")
                msg.send()
                inter=Interview(emp_id=empid,JSId_id=js.JS.id,Job_id=jobid,rounds=totalrounds,interviewLocation=interviewLocation,Denied=False)
                inter.save()
                interview_id=inter.id
                res=Reschedule(interview_id=interview_id,emp_id=empid,JSId_id=js.JS.id,Job_id=jobid,empschedule_date1=scheduledate,empschedule_time1=scheduletime,empupdate1=d1,Empconfirmation=True,JSconfirmation=True)
                res.save()

        messages.success(request, 'Interview has been scheduled successfully')
        return HttpResponseRedirect('/accounts/MyInterviewZoneEmp/')



@login_required(login_url='/accounts/EmpReg/')
def RecruiterChangePassword(request):
    if request.method=="POST":
        frm_pass= PasswordReset(request.POST,user=request.user)
        if frm_pass.is_valid():
            pass2=request.POST.get('password2')
            usr=User.objects.get(id__exact=request.user.id)
            usr.set_password(pass2)
            usr.save()
            messages.success(request, 'Your password has been changed successfully')
            return HttpResponseRedirect("/accounts/RecruiterChangePassword/")

    else:
        frm_pass=PasswordReset(user=request.user)
    return render(request,'registration/RecruiterChangePassword.html',{'form':frm_pass})

@login_required(login_url='/accounts/login/')
def JSChangePassword(request):
    if request.method=="POST":
        frm_pass= PasswordReset(request.POST,user=request.user)
        if frm_pass.is_valid():
            pass2=request.POST.get('password2')
            usr=User.objects.get(id__exact=request.user.id)
            usr.set_password(pass2)
            usr.save()
            messages.success(request, 'Your password has been changed successfully')
            return HttpResponseRedirect('/accounts/JSChangePassword/')
            
    else:
        frm_pass=PasswordReset(user=request.user)
    return render(request,'registration/JSChangePassword.html',{'form':frm_pass})

@login_required(login_url='/accounts/login/')
def ApplyJob(request,job_id):
    jobid=job_id

    try:
        details=JSDetails.objects.get(user_id=request.user.id)
        personal=JSPersonal.objects.get(user_id=request.user.id)
        txtres=JSTextResume.objects.get(user_id=request.user.id)
        actres=JSResumeActive.objects.get(user_id=request.user.id)
        resid=actres.resumeActive_id
        res=JSResume.objects.get(id=resid)
        semail=personal.sec_email
        handno=personal.handno
        workno=personal.workno
        homeno=personal.homeno
        wexpyear=personal.work_expyears
        wexpmon=personal.work_expmonths
        lsalary=personal.salaryrange
        fname=personal.user.first_name
        lname=personal.user.last_name
        pemail=personal.user.email
        resume=res.resumeFile
        med=settings.MEDIA_ROOT+'/%s' %resume
        job=jobs.objects.get(id=jobid)
        jrcode=job.referencecode
        jtitle=job.title
        to=job.emp.email
        hitcount=job.hitcount
        current_domain = Site.objects.get_current().domain
        subject="Job Applied for the Position of %s [%s]" % (jtitle, jrcode)
        message_template = loader.get_template('registration/message.html')
        message_context = Context({'username':job.emp.username,'companyname':job.emp.companyname,'position':jtitle,'jobcode':jrcode,'current_domain':current_domain, 'semail': semail, 'fname': fname, 'lname':lname, 'pemail':pemail, 'handno':handno,'workno':workno,'homeno':homeno,'wexpyear':wexpyear, 'wexpmon':wexpmon, 'lsalary':lsalary })
        message = message_template.render(message_context)
        try:
            msg=EmailMultiAlternatives(subject,message,pemail,[to])
            msg.attach_alternative(message, "text/html")
            if not txtres.activetext_resume:
                msg.attach_file(med)
            msg.send()
            hitcount=hitcount+1
            job.hitcount=hitcount
            job.save()
            appliedjob=JSAppliedJobs(JS_id=personal.id,emp_id=job.emp.id,Job_id=job.id)
            appliedjob.save()
            messages.success(request, 'Job has been applied successfully')
            return HttpResponseRedirect('/accounts/JobApplySuccess/')
        except:
            raise Http404
    except:
        usr=User.objects.get(id__exact=request.user.id)
        fname=usr.first_name
        lname=usr.last_name
        pemail=usr.email
        job=jobs.objects.get(id__exact=jobid)
        hitcount=job.hitcount
        jrcode=job.referencecode
        jtitle=job.title
        to=job.emp.email
        current_domain = Site.objects.get_current().domain
        subject="Job Applied for the Position of %s [%s]" % (jtitle, jrcode)
        message_template = loader.get_template('registration/message.html')
        message_context = Context({'username':request.user.username,'companyname':request.user.companyname,'position':jtitle,'jobcode':jrcode,'current_domain':current_domain,'fname': fname, 'lname':lname, 'pemail':pemail})
        message = message_template.render(message_context)
        msg=EmailMultiAlternatives(subject,message,pemail,[to])
        msg.attach_alternative(message, "text/html")
        msg.send()
        hitcount=hitcount+1
        job.hitcount=hitcount
        job.save()
        appliedjob=JSAppliedJobs(JS_id=personal.id,emp_id=job.emp.id,Job_id=job.id)
        appliedjob.save()
        messages.success(request, 'Job has been applied successfully')
        return HttpResponseRedirect('/accounts/JobApplySuccess/')

def faq(request):
    return render_to_response('registration/faq.html',context_instance=RequestContext(request))

    
def faq1(request):
    return render_to_response('registration/faq1.html',context_instance=RequestContext(request))
def faq2(request):
    return render_to_response('registration/faq2.html',context_instance=RequestContext(request))
def faq3(request):
    return render_to_response('registration/faq3.html',context_instance=RequestContext(request))
def faq4(request):
    return render_to_response('registration/faq4.html',context_instance=RequestContext(request))
def faq5(request):
    return render_to_response('registration/faq5.html',context_instance=RequestContext(request))
def faq6(request):
    return render_to_response('registration/faq6.html',context_instance=RequestContext(request))
def faq7(request):
    return render_to_response('registration/faq7.html',context_instance=RequestContext(request))
def faq8(request):
    return render_to_response('registration/faq8.html',context_instance=RequestContext(request))
def faq9(request):
    return render_to_response('registration/faq9.html',context_instance=RequestContext(request))
def faq10(request):
    return render_to_response('registration/faq10.html',context_instance=RequestContext(request))
def AboutUs(request):
    return render_to_response('registration/AboutUs.html',context_instance=RequestContext(request))
def PrivacyPolicy(request):
    return render_to_response('registration/Privacy&Policy.html',context_instance=RequestContext(request))
def TermsOfUse(request):
    return render_to_response('registration/TermsOfUse.html',context_instance=RequestContext(request))
def Feedback(request):
    if request.method=='POST':
        names=request.POST.get('names')
        fromemail=request.POST.get('email')
        subject=request.POST.get('Subject')
        message=request.POST.get('message')
        usr=User.objects.get(is_staff=True)
        toemail=usr.email
        #toemail="karthik@capsone.com"
        send_mail(subject, message, fromemail, [toemail])
        messages.success(request, 'Thank you for your Feedback, It will let us to enhance our services for you')
        return HttpResponseRedirect('/accounts/Feedback/')
    else:
        return render(request,'registration/Feedback.html')

def ContactUs(request):
    if 'lang' in request.GET:
        from django.utils.translation import activate
        activate(request.GET['lang'])
    return render_to_response('registration/ContactUs.html',context_instance=RequestContext(request))
def Help(request):
    return render_to_response('registration/Help.html',context_instance=RequestContext(request))
def TechNews(request):
    return render_to_response('registration/TechNews.html',context_instance=RequestContext(request))
def MarketReport(request):
    return render_to_response('registration/MarketReport.html',context_instance=RequestContext(request))
def PressRelease(request):
    return render_to_response('registration/PressRelease.html',context_instance=RequestContext(request))

def JobFair(request):
    return render_to_response('registration/Jobs_fair.html',context_instance=RequestContext(request))

def Testimonial(request):
    return render_to_response('registration/Testimonial.html',context_instance=RequestContext(request))

def Events(request):
    return render_to_response('registration/Events.html',context_instance=RequestContext(request))

def Webinars(request):
    return render_to_response('registration/Webinars.html',context_instance=RequestContext(request))


def JobsCity(request):
    jobsloc = jobs.objects.values('state').annotate(count=Count('state')).order_by('-count')

    return render_to_response('registration/JobsCity.html',{'jobsloc':jobsloc},context_instance=RequestContext(request))

def JobsCompany(request):
    compjob = User.objects.filter(jobs__isnull=False).annotate(job_count=Count('jobs')).order_by('-job_count')
    return render_to_response('registration/JobsCompany.html',{'compjob':compjob},context_instance=RequestContext(request))

def JobsCategory(request):
    jobcat = jobs.objects.values('industry').annotate(count=Count('industry')).order_by('-count')
    return render_to_response('registration/JobsCategory.html',{'jobcat':jobcat}, context_instance=RequestContext(request))

def JobsContract(request):
    jobcontract = jobs.objects.values('jobtype').annotate(count=Count('jobtype')).order_by('-count')
    return render_to_response('registration/JobsContract.html',{'jobcontract':jobcontract},context_instance=RequestContext(request))


#@login_required(login_url='/accounts/login/')
def SocialPassReset(request):

    if request.method == 'POST':
        uid=request.POST.get('userid')
        usertype=request.POST.get('usertype')
        un=request.POST.get('username')
        pas=request.POST.get('password1')

        usr=User.objects.get(id=uid)
        usr.usertype=usertype
        usr.username=un
        usr.save()
        usr1=User.objects.get(id=uid)
        usr1.set_password(pas)
        usr1.save()
        return HttpResponseRedirect('/accounts/Profile/')
    else:
        
        return render_to_response('registration/socialpassreset.html', context_instance=RequestContext(request))


@login_required(login_url='/accounts/login/')
def subprofilepages(request,num):
    #if num not in '12345678':
    #    raise Http404()

    temp=['personalinfo','educationdetails','profilesummary',
    'itskills','employmentdetails','projectDetails','otherDetails',
    'resumeupload','jssecurityclearance']
    details = User.objects.filter(id=request.user.id)
    details1 = JSDetails.objects.filter(user_id=request.user.id)
    if not details1:
        return HttpResponseRedirect("/accounts/ProfileDetails/")
    else:
        users = User.objects.get(id=request.user.id)
        detail = JSDetails.objects.filter(user_id=request.user.id)
        personal = JSPersonal.objects.filter(user_id=request.user.id)
        qualification = JSQualification.objects.filter(user_id=request.user.id)
        certificate = JSCertificate.objects.filter(user_id=request.user.id)
        profilesum = JSProfileSummary.objects.filter(user_id=request.user.id)
        skills = JSSkills.objects.filter(user_id=request.user.id)
        employer = JSEmployerDetails.objects.filter(user_id=request.user.id)
        project = JSProjectDetails.objects.filter(user_id=request.user.id)
        language = JSLanguage.objects.filter(user_id=request.user.id)
        other = JSDetailOther.objects.filter(user_id=request.user.id)
        
        videoresume = RecordedVideos.objects.filter(user=request.user)
        jssecclear = JSsecurity.objects.filter(user_id=request.user.id)
        #extra = JSExtra.objects.filter(user_id=request.user.id)


        text=JSTextResume.objects.get(user_id=request.user.id)
        act=text.activetext_resume
        tresume=JSTextResume.objects.filter(user_id=request.user.id)
        if act:

            return render_to_response('registration/test/'+temp[int(num)-1]+'.html', {"user":users,'detail':detail,'personal':personal,'qualification':qualification,'certificate':certificate,'profilesum':profilesum,'skills':skills,'employer':employer,'project':project,'other':other,'videoresume':videoresume,'resume':tresume,'jssecclear':jssecclear,'details1':details1,'language':language}, context_instance=RequestContext(request))
        else:
            try:
                res=JSResumeActive.objects.get(user_id=request.user.id)
                resactid=res.resumeActive_id
                resume=JSResume.objects.filter(id=resactid)

                return render_to_response('registration/test/'+temp[int(num)-1]+'.html', {"user":users,'detail':detail,'personal':personal,'qualification':qualification,'certificate':certificate,'profilesum':profilesum,'skills':skills,'employer':employer,'project':project,'other':other,'videoresume':videoresume,'resume':resume,'jssecclear':jssecclear,'details1':details1,'language':language}, context_instance=RequestContext(request))
            except:
                return render_to_response('registration/test/'+temp[int(num)-1]+'.html', {"user":users,'detail':detail,'personal':personal,'qualification':qualification,'certificate':certificate,'profilesum':profilesum,'skills':skills,'employer':employer,'project':project,'other':other,'videoresume':videoresume,'jssecclear':jssecclear,'details1':details1,'language':language}, context_instance=RequestContext(request))

        


@login_required(login_url='/accounts/EmpReg/')
def EmployerFolder(request,fid):
    
    folderid=fid
    folder=RecruiterFolder.objects.get(id=folderid)
    details=SaveCandidateFolder.objects.filter(folder_id=folderid,employer_id=request.user.id)
    return render_to_response('registration/SaveCandidateDetails.html',{'folder':folder, 'fdetails':details}, context_instance=RequestContext(request))



    '''folder=RecruiterFolder.objects.get(id=folderid)
            
                details=SaveCandidateFolder.objects.filter(folder_id=folderid)
                folderdetails=[]
                for i in details:
                    folderdetails.append(JSDetails.objects.get(id=i.jobseeker_id))
            
                #   return HttpResponse(js.id)
                return render_to_response('registration/SaveCandidateDetails.html',{'folder':folder, 'fdetails':folderdetails}, context_instance=RequestContext(request))'''


#----------------- 1st JUNE ----------------------

@login_required(login_url='/accounts/EmpReg/')
def RecruiterDashboardjobs(request,jsjob_id):
    msg=""
    job = jobs.objects.filter(emp_id=request.user.id).count()
    remaining = 5-job
    msg = "You Have Posted %s Jobs and "% job 
    msg1 = "You Have %s Job Posts Remaining"% remaining
    query = Q(emp_id=request.user.id)
    query0 = Q(marklive__gt=datetime.now().date())
    query1 = Q(todate__gte=datetime.now().date())
    query11 = Q(marklive__lte=datetime.now().date())
    query2 = Q(todate__lt=datetime.now().date())
    PendingJobList=jobs.objects.filter(query,query0)
    ActJobList=jobs.objects.filter(query,query1,query11)
    InactJobList=jobs.objects.filter(query,query2)
    msgActive = "Active Jobs"
    msgInactive = "Inactive Jobs"
    msgPending = "Future Jobs"
    msgAll = "All Jobs"
    allpostedjobs=jobs.objects.filter(emp_id=request.user.id)
    employerPackages=emppack_activation.objects.filter(subscribed_pack__employer_id=request.user.id)
    if employerPackages:
        jobcount=0
        for pack in employerPackages:
            jobcount+=pack.totaljobpost

    if jsjob_id=='1':
        msg2 = "YOUR OPEN JOBS"
        return render(request,'registration/RecruiterDashboardjobs.html', {'msgInactive':msgInactive,'msgPending':msgPending,'msgAll':msgAll,'jsjob_id':jsjob_id,'msg': msg,'msg1':msg1,'msg2':msg2,'remaining':remaining,'ActJobList':ActJobList})

    elif jsjob_id=='2':
        msg2 = "YOUR EXPIRED JOBS"
        return render(request,'registration/RecruiterDashboardjobs.html', {'msgActive':msgActive,'msgPending':msgPending,'msgAll':msgAll,'jsjob_id':jsjob_id,'msg': msg,'msg1':msg1,'msg2':msg2,'remaining':remaining,'InactJobList':InactJobList})

    elif jsjob_id=='3':
        msg2 = "YOUR FUTURE JOBS"
        return render(request,'registration/RecruiterDashboardjobs.html', {'msgActive':msgActive,'msgInactive':msgInactive,'msgAll':msgAll,'jsjob_id':jsjob_id,'msg': msg,'msg1':msg1,'msg2':msg2,'remaining':remaining,'PendingJobList':PendingJobList})

    elif jsjob_id=='4':
        msg2 = "YOUR POSTED JOBS"
        return render(request,'registration/RecruiterDashboardjobs.html', {'allpostedjobs':allpostedjobs,'employerPackages':employerPackages,'jobcount':jobcount})


@login_required(login_url='/accounts/EmpReg/')
def SearchAllJobs(request):
    userid=request.user.id
    details=jobs.objects.filter(emp_id__exact=userid)
    
    return render_to_response('registration/search_all_jobs.html',{'details': details}, context_instance=RequestContext(request))

@login_required(login_url='/accounts/EmpReg/')
def SearchAllJobsResult(request):
    ownername = request.GET['ownername']
    referencecode = request.GET['referencecode']
    title = request.GET['title']
    jobtype = request.GET['jobtype']
    after = request.GET['after']
    before = request.GET['before']

    now=datetime.now()
    d=datetime(now.year, now.month, now.day)
    d1= d.strftime('%m-%d-%Y')

    query = Q(emp_id=request.user.id,ownername__icontains=ownername,referencecode__icontains=referencecode,title__icontains=title,jobtype__icontains=jobtype,marklive__gte=after,marklive__lte=before)
    query0 = Q(marklive__gt=d1)

    query1 = Q(todate__gte=d1)

    query11 = Q(marklive__lte=d1)

    query2 = Q(todate__lt=d1)
    
    PendingJobList=jobs.objects.filter(query,query0)
    ActJobList=jobs.objects.filter(query,query1,query11)
    InactJobList=jobs.objects.filter(query,query2)


    return render_to_response('registration/search_all_jobs_result.html', {'ActJobList':ActJobList, 'InactJobList':InactJobList, 'PendingJobList':PendingJobList}, context_instance=RequestContext(request))


    #details = jobs.objects.filter(emp_id=request.user.id,ownername__icontains=ownername,referencecode__icontains=referencecode,title__icontains=title,jobtype__icontains=jobtype,marklive__gte=after,marklive__lte=before)
    
    #return render_to_response('registration/search_all_jobs_result.html', {'details': details},context_instance=RequestContext(request))


@login_required(login_url='/accounts/EmpReg/')
def Candidatefolder(request):
    d=dict()
    if request.method=='POST':
        form = RecruiterFolders(request.POST)

        if form.is_valid():
            foldername=request.POST.get('foldername')
            now=datetime.now()
            d=datetime(now.year, now.month, now.day)
            d1= d.strftime('%m-%d-%Y')
            s=RecruiterFolder(employer_id=request.user.id,foldername=foldername,lastupdate=d1)
            s.save()
            messages.success(request, 'Folder has been created successfully')
        else:
            messages.error(request,'Folder already exists')
        return HttpResponseRedirect('/accounts/JobsEmp/')
    else:
        """
        import json
        if 'param1' in request.GET:
            param1=request.GET['param1']
            valz= request.GET['param2']
            if param1=='foldername':
                already_exist=RecruiterFolder.objects.filter(foldername=valz,employer_id=request.user.id).exists()
            
            return HttpResponse(json.dumps({'already':already_exist,'fname':param1}), mimetype="application/json")
        """
        form = RecruiterFolders()
        job = jobs.objects.filter(emp_id=request.user.id).count()       
        folder=RecruiterFolder.objects.filter(employer_id=request.user.id)        
        for i in folder:
            i.fcount=SaveCandidateFolder.objects.foldercount_fname(request.user.id,i)

        return render(request,'registration/candidate_folder.html',{'folders':folder,'form':form })


@login_required(login_url='/accounts/EmpReg/')
def savedsearchresult(request):

    savesearch=RecSaveSearch.objects.filter(employer_id=request.user.id)

    return render_to_response('registration/saved_search_result.html',{'savesearch':savesearch },context_instance=RequestContext(request))


def BlogTopic(request):
    btopic=BlogTopics.objects.all()
    return render_to_response('registration/BlogTopics.html', {'btopic':btopic}, context_instance=RequestContext(request))

def blog(request,btid):
    btopicid=btid
    btop=BlogTopics.objects.filter(id=btopicid)    
    bass=Blog.objects.filter(btopic_id=btopicid)
    #commentcount=BComments.objects.filter(blog_id=btopicid)
    return render(request,'registration/blog.html', {'bass':bass, 'btop':btop})

def blogArticle(request,baid):
    if request.method=='POST':
        articleid=baid
        userid=request.POST.get('userid')
        articleid=request.POST.get('articleid')
        comments=request.POST.get('comment')
        c=BComments(user_id=userid,blog_id=articleid,comments=comments)
        c.save()
        messages.success(request, 'Your comments added successfully')
        return HttpResponseRedirect('/accounts/BlogArticle/%s/' %articleid)

    else:
        articleid=baid
        article=Blog.objects.filter(id=articleid)
        com=BComments.objects.filter(blog_id=articleid)

        #profilepic=[]
        #for i in com:

            #profilepic.append(js_details.objects.get(user_id=i.user_id))
        
        return render_to_response('registration/BlogArticle.html', {'article':article,'com':com},context_instance=RequestContext(request))


@login_required(login_url='/accounts/login/')
def blogpost(request):
    if request.method=='POST':
        userid=request.user.id
        user_id=userid
        btopic_id=request.POST.get("btopicid")
        btitle=request.POST.get("btitle")
        bimage=request.FILES.get("bimage")
        bcontent=request.POST.get("bcontent")
        
        article=Blog(user_id=user_id, btopic_id=btopic_id, btitle=btitle, bimage=bimage, bcontent=bcontent)
        article.save()
        messages.success(request, 'One article posted successfully')
        return HttpResponseRedirect('/accounts/BlogTopics/')
    else:
        btopics=BlogTopics.objects.all()
        return render_to_response('registration/BlogPost.html', {'btopics':btopics}, context_instance=RequestContext(request))


@login_required(login_url='/accounts/login/')
def MyInterviewZone(request):
    userid=request.user.id
    try:
        jsid=JSDetails.objects.get(user_id=userid)
        interview=Reschedule.objects.filter(JSId_id=jsid.id).select_related()
        status=Interview.objects.filter(JSId_id=jsid.id)
        return render_to_response('registration/MyInterviewZone.html',{'interview':interview,'status':status}, context_instance=
            RequestContext(request))
    except:
        return render_to_response('registration/MyInterviewZone.html', context_instance=
            RequestContext(request))


@login_required(login_url='/accounts/login/')
def RescheduleInterviewsJS(request,int_id):
    interview_id=int_id
    con=Reschedule.objects.get(interview_id=interview_id)
    jsconfirm=con.JSconfirmation
    empconfirm=con.Empconfirmation
    cancel=con.interview.Denied

    if cancel:

        msg="Not able to Reschedule once its Cancelled"
        userid=request.user.id
        jsid=JSDetails.objects.get(user_id=userid)
        interview=Reschedule.objects.filter(JSId_id=jsid.id).select_related()
        status=Interview.objects.filter(JSId_id=jsid.id)
        return render_to_response('registration/MyInterviewZone.html',{'interview':interview,'status':status,'msg':msg}, context_instance=RequestContext(request))


    elif jsconfirm:


        userid=request.user.id
        jsid=JSDetails.objects.get(user_id=userid)
        interview=Reschedule.objects.filter(JSId_id=jsid.id).select_related()
        status=Interview.objects.filter(JSId_id=jsid.id)
        return render_to_response('registration/MyInterviewZone.html',{'interview':interview,'status':status}, context_instance=RequestContext(request))
    else:

        interview=Reschedule.objects.filter(interview_id=interview_id).select_related()
        return render_to_response('registration/RescheduleInterviewsJS.html',{'interview':interview},context_instance=RequestContext(request))


@login_required(login_url='/accounts/EmpReg/')
def RescheduleInterviewsEmp(request,int_id):
    interview_id=int_id
    con=Reschedule.objects.get(interview_id=interview_id)
    jsconfirm=con.JSconfirmation
    empconfirm=con.Empconfirmation
    cancel=con.interview.Denied

    if cancel:

        msg="Not able to Reschedule once its Cancelled"
        interview=Reschedule.objects.filter(interview_id=interview_id).select_related()
        status=Interview.objects.filter(id=interview_id)
        return render_to_response('registration/EmpInterviewZone.html',{'interview':interview,'status':status,'msg':msg}, context_instance=RequestContext(request))


    elif empconfirm:
        msg="Not able to Reschedule once its confirmed"
        interview=Reschedule.objects.filter(interview_id=interview_id).select_related()
        status=Interview.objects.filter(id=interview_id)
        return render_to_response('registration/EmpInterviewZone.html',{'interview':interview,'status':status,'msg':msg}, context_instance=RequestContext(request))
    else:
        interview=Reschedule.objects.filter(interview_id=interview_id).select_related()
        
        return render_to_response('registration/RescheduleInterviewsEmp.html',{'interview':interview},context_instance=RequestContext(request))




@login_required(login_url='/accounts/login/')
def JSScheduleInterview(request):
    now=datetime.now()
    d1= now.strftime('%m-%d-%Y-%H:%M')
    
    if request.method=='POST':
        interviewid=request.POST.get('interviewid')
        redate=request.POST.get('scheduledate')
        retime=request.POST.get('scheduletime')

        edit=Reschedule.objects.get(interview_id=interviewid)

        if not edit.jsschedule_date1:
            edit.jsschedule_date1=redate
            edit.jsschedule_time1=retime
            edit.jsupdate1=d1
            edit.JSconfirmation=True;
            edit.Empconfirmation=False;
            edit.save()
            messages.success(request, 'Interview has been Reschedule successfully')
            return HttpResponseRedirect('/accounts/MyInterviewZone/')

        elif not edit.jsschedule_date2:
            edit.jsschedule_date2=redate
            edit.jsschedule_time2=retime
            edit.jsupdate2=d1
            edit.JSconfirmation=True;
            edit.Empconfirmation=False;
            edit.save()
            messages.success(request, 'Interview has been Reschedule successfully')
            return HttpResponseRedirect('/accounts/MyInterviewZone/')

        else:
            edit.jsschedule_date3=redate
            edit.jsschedule_time3=retime
            edit.jsupdate3=d1
            edit.JSconfirmation=True;
            edit.Empconfirmation=False;
            edit.save()
            messages.success(request, 'Interview has been Reschedule successfully')
            return HttpResponseRedirect('/accounts/MyInterviewZone/')

        

@login_required(login_url='/accounts/EmpReg/')
def EmpScheduleInterview(request):
    now=datetime.now()
    d1= now.strftime('%m-%d-%Y-%H:%M')
    
    if request.method=='POST':
        interviewid=request.POST.get('interviewid')
        redate=request.POST.get('scheduledate')
        retime=request.POST.get('scheduletime')

        edit=Reschedule.objects.get(interview_id=interviewid)

        if not edit.empschedule_date1:
            edit.empschedule_date1=redate
            edit.empschedule_time1=retime
            edit.empupdate1=d1
            edit.JSconfirmation=False;
            edit.Empconfirmation=True;
            edit.save()
            messages.success(request, 'Interview has been Reschedule successfully')
            return HttpResponseRedirect('/accounts/MyInterviewZoneEmp/')
        elif not edit.empschedule_date2:
            edit.empschedule_date2=redate
            edit.empschedule_time2=retime
            edit.empupdate2=d1
            edit.JSconfirmation=False;
            edit.Empconfirmation=True;
            edit.save()
            messages.success(request, 'Interview has been Reschedule successfully')
            return HttpResponseRedirect('/accounts/MyInterviewZoneEmp/')

        else:
            edit.empschedule_date3=redate
            edit.empschedule_time3=retime
            edit.empupdate3=d1
            edit.JSconfirmation=False;
            edit.Empconfirmation=True;
            edit.save()
            messages.success(request, 'Interview has been Reschedule successfully')
            return HttpResponseRedirect('/accounts/MyInterviewZoneEmp/')


@login_required(login_url='/accounts/EmpReg/')
def MyInterviewZoneEmp(request):
    empid=request.user.id
    interview=Reschedule.objects.filter(emp_id=empid).select_related()
    return render_to_response('registration/EmpInterviewZone.html',{'interview':interview},context_instance=RequestContext(request))

@login_required(login_url='/accounts/login/')
def InterviewConfirmJS(request,int_id):
    interviewid=int_id
    inter=Reschedule.objects.get(interview_id=interviewid)
    inter.JSconfirmation=True
    inter.save()
    messages.success(request, 'Interview has been confirmed successfully')
    return HttpResponseRedirect('/accounts/MyInterviewZone/')

@login_required(login_url='/accounts/EmpReg/')
def InterviewConfirmEmp(request,int_id):
    interviewid=int_id
    inter=Reschedule.objects.get(interview_id=interviewid)
    inter.Empconfirmation=True
    inter.save()
    messages.success(request, 'Interview has been confirmed successfully')
    return HttpResponseRedirect('/accounts/MyInterviewZoneEmp/')

@login_required(login_url='/accounts/login/')
def CancelInterviewJS(request):
    if request.method=="POST":
        interviewid=request.POST.get('intid')
        userid=request.POST.get('userid')
        js=JSDetails.objects.get(user_id=userid)
        jsid=js.id
        inter=Interview.objects.get(id=interviewid,JSId_id=jsid)
        inter.Denied=True
        inter.save()
        messages.success(request, 'Interview has been Cancelled successfully')
        return HttpResponseRedirect('/accounts/MyInterviewZone/')

@login_required(login_url='/accounts/EmpReg/')
def CancelInterviewEmp(request):
    if request.method=="POST":
        interviewid=request.POST.get('intid')
        empid=request.POST.get('empid')
        inter=Interview.objects.get(id=interviewid,emp_id=empid)
        inter.Denied=True
        inter.save()
        messages.success(request, 'Interview has been Cancelled successfully')
        return HttpResponseRedirect('/accounts/MyInterviewZoneEmp/')
@login_required(login_url='/accounts/EmpReg/')
def EmpInterviewCofirmPage(request):
    result=Interview.objects.filter(Q(emp_id=request.user.id) & ~Q(interviewpassed=True) & ~Q(interviewfailed=True) & ~Q(Denied=True))
    confirmresult=[]
    for res in result:
        eid=res.emp_id
        jid=res.Job_id
        jsid=res.JSId_id
        inid=res.id
        for con in Reschedule.objects.filter( Q(id=inid),Q(JSconfirmation=True),Q(Empconfirmation=True)):
            confirmresult.append(con)        
        #confirm=confirmresult
    return render(request,'registration/EmpInterviewCofirmPage.html',{'confirm':confirmresult})
@login_required(login_url='/accounts/EmpReg/')
def EmpInterviewCancelPage(request):
    query=Q(emp_id=request.user.id) & Q(Denied=True)
    cancel=Interview.objects.filter(query)
    return render(request,'registration/EmpInterviewCancelPage.html',{'cancel':cancel})
@login_required(login_url='/accounts/EmpReg/')
def EmpInterviewSuccessPage(request):
    query=Q(emp_id=request.user.id) & Q(interviewpassed=True)
    success=Interview.objects.filter(query)
    return render(request,'registration/EmpInterviewSuccessPage.html',{'success':success})

@login_required(login_url='/accounts/EmpReg/')
def EmpInterviewFailPage(request):
    query=Q(emp_id=request.user.id) & Q(interviewfailed=True)
    fail=Interview.objects.filter(query)
    return render(request,'registration/EmpInterviewFailPage.html',{'fail':fail})
@login_required(login_url='/accounts/login/')
def JSInterviewCofirmPage(request):
    try:
        js=JSDetails.objects.get(user_id=request.user.id)
        jsid=js.id
    
        result=Interview.objects.filter(Q(JSId_id=jsid) & ~Q(interviewpassed=True) & ~Q(interviewfailed=True) & ~Q(Denied=True))
        confirmresult=[]
        for res in result:
            eid=res.emp_id
            jid=res.Job_id
            jsid=res.JSId_id
            inid=res.id
            for con in Reschedule.objects.filter( Q(id=inid) & Q(JSconfirmation=True) & Q(Empconfirmation=True)):
                confirmresult.append(con)
            confirm=confirmresult
        return render(request,'registration/JSInterviewCofirmPage.html',{'confirm':confirm})
    except:
        return render(request,'registration/JSInterviewCofirmPage.html')

@login_required(login_url='/accounts/login/')
def JSInterviewSuccessPage(request):
    if JSDetails.objects.filter(user_id=request.user.id):
        js=JSDetails.objects.get(user_id=request.user.id)
        jsid=js.id
        success=Interview.objects.filter(Q(JSId_id=jsid) & Q(interviewpassed=True))
        return render(request,'registration/JSInterviewSuccessPage.html',{'success':success})
    else:
        return render(request,'registration/JSInterviewSuccessPage.html')

@login_required(login_url='/accounts/login/')
def JSInterviewFailPage(request):
    if JSDetails.objects.filter(user_id=request.user.id):
        js=JSDetails.objects.get(user_id=request.user.id)
        jsid=js.id
        query=Q(JSId_id=jsid) & Q(interviewfailed=True)
        fail=Interview.objects.filter(query)
        return render(request,'registration/JSInterviewFailPage.html',{'fail':fail})
    else:
        return render(request,'registration/JSInterviewFailPage.html')

@login_required(login_url='/accounts/login/')
def JSInterviewCancelPage(request):
    if JSDetails.objects.filter(user_id=request.user.id):
        js=JSDetails.objects.get(user_id=request.user.id)
        jsid=js.id
        query=Q(JSId_id=jsid) & Q(Denied=True)
        cancel=Interview.objects.filter(query)
        return render(request,'registration/JSInterviewCancelPage.html',{'cancel':cancel})
    else:
        return render(request,'registration/JSInterviewCancelPage.html')

@login_required(login_url='/accounts/EmpReg/')
def RoundsEmp(request,int_id):
    interviewid=int_id
    inter=Interview.objects.filter(id=interviewid)
    inter1=Interview.objects.get(id=interviewid)
    #empid=inter.emp_id
    #jsid=inter.JSId_id
    #jobid=inter.Job_id
    roundss=inter1.rounds
    #jobseeker=JSDetails.objects.filter(id=jsid)
    #employer=User.objects.filter(id=empid)
    #job=jobs.objects.filter(id=jobid)
    roundcount=InterviewRounds.objects.filter(interview_id=interviewid).count()

    remcount = int(roundss)-roundcount
    roundresults=InterviewRounds.objects.filter(interview_id=interviewid)
    return render(request,'registration/RoundsEmp.html', {'inter':inter,'roundcount':roundcount,'roundresults':roundresults,'remcount':remcount})




@login_required(login_url='/accounts/login/')
def RoundsJS(request,int_id):
    interviewid=int_id
    interviewid=int_id
    inter=Interview.objects.filter(id=interviewid)
    inter1=Interview.objects.get(id=interviewid)
    roundss=inter1.rounds
    roundcount=InterviewRounds.objects.filter(interview_id=interviewid).count()
    outof= roundcount*10

    roundresults=InterviewRounds.objects.filter(interview_id=interviewid)
    return render(request,'registration/RoundsJS.html',{'inter':inter,'roundcount':roundcount,'roundresults':roundresults,'outof':outof})



@login_required(login_url='/accounts/EmpReg/')
def RoundResult(request):
    if request.method=='POST':
        empid=request.POST.get('empid')
        jsid=request.POST.get('jsid')
        jobid=request.POST.get('jobid')
        interviewid=request.POST.get('interviewid')
        roundno=request.POST.get('roundno')
        score=request.POST.get('score')
        interviewby=request.POST.get('interviewby')
        interviewdate=request.POST.get('interviewdate')
        description=request.POST.get('description')
        nextround=request.POST.get('nextround')
        status=request.POST.get('status')
        
        if status=="False":
            result =  Interview.objects.get(emp=empid,JSId=jsid,Job=jobid,Denied=False) 
            result.interviewfailed=True;
            result.save()
            result=InterviewRounds(interview_id=interviewid,emp_id=empid,JSId_id=jsid,Job_id=jobid,roundno=roundno,score=score,interviewby=interviewby,interviewdate=interviewdate,tips=description,nextrounddate=nextround,status=False)
        else:
            result =  Interview.objects.get(emp=empid,JSId=jsid,Job=jobid,Denied=False)
            if result.rounds==roundno:
                result.interviewpassed=True
                result.save()

            result=InterviewRounds(interview_id=interviewid,emp_id=empid,JSId_id=jsid,Job_id=jobid,roundno=roundno,score=score,interviewby=interviewby,interviewdate=interviewdate,tips=description,nextrounddate=nextround,status=True)
        result.save()

        return HttpResponseRedirect('/accounts/RoundsEmp/%s/' %interviewid)


#------------ 1st JUNE ------------------------

def doc(request):
  
    res=JSResumeActive.objects.get(user_id=request.user.id)
    resid=res.resumeActive_id
    resume=JSResume.objects.get(id=resid)
    resumefile=resume.resumeFile

    #call(["unoconv","-f","html","-o",settings.CURRENT_DIR+"/tagging/templates/documents",settings.CURRENT_DIR+"/media/"+str(resumefile)])

    name, fileExtension = os.path.splitext(str(resumefile))
    return render(request,'%s.html'%name)
   

@login_required(login_url='/accounts/EmpReg/')
def ReceivedApplication(request):
    try:
        received=JSAppliedJobs.objects.filter(emp_id=request.user.id,empappdel=True)
        employers=jobs.objects.filter(emp_id=request.user.id)
        return render_to_response('registration/ReceivedApplication.html',{'received':received,'employers':employers},context_instance=RequestContext(request))
    except:
        return render_to_response('registration/ReceivedApplication.html',context_instance=RequestContext(request))


@login_required(login_url='/accounts/EmpReg/')
def DeleteReceivedApplication(request):
    if request.method=='POST':
        empid=request.POST.get('empid')
        for appid in request.POST.get('recappid').split(','):
            
            recapp=JSAppliedJobs.objects.get(id=appid,emp_id=empid)
            if not recapp.jsappdel:
                recapp.delete()
            else:
                recapp.empappdel=False
                recapp.save()
        messages.success(request, 'Application deleted successfully')
        return HttpResponseRedirect('/accounts/ReceivedApplication/')


def MyJobs(request):
    now=datetime.now()
    d=datetime(now.year, now.month, now.day)
    d1= d.strftime('%m-%d-%Y')
    jsinfo = JSDetails.objects.filter(user_id=request.user.id)

    if jsinfo:
        if JSSkills.objects.filter(user_id=request.user.id):
            skilcount = JSSkills.objects.filter(user_id=request.user.id).count()
            if skilcount == 1:
                skil = JSSkills.objects.get(user_id=request.user.id)
                if skil.skill:
                        details=jobs.objects.filter(Q(employerkeyskills__keyskills__icontains=skil.skill))

                        return render_to_response('registration/MyJobs.html',{'jsinfo':jsinfo,'details': details},context_instance=RequestContext(request))
                else:
                    return render_to_response('registration/MyJobs.html',context_instance=RequestContext(request))
            else:
                skil = JSSkills.objects.filter(user_id=request.user.id)
                list_result=[]
                for search in skil:
                    for res in jobs.objects.filter(Q(employerkeyskills__keyskills__icontains=search.skill)):
                        if not res in list_result:
                            list_result.append(res)
                details=list_result
                return render_to_response('registration/MyJobs.html',{'jsinfo':jsinfo,'details': details},context_instance=RequestContext(request))
        else:
            return render_to_response('registration/MyJobs.html',context_instance=RequestContext(request))
    else:
            return render_to_response('registration/MyJobs.html',context_instance=RequestContext(request))


@login_required(login_url='/accounts/login/')
def myapplications(request):
    if JSDetails.objects.filter(user_id=request.user.id):
        appjob=JSAppliedJobs.objects.filter(JS_id=request.user.jsdetails.id)
        return render(request,'registration/application_history.html',{'appjob':appjob})
    else:
        messages.warning(request, 'Please fill your details first !.')
        return HttpResponseRedirect('/accounts/ProfileDetails/')

@login_required(login_url='/accounts/login/')
def JobApplySuccess(request):
    userid=request.user.id
    now=datetime.now()
    d=datetime(now.year, now.month, now.day)
    d1= d.strftime('%m-%d-%Y')
    try:
        js = JSDetails.objects.get(user_id=userid)
        jsid = js.id

        appjob=JSAppliedJobs.objects.filter(JS_id=jsid).latest('applieddate')
        jsappjobid = appjob.Job.id
        jsappjobtitle = appjob.Job.title
        jsappjobloc = appjob.Job.state

        alljobid = jobs.objects.filter(title=jsappjobtitle)

        result=[]
        for a in alljobid:
            jid = a.id
            for res in JSAppliedJobs.objects.filter(Q(Job_id=jid),~Q(Job_id=jsappjobid),~Q(JS_id=jsid)):
                result.append(res)

        allappjob=result
        return render_to_response('registration/JobApplySuccess.html',{'allappjob':allappjob}, context_instance=RequestContext(request))
    except:
        return render_to_response('registration/JobApplySuccess.html', context_instance=RequestContext(request))


@login_required(login_url='/accounts/login/')
def delete_myapplications(request):
    if request.method=="POST":
        for sntapp in request.POST.get('sntappid').split(','):
            appdel=JSAppliedJobs.objects.get(id=sntapp)

            if not appdel.empappdel:
                appdel.delete()
            else:
                appdel.jsappdel=False
                appdel.save()
        messages.success(request, 'Sent application deleted successfully')
        return HttpResponseRedirect('/accounts/MyApplications/')


@login_required(login_url='/accounts/login/')
def MySearchAgents(request):
    savesearch=JSsavesearch.objects.filter(user_id=request.user.id)
    return render_to_response('registration/MySearchAgents.html',{'savesearch':savesearch},context_instance=RequestContext(request))


@login_required(login_url='/accounts/login/')
def DeleteAllJSSaveJob(request):
    if request.method=="POST":
        userid=request.POST.get('userid')
        for agentid in request.POST.get('saveresultid').split(','):
            agent=JSsavesearch.objects.get(id=agentid)
            agent.delete()
        messages.success(request, 'Your search agent has been deleted successfully')
        return HttpResponseRedirect('/accounts/MyApplications/')


@login_required(login_url='/accounts/login/')
def EditJSSaveJob(request):
    if request.method=="POST":
        userid=request.POST.get('userid')
        agentid=request.POST.get('saveresultid')
        agentname=request.POST.get('editsavejob')
        agent=JSsavesearch.objects.get(id=agentid,user_id=userid)
        agent.searchname=agentname
        agent.save()
        messages.success(request, 'Your search agent has been edited successfully')
        return HttpResponseRedirect('/accounts/MyApplications/')


@login_required(login_url='/accounts/login/')
def NewProfilePictures(request):
    if request.method=="POST":
        userid=request.POST.get('userid')
        upimages=request.FILES.get('uplaodimage')
        JSDetails(user_id=userid,post_date=datetime.now(),update_date=datetime.now()).save()
        JS=JSDetails.objects.get(user_id=userid)
        JS_id=JS.id
        JSPersonal(user_id=userid,JS_id=JS_id).save()
        JSQualification(user_id=userid,JS_id=JS_id).save()
        JSCertificate(user_id=userid,JS_id=JS_id).save()
        JSProfileSummary(user_id=userid,JS_id=JS_id,profile_pic=upimages).save()
        JSSkills(user_id=userid,JS_id=JS_id).save()
        JSEmployerDetails(user_id=userid,JS_id=JS_id).save()
        JSProjectDetails(user_id=userid,JS_id=JS_id).save()
        JSLanguage(user_id=userid,JS_id=JS_id).save()
        JSsecurity(user_id=userid,JS_id=JS_id).save()
        JSDetailOther(user_id=userid,JS_id=JS_id).save()
        JSResume(user_id=userid,JS_id=JS_id).save()
        JSTextResume(user_id=userid,JS_id=JS_id).save()
        JSVideoResume(user_id=userid,JS_id=JS_id).save()
        messages.success(request, 'Profile has been edited successfully')
        return HttpResponseRedirect('/accounts/Profile/')

from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
from django.core.urlresolvers import reverse

def paypal(request):
# What you want the button to do.
    paypal_dict = {
    "business": settings.PAYPAL_RECEIVER_EMAIL,
    "amount": "0.00",
    "item_name": "name of the item",
    "invoice": "unique-invoice-id",
    "notify_url": "%s%s" % (settings.SITE_NAME, reverse('paypal-ipn')),
    "return_url": "http://192.168.0.33:2003/accounts/EmpSelectedPack/",
    "cancel_return": "http://192.168.0.33:2003/accounts/EmpPackname/",
    }
    # Create the instance.
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {"form": form.sandbox()}
    return render_to_response('registration/paypal.html', context)
    # paypal.html
   


def emp_packname(request):
    empavailpack = emp_avail_packs.objects.all()
    return render(request,'registration/EmpPackname.html',{'empavailpack':empavailpack})


@login_required(login_url='/accounts/EmpReg/')
def emp_pack_subscription(request,pck_id):

    if request.method=='POST':
        pckid=pck_id
        pack = emp_avail_packs.objects.get(id=pckid)

        now=datetime.now()
        d=datetime(now.year, now.month, now.day)
        d1= d.strftime('%m-%d-%Y')
        da=d+timedelta(int(pack.pack_duration))
        d2= da.strftime('%m-%d-%Y')

        employer_id=request.POST.get('employer_id')
        pack_id=request.POST.get('pckid')
        quantity=request.POST.get('quantity')
        spack_jobpost=request.POST.get('spack_jobpost')
        spack_resume=request.POST.get('spack_resume')
        spack_cost=request.POST.get('spack_cost')

        pack_activate=d1
        pack_expire=d2

        a=emp_selected_packs(employer_id=employer_id,pack_id=pack_id,quantity=quantity,spack_jobpost=spack_jobpost,spack_resume=spack_resume,spack_cost=spack_cost,pack_activate=pack_activate,pack_expire=pack_expire)
        a.save()
        emppack=emp_selected_packs_add.objects.filter(employer_id=request.user.id).count()
        if emppack is 0:
            ea=emp_selected_packs_add(employer_id=employer_id,pack_id=pack_id,spack_jobpost=spack_jobpost,spack_resume=spack_resume,pack_activate=pack_activate,pack_expire=pack_expire)
            ea.save()

        else:
            try:
                emp=emp_selected_packs_add.objects.get(employer_id=request.user.id,pack_id=pack_id)

                jobpost = emp.spack_jobpost+int(spack_jobpost)
                
                resview = emp.spack_resume+int(spack_resume)

                emp.spack_jobpost=jobpost
                emp.spack_resume=resview
                emp.pack_activate=pack_activate
                emp.pack_expire=pack_expire
                emp.save()
                
            except:
                ea=emp_selected_packs_add(employer_id=employer_id,pack_id=pack_id,spack_jobpost=spack_jobpost,spack_resume=spack_resume,pack_activate=pack_activate,pack_expire=pack_expire)
                ea.save()

        packid=a.id
        return HttpResponseRedirect('/accounts/EmpSubConf/%s/'% packid)
    else:
        pckid=pck_id
        pack = emp_avail_packs.objects.filter(id=pckid)

        return render_to_response('registration/EmpPack.html', {'pack':pack}, context_instance=RequestContext(request) )


@login_required(login_url='/accounts/EmpReg/')
def EmpSubConf(request,pack_id):
    packid=pack_id
    pack= emp_selected_packs.objects.filter(id=packid,employer_id=request.user.id)
   
    paypal_dict = {
    "business": settings.PAYPAL_RECEIVER_EMAIL,
    "amount": "pack.spack_cost",
    "item_name": "pack.emp_avail_packs.pack_name",
    "invoice": "unique-invoice-id",
    "notify_url": "%s%s" % (settings.SITE_NAME, reverse('paypal-ipn')),
    "return_url": "http://192.168.0.6/accounts/EmpSelectedPack/",
    "cancel_return": "http://192.168.0.6/accounts/EmpPackname/",
    }
    # Create the instance.
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {"form": form.sandbox(),'pack':pack}
    return render_to_response('registration/paypal.html', context, context_instance=RequestContext(request) )



@login_required(login_url='/accounts/EmpReg/')
def emp_selected_pack(request):
    subscribed=emp_subscribed_packs.objects.filter(employer_id=request.user.id).order_by('-pack_activate')
    subscribed_packcount=emp_subscribed_packs.objects.filter(employer_id=request.user.id).count()
    remjobcnt=0
    rescnt=0
    totactjob=0
    for a in emp_subscribed_packs.objects.filter(employer_id=request.user.id):
        for count in emppack_activation.objects.filter(subscribed_pack_id=a.id):
            remjobcnt+=count.totaljobpost
            rescnt+=count.totalresume
            totactjob+=count.total_activated_job

    totviewres=profileviews.objects.filter(employer_id=request.user.id).count()
    remrescnt=rescnt-totviewres
    return render(request,'registration/EmpSelPack.html',{'subscribed':subscribed,'subscribed_packcount':subscribed_packcount,'remjobcnt':remjobcnt,'remrescnt':remrescnt,'totactjob':totactjob,'totviewres':totviewres})


@login_required(login_url='/accounts/EmpReg/')
def emp_selected_pack_add(request):
    emppack=emp_selected_packs.objects.filter(employer_id=request.user.id).count()
    empselpack= emp_selected_packs.objects.filter(employer_id=request.user.id).order_by('-pack_activate')


    now=datetime.now()
    d=datetime(now.year, now.month, now.day)
    d1= d.strftime('%m-%d-%Y')

    query = Q(employer_id=request.user.id) & Q(pack_expire__gte=d1)

    msgtime=emp_selected_packs.objects.filter(query).count()
    

    msg1="Totally You have allow to Post 5 Jobs."
    empsavesearch=RecSaveSearch.objects.filter(employer_id=request.user.id)
    sacount=RecSaveSearch.objects.filter(employer_id=request.user.id).count()
    msg = 5-sacount

    msgpack="You bave subscribed %s packs."%emppack
    job = jobs.objects.filter(emp_id=request.user.id).count()
    folder=RecruiterFolder.objects.filter(employer_id=request.user.id)
    for i in folder:
        i.fcount=SaveCandidateFolder.objects.foldercount_fname(request.user.id,i)
    remaining = 5-job
    msg2 = "You have posted %s Jobs."% job
    msg3 = "At Maximum you have %s Jobs Post Remaining"% remaining
    return render_to_response('registration/EmpSelPack.html',{'empselpack':empselpack,'msgtime':msgtime,'msgpack':msgpack,'msg1': msg1, 'msg2':msg2, 'msg3':msg3,'folders':folder,'savesearch':empsavesearch },context_instance=RequestContext(request))


@login_required(login_url='/accounts/EmpReg/')
def editsearchagent(request):
    if request.method=='POST':
        empid=request.POST.get('empid')
        saveid=request.POST.get('saveresultid')
        savename=request.POST.get('editsavejob')
        editsave=RecSaveSearch.objects.get(id=saveid,employer_id=empid)
        editsave.searchname=savename
        editsave.save()
        messages.success(request, 'Search agent has been edited successfully')
        return HttpResponseRedirect("/accounts/JobsEmp/")


@login_required(login_url='/accounts/EmpReg/')
def DeleteRecFolder(request):
    if request.method=='POST':
        empid=request.POST.get('empid')
        for sa in request.POST.get('folderid').split(','):
            recdet=RecruiterFolder.objects.get(id=sa,employer_id=empid)
            recdet.delete()
        messages.success(request, 'Folder has been deleted successfully')
        return HttpResponseRedirect('/accounts/JobsEmp/')

@login_required(login_url='/accounts/EmpReg/')
def EditRecFolder(request):
    if request.method=='POST':
        empid=request.POST.get('empid')
        folderid=request.POST.get('folderid')
        foldername=request.POST.get('foldername')
        editsave=RecruiterFolder.objects.get(id=folderid,employer_id=empid)
        editsave.foldername=foldername
        editsave.save()
        messages.success(request, 'Folder has been edited successfully')
        return HttpResponseRedirect("/accounts/JobsEmp/")


@login_required(login_url='/accounts/EmpReg/')
def DelJSInsideFolder(request):
    if request.method=='POST':
        empid=request.POST.get('empid')
        fid = request.POST.get('fid')
        for scid in request.POST.get('savecandidateid').split(','):
            recdet=SaveCandidateFolder.objects.get(id=scid,employer_id=empid)
            recdet.delete()

        return HttpResponseRedirect('/accounts/RecruiterFolder/%s/'% fid)


def careerplus(request):
    jsavailpack = jspacks.objects.all()
    return render(request,'registration/career_service.html',{'jsavailpack':jsavailpack})

def resumebooster(request):
    return render(request,'registration/resume_high_pitched.html')

def resumeplus(request):
    return render(request,'registration/resume_plus.html')

@login_required(login_url='/accounts/login/')
def ordersummary(request,pck_id):
    if request.method=='POST':
        pckid=pck_id
        pack = jspacks.objects.get(id=pckid)

        now=datetime.now()
        d=datetime(now.year, now.month, now.day)
        d1= d.strftime('%m-%d-%Y')
        da=d+timedelta(int(pack.pack_duration))
        d2= da.strftime('%m-%d-%Y')

        jobseeker_id=request.POST.get('jobseeker_id')
        pack_id=request.POST.get('pckid')
        quantity=request.POST.get('quantity')
        spack_cost=request.POST.get('spack_cost')

        pack_activate=d1
        pack_expire=d2
        a=js_selected_packs(jobseeker_id=jobseeker_id,pack_id=pack_id,quantity=quantity,spack_cost=spack_cost,pack_activate=pack_activate,pack_expire=pack_expire)
        a.save()
        return HttpResponseRedirect('/accounts/Profile/')

    else:
        pckid=pck_id
        pack = jspacks.objects.filter(id=pckid)

        return render(request,'registration/order_summary.html', {'pack':pack})



def emp_packname(request):
    empavailpack = emppacks.objects.all()
    return render(request,'registration/EmpPackname.html',{'empavailpack':empavailpack})



@login_required(login_url='/accounts/EmpReg/')
def emp_pack_subscription(request,pck_id):

    if request.method=='POST':
        pckid=pck_id
        pack = emp_avail_packs.objects.get(id=pckid)

        now=datetime.now()
        d=datetime(now.year, now.month, now.day)
        d1= d.strftime('%m-%d-%Y')
        da=d+timedelta(int(pack.pack_duration))
        d2= da.strftime('%m-%d-%Y')

        employer_id=request.POST.get('employer_id')
        pack_id=request.POST.get('pckid')
        quantity=request.POST.get('quantity')
        spack_jobpost=request.POST.get('spack_jobpost')
        spack_resume=request.POST.get('spack_resume')
        spack_cost=request.POST.get('spack_cost')

        pack_activate=d1
        pack_expire=d2

        a=emp_selected_packs(employer_id=employer_id,pack_id=pack_id,quantity=quantity,spack_jobpost=spack_jobpost,spack_resume=spack_resume,spack_cost=spack_cost,pack_activate=pack_activate,pack_expire=pack_expire)
        a.save()
        emppack=emp_selected_packs_add.objects.filter(employer_id=request.user.id).count()
        if emppack is 0:
            ea=emp_selected_packs_add(employer_id=employer_id,pack_id=pack_id,spack_jobpost=spack_jobpost,spack_resume=spack_resume,pack_activate=pack_activate,pack_expire=pack_expire)
            ea.save()

        else:
            try:
                emp=emp_selected_packs_add.objects.get(employer_id=request.user.id,pack_id=pack_id)

                jobpost = emp.spack_jobpost+int(spack_jobpost)
                
                resview = emp.spack_resume+int(spack_resume)

                emp.spack_jobpost=jobpost
                emp.spack_resume=resview
                emp.pack_activate=pack_activate
                emp.pack_expire=pack_expire
                emp.save()
                
            except:
                ea=emp_selected_packs_add(employer_id=employer_id,pack_id=pack_id,spack_jobpost=spack_jobpost,spack_resume=spack_resume,pack_activate=pack_activate,pack_expire=pack_expire)
                ea.save()

        packid=a.id
        return HttpResponseRedirect('/accounts/EmpSubConf/%s/'% packid)
    else:
        pckid=pck_id
        pack = emp_avail_packs.objects.filter(id=pckid)

        return render(request,'registration/EmpPack.html', {'pack':pack})

def ForgotPassword(request):
    if request.method=="POST":
        ut=request.POST.get('usertype')
        em=request.POST.get('email')
        qt=request.POST.get('question')
        ans=request.POST.get('answer')
        query=Q(usertype=ut) & Q(email=em) & Q(securityquestions__question=qt) & Q(securityquestions__answer=ans)
        if User.objects.filter(query):
            salt = sha.new(str(random.random())).hexdigest()[:5]
            activation_key = sha.new(salt+em).hexdigest()
            current_domain = Site.objects.get_current().domain
            subject="[%s] : Password Reset"% current_domain
            message_template = loader.get_template('registration/passwordreset_activationmail.html')
            message_context = Context({'site_url': 'http://%s/' % current_domain,'activation_key': activation_key})
            message = message_template.render(message_context)
            msg=EmailMultiAlternatives(subject,message,settings.DEFAULT_FROM_EMAIL,[em])
            msg.attach_alternative(message, "text/html")
            msg.send()
            usr=User.objects.get(query)
            userid=usr.id
            activationcode.objects.filter(user_id=userid).delete()
            activationcode(user_id=userid,key=activation_key).save()
            messages.success(request, 'Thank you for your request. Activation link for reset password has been sent to your mail')
            return HttpResponseRedirect('/accounts/login/')
        else:
            messages.error(request, 'The details are not matched! Please give valid details')
            return HttpResponseRedirect('/accounts/ForgotPassword/')
    else:
        return render(request,'registration/ForgotPassword.html')

def PasswordResetActivate(request, activation_key):
    activation_key = activation_key.lower()
    current_domain = Site.objects.get_current().domain
    if activationcode.objects.filter(key=activation_key):
        actdate=activationcode.objects.get(key=activation_key)
        key_generated=actdate.key_date
        userid=actdate.user_id
        delta = timedelta(days=1)
        target_date = key_generated + delta
        if target_date <= datetime.now():
            messages.error(request, 'Your Password activation key got expired. Please once again submit the details')
            return HttpResponseRedirect("/accounts/ForgotPasswordEmp/")
        else:
            return render(request,'registration/SetNewPassword.html',{'userid':userid})

        
    else:
        return HttpResponse("<html><body onload='error()'><script type='text/javascript'>function error(){alert('Your Password activation key is invalid / expired / already used. Please submit the details again.');window.location='http://%s';}</script></body></html>"%current_domain)

def SetNewPassword(request):
    if request.method=='POST':
        pwd=request.POST.get('newpassword')
        userid=request.POST.get('userid')
        if userid:
            usr=User.objects.get(id=userid)
            usertype=usr.usertype
            usr.set_password(pwd)
            usr.save()
            activationcode.objects.filter(user_id=userid).delete()
            messages.success(request, 'Your Password has been reset successfully. Continue to login. ')
            if usertype=='jobseeker':
                return HttpResponseRedirect("/accounts/login/")
            if usertype=='employer':
                return HttpResponseRedirect("/accounts/EmpReg/")
        else:
            messages.error(request, 'Invalid user')
            return HttpResponseRedirect("/accounts/ForgotPasswordEmp/")
    else:
        return render(request,'registration/SetNewPassword.html')


def ForgotUsername(request):
    if request.method=="POST":
        ut=request.POST.get('usertype')
        em=request.POST.get('email')
        qt=request.POST.get('question1')
        ans=request.POST.get('answer1')
        query=Q(usertype=ut) & Q(email=em) & Q(securityquestions__question=qt) & Q(securityquestions__answer=ans)
        if User.objects.filter(query):
            un=User.objects.get(query)
            uname=un.username
            current_domain = Site.objects.get_current().domain
            subject="[%s] :Username for logging Itechtalents"% current_domain
            message_template = loader.get_template('registration/passwordreset.html')
            message_context = Context({'current_domain': current_domain,'un':uname})
            message = message_template.render(message_context)
            msg=EmailMultiAlternatives(subject,message,settings.DEFAULT_FROM_EMAIL,[em])
            msg.attach_alternative(message, "text/html")
            msg.send()
            messages.success(request, 'Thank you for your request. Username has been sent to your mail')
            return HttpResponseRedirect('/accounts/login/')

        else:
            messages.error(request, 'The details are not matched! Please give valid details')
            return HttpResponseRedirect('/accounts/ForgotPassword/')
    else:
        return HttpResponseRedirect('/accounts/ForgotPassword/')


def ForgotPasswordEmp(request):
    if request.method=="POST":
        ut=request.POST.get('usertype')
        em=request.POST.get('email')
        qt=request.POST.get('question')
        ans=request.POST.get('answer')
        query=Q(usertype=ut) & Q(email=em) & Q(securityquestions__question=qt) & Q(securityquestions__answer=ans)
        if User.objects.filter(query):
            salt = sha.new(str(random.random())).hexdigest()[:5]
            activation_key = sha.new(salt+em).hexdigest()
            current_domain = Site.objects.get_current().domain
            subject="[%s] : Password Reset"% current_domain

            message_template = loader.get_template('registration/passwordreset_activationmail.html')
            message_context = Context({'site_url': 'http://%s/' % current_domain,'activation_key': activation_key})
            message = message_template.render(message_context)
            msg=EmailMultiAlternatives(subject,message,settings.DEFAULT_FROM_EMAIL,[em])
            msg.attach_alternative(message, "text/html")
            msg.send()
            usr=User.objects.get(query)
            userid=usr.id
            activationcode.objects.filter(user_id=userid).delete()
            activationcode(user_id=userid,key=activation_key).save()
            messages.success(request, 'Thank you for your request. Password activation link has been sent to your mail')
            return HttpResponseRedirect('/accounts/EmpReg/')
        else:
            messages.error(request, 'The details are not matched! Please give valid details')
            return HttpResponseRedirect('/accounts/ForgotPasswordEmp/')
    else:
        return render(request,'registration/ForgotPasswordEmp.html')

def ForgotUsernameEmp(request):
    if request.method=="POST":
        ut=request.POST.get('usertype')
        em=request.POST.get('email1')
        qt=request.POST.get('question1')
        ans=request.POST.get('answer1')
        query=Q(usertype=ut) & Q(email=em) & Q(securityquestions__question=qt) & Q(securityquestions__answer=ans)
        if User.objects.filter(query):
            un=User.objects.get(query)
            uname=un.username
            current_domain = Site.objects.get_current().domain
            subject="[%s] :Username for logging Itechtalents"% current_domain
            message_template = loader.get_template('registration/passwordreset.html')
            message_context = Context({'current_domain': current_domain,'un':uname})
            message = message_template.render(message_context)
            msg=EmailMultiAlternatives(subject,message,settings.DEFAULT_FROM_EMAIL,[em])
            msg.attach_alternative(message, "text/html")
            msg.send()
            messages.success(request, 'Thank you for your request. Password has been sent to your mail')
            return HttpResponseRedirect('/accounts/EmpReg/')

        else:
            messages.error(request, 'The details are not matched! Please give valid details')
            return HttpResponseRedirect('/accounts/ForgotPasswordEmp/')
    else:
        return HttpResponseRedirect('/accounts/ForgotPasswordEmp/')
def is_jobseeker(user):
    try:
        user.usertype
        if user.usertype=='jobseeker':return True
        else:return False
    except:return False
@user_passes_test(is_jobseeker,login_url='/accounts/login/')
def profile(request):
    userid=request.user.id
    progress=0
    if JSDetails.objects.filter(user_id=userid):
        jsinfo = JSDetails.objects.filter(user_id=userid)
        personal=JSPersonal.objects.filter(user_id=userid)
        certificates=JSCertificate.objects.filter(user_id=userid)
        jsemployer=JSEmployerDetails.objects.filter(user_id=userid)
        jssecret=JSsecurity.objects.filter(user_id=userid)
        jslang=JSLanguage.objects.filter(user_id=userid)
        jsresume=JSResume.objects.filter(user_id=userid)
        jstext=JSTextResume.objects.filter(user_id=userid)
        jsvideo=JSVideoResume.objects.filter(user_id=userid)
        education=JSQualification.objects.filter(user_id=userid)
        if education:
            for a in education:
                if a.degree:progress=progress+5
                break
        profilesummary=JSProfileSummary.objects.filter(user_id=userid)
        if profilesummary:
            for a in profilesummary:
                if a.profile_summary:progress=progress+5
        skills=JSSkills.objects.filter(user_id=userid)
        if skills:
            for a in skills:
                if a.skill:progress=progress+5
                break
        projectdetails=JSProjectDetails.objects.filter(user_id=userid)
        if projectdetails:
            for a in projectdetails:
                if a.project_title:progress=progress+5
                break
        other=JSDetailOther.objects.filter(user_id=userid)
        if other:
            for a in other:
                if a.emptype:progress=progress+5
                if a.workpermit:progress=progress+5

        textresume=JSTextResume.objects.get(user_id=userid)
        con=textresume.activetext_resume
        videoresume = JSVideoResume.objects.filter(user_id=userid)
        if videoresume:
            for a in videoresume:
                if a.videoresume:
                    progress=progress+15
        profilesum=JSProfileSummary.objects.filter(user_id=userid)
        if personal:
            for a in personal:
                if a.city:
                    progress=progress+5
                if a.state:
                    progress=progress+5
                if a.country:
                    progress=progress+5
                if a.zipcode:
                    progress=progress+5
                if a.handno:
                    progress=progress+5
                if a.industry:
                    progress=progress+5
                if a.functional_area:
                    progress=progress+5
                if a.work_expyears:
                    progress=progress+5
            try:
                if con:
                    tresume=JSTextResume.objects.filter(user_id=userid)
                    for a in tresume:
                        if a.resumeFile:
                            progress=progress+15
                    return render(request,'registration/profile.html', {'jsinfo':jsinfo,'jsresume':jsresume,'jstext':jstext,'jsvideo':jsvideo,'education':education,'certificates':certificates,'skills':skills,'jsemployer':jsemployer,'projectdetails':projectdetails,'jssecret':jssecret,'jslang':jslang,'other':other,'videoresume':videoresume,'personal':personal,'tresume':tresume,'profilesum':profilesum,'progress':progress})
                else :
                    res=JSResumeActive.objects.get(user_id=userid)
                    resactid=res.resumeActive_id
                    resume=JSResume.objects.filter(id=resactid)
                    for a in resume:
                        if a.resumeFile:
                            progress=progress+15
                    return render(request,'registration/profile.html', {'jsinfo':jsinfo,'jsresume':jsresume,'jstext':jstext,'jsvideo':jsvideo,'education':education,'certificates':certificates,'skills':skills,'jsemployer':jsemployer,'projectdetails':projectdetails,'jssecret':jssecret,'jslang':jslang,'other':other,'videoresume':videoresume,'personal':personal,'resume':resume,'profilesum':profilesum,'progress':progress})
            except:
                return render(request,'registration/profile.html',{'jsinfo':jsinfo,'jsresume':jsresume,'jstext':jstext,'jsvideo':jsvideo,'education':education,'certificates':certificates,'skills':skills,'jsemployer':jsemployer,'projectdetails':projectdetails,'jssecret':jssecret,'jslang':jslang,'other':other,'videoresume':videoresume,'personal':personal,'profilesum':profilesum,'progress':progress})
    else:
        msg="ADD USER DETAILS"
        return render(request,'registration/profile.html', {'msg':msg,'progress':progress})

def emprescomp(request):
    try:
        resumes=[]
        for i in range(1,4):
            sel_resume=request.GET['r'+str(i)]
            js=JSAppliedJobs.objects.get(id=sel_resume)
            if profileviews.objects.filter(employer_id=request.user.id,jobseeker=js.JS.user.id):
                cnt=0
                for i in emp_subscribed_packs.objects.filter(employer_id=request.user.id):
                    for j in emppack_activation.objects.filter(subscribed_pack_id=i.id):
                        cnt=j.totalresume+cnt
                resume=JSTextResume.objects.get(JS_id=js.JS_id)
                istxt=1
                if not resume.activetext_resume:
                    docres=JSResumeActive.objects.get(JS_id=js.JS_id)
                    resume=JSResume.objects.get(id=docres.resumeActive_id)
                    istxt=0
                res=JSAppliedJobs.objects.filter(id=sel_resume)
                resumes.append([resume,istxt])
            else:
                resume=JSTextResume.objects.get(JS_id=js.JS_id)
                istxt=1
                print "asss"
                if not resume.activetext_resume:
                    docres=JSResumeActive.objects.get(JS_id=js.JS_id)
                    resume=JSResume.objects.get(id=docres.resumeActive_id)
                    istxt=0
                res=JSAppliedJobs.objects.filter(id=sel_resume)
                resumes.append([resume,istxt])
        return render(request,'registration/emp_resume_comp.html', {'res':res,'resumes':resumes})
    except:
        try:
            resumes=[]
            for i in range(1,3):
                sel_resume=request.GET['r'+str(i)]
                js=JSAppliedJobs.objects.get(id=sel_resume)
                resume=JSTextResume.objects.get(JS_id=js.JS_id)
                istxt=1
                if not resume.activetext_resume:
                    docres=JSResumeActive.objects.get(JS_id=js.JS_id)
                    resume=JSResume.objects.get(id=docres.resumeActive_id)
                    istxt=0
                resumes.append([resume,istxt])
                res=JSAppliedJobs.objects.filter(id=sel_resume)
            return render(request,'registration/emp_resume_comp.html', {'res':res,'resumes':resumes})
        except:
            try:
                resumes=[]
                for i in range(1,2):

                    sel_resume=request.GET['r'+str(i)]
                    js=JSAppliedJobs.objects.get(id=sel_resume)
                    resume=JSTextResume.objects.get(JS_id=js.JS_id)
                    istxt=1
                    if not resume.activetext_resume:
                        docres=JSResumeActive.objects.get(JS_id=js.JS_id)
                        resume=JSResume.objects.get(id=docres.resumeActive_id)
                        istxt=0
                    resumes.append([resume,istxt])
                    res=JSAppliedJobs.objects.filter(id=sel_resume)
                return render(request,'registration/emp_resume_comp.html', {'res':res,'resumes':resumes})
            except:
                msgrc ="Select atleast one resume"
                return render(request,'registration/emp_resume_comp.html', {'msgrc':msgrc})           

def emprescompdoc(request,res_id):
    resuid=res_id
    res=JSResumeActive.objects.get(resumeActive_id=resuid)
    resid=res.resumeActive_id
    resume=JSResume.objects.get(id=resuid)
    resumefile=resume.resumeFile
    name, fileExtension = os.path.splitext(str(resumefile))
    return render(request,'%s.html'%name)

def empdoc(request,userjs_id):
    jsid=userjs_id
    res=JSResumeActive.objects.get(user_id=jsid)
    resid=res.resumeActive_id
    resume=JSResume.objects.get(id=resid)
    resumefile=resume.resumeFile
    name, fileExtension = os.path.splitext(str(resumefile))
    return render(request,'%s.html'%name)
def iTechTalents(request):
    return render(request,'registration/iTechTalents.html')
def videorecording(request):
    return render(request,'registration/videorecording.html')

def ActivateJob(request):
    if request.method=="POST":
        empid=request.POST.get('user_id')
        jobid=request.POST.get('jobid')
        fromdate=request.POST.get('fromdate')
        enddate=request.POST.get('todate')
        subid=request.POST.get('selectPackage')
        actJob=jobs.objects.get(id=jobid)
        frmdate=datetime.strptime(fromdate , '%m-%d-%Y')
        todate=datetime.strptime(enddate , '%m-%d-%Y')
        actJob.marklive=frmdate
        actJob.todate=todate
        actJob.is_active=True
        actJob.save()
        reducecount=emppack_activation.objects.get(id=subid)
        reducecount.total_activated_job+=1; #add activated job count 1
        reducecount.totaljobpost-=1; #reduce total job post count 1
        reducecount.save()
        messages.success(request, 'Job has been activated successfully')
        return HttpResponseRedirect('/accounts/JobsEmp/')

def SelectPack(request):
    if request.method=="POST":
        empid=request.POST.get('employerid')
        packid=request.POST.get('packid')
        pack_activation=datetime.now() #today's date
        pack_expired=pack_activation + timedelta(days=30) #add 30 days from today's date
        subscribed=emp_subscribed_packs(employer_id=empid,pack_id=packid,pack_activate=pack_activation,pack_expire=pack_expired)
        subscribed.save() # add new records subscribed packs table
        subscribed_packRecords=emp_subscribed_packs.objects.get(id=subscribed.id)
        jobPostResume=emppacks.objects.get(id=subscribed.pack_id) # get number of job post and resume views for subscribed pack
        pack_already=emppack_activation.objects.filter(pack_id=subscribed_packRecords.pack_id)
        if pack_already: # check this pack is already subsribed or not
            packalready=emppack_activation.objects.get(pack_id=subscribed_packRecords.pack_id)
            packalready.subscribed_pack_id=subscribed.id
            packalready.totaljobpost=packalready.totaljobpost+jobPostResume.no_jobpost
            packalready.totalresume+=jobPostResume.no_resume
            packalready.save()
        else:
            emppack_activation(subscribed_pack_id=subscribed.id,pack_id=packid,totaljobpost=jobPostResume.no_jobpost,totalresume=jobPostResume.no_resume).save()
        messages.success(request, 'Pack has been subscriped successfully')
        return HttpResponseRedirect('/accounts/JobsEmp/')