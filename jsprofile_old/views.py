# Create your views here.
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from registration.models import *
from django.views.generic.base import View
from django.http import HttpResponse,HttpResponseRedirect
import json
from django.template import Context,Template
from django.conf import settings
from datetime import datetime
from django.contrib import messages
import os
from subprocess import call
import re
from django.utils.html import strip_tags

def is_jobseeker(user):
  try:
    user.usertype
    if user.usertype=='jobseeker':return True
    else:return False
  except:return False

#JobseekerHome
@user_passes_test(is_jobseeker,login_url='/accounts/login/')
def home(request):
  menus=['Resume','Personal Details','Educational Details',
  'Technical Skill Set','Profile Summary','Employment Details',
  'Project Details','Secret Clearance Section','Other Details']
  userid=request.user.id
  progress=0
  resactid=''
  resume=''
  if JSDetails.objects.filter(user_id=userid):
    jsinfo = JSDetails.objects.filter(user_id=userid)
    personal=JSPersonal.objects.filter(user_id=userid)
    certificates=JSCertificate.objects.filter(user_id=userid)
    jsemployer=JSEmployerDetails.objects.filter(user_id=userid)
    jssecret=JSsecurity.objects.filter(user_id=userid)
    jslang=JSLanguage.objects.filter(user_id=userid)
    jsresume=JSResume.objects.filter(user_id=userid)
    education=JSQualification.objects.filter(user_id=userid)
    other=JSDetailOther.objects.filter(user_id=userid)
    skills=JSSkills.objects.filter(user_id=userid)
    projectdetails=JSProjectDetails.objects.filter(user_id=userid)
    profilesummary=JSProfileSummary.objects.filter(user_id=userid)
    tresume=JSTextResume.objects.filter(user_id=userid)
    if tresume:
      if tresume[0].activetext_resume:progress=progress+15      
    resume=""
    if JSResumeActive.objects.filter(user_id=userid):
      res=JSResumeActive.objects.get(user_id=userid)
      resactid=res.resumeActive.id
      resume=JSResume.objects.filter(id=resactid)
      progress=progress+15      
    if education:
      for a in education:
        if a.degree:progress=progress+5
        break
    if profilesummary:
      for a in profilesummary:
        if a.profile_summary:progress=progress+5
    if skills:
      for a in skills:
        if a.skill:progress=progress+5
        break
    if projectdetails:
      for a in projectdetails:
        if a.project_title:progress=progress+5
        break
    if other:
      for a in other:
        if a.emptype:progress=progress+5
        if a.workpermit:progress=progress+5
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

    # return render(request,'jsprofile/home.html', {'navs':menus})
    return render(request,'jsprofile/home.html',{'navs':menus,'jsinfo':jsinfo,'jsresume':jsresume,'education':education,'certificates':certificates,'skills':skills,'jsemployer':jsemployer,'projectdetails':projectdetails,'jssecret':jssecret,'jslang':jslang,'other':other,'resume':resume,'personal':personal,'profilesum':profilesummary,'progress':progress,'tresume':tresume})
  else:
    msg="ADD USER DETAILS"
    return render(request,'jsprofile/home.html', {'msg':msg,'navs':menus})
def Update_education_after_add(md): 
  str_html='''    
    <tr id="edu{{l.pk}}"><td><a href="#" class="editdegree" data-type="select" data-source="/ajax/fillcombo/degree/" data-title="Enter degree" data-pk="{{l.pk}}" data-url="/ajax/update/" data-name="degree" data-params="{curtable:'edutable'}">{{ l.degree }}</a></td>
      <td><a href="#" data-type="text" data-pk="{{l.pk}}" data-title="Specialization" class="editdegree editable editable-click" data-url="/ajax/update/" data-name="special" data-params="{curtable:'edutable'}">{{l.special}}</a></td>
      <td><a href="#" data-type="text" data-pk="{{l.pk}}" data-title="University/Board" class="editdegree editable editable-click" data-url="/ajax/update/" data-name="institution" data-params="{curtable:'edutable'}">{{l.institution}}</a></td>
      <td><a href="#" data-type="text" data-pk="{{l.pk}}" data-title="City/State" class="editdegree editable editable-click" data-url="/ajax/update/" data-name="location" data-params="{curtable:'edutable'}">{{l.location}}</a></td>
      <td><a href="#" class="editdegree editable editable-click" data-type="select" data-source="/ajax/fillcombo/country/" data-title="Enter Country" data-pk="{{l.pk}}" data-url="/ajax/update/" data-name="country" data-params="{curtable:'edutable'}">{{ l.country }}</a></td>
      <td><a href="#" data-type="date" data-pk="{{l.pk}}" data-viewformat="mm-yyyy" data-title="Year of Passing" class="monthview editable editable-click" data-url="/ajax/update/" data-name="year" data-params="{curtable:'edutable'}">{{l.year}}</a></td>
      <td><a class="btn btn-mini btn-danger deleteedu" data-eduid="{{ l.pk }}" href="#">delete</a></td>
    </tr>
  '''

  t = Template(str_html)  
  return HttpResponse(t.render(Context({'l': md})))

def Update_skills_after_add(md):
  str_html='''
    <tr id="skill{{l.pk}}">
      <td><a href="#" class="editskill" data-type="text" data-title="Enter skill" data-pk="{{l.pk}}" data-url="/ajax/update/" data-name="skill" data-params="{curtable:'skilltable'}">{{ l.skill }}</a></td>
      <td><a href="#" class="editskill" data-type="text" data-title="Enter the Version" data-pk="{{l.pk}}" data-url="/ajax/update/" data-name="version" data-params="{curtable:'skilltable'}">{{ l.version }}</a></td>
      <td><a href="#" class="editskill" data-type="select" data-source="/ajax/fillcombo/lastused/" data-title="last Used Year?" data-pk="{{l.pk}}" data-url="/ajax/update/" data-name="lastused" data-params="{curtable:'skilltable'}">{{l.lastused}}</a></td>
      <td><a href="#" class="editskill" data-type="select" data-source="/ajax/fillcombo/skillyear/" data-title="Years of Experience." data-pk="{{l.pk}}" data-url="/ajax/update/" data-name="skillyear" data-params="{curtable:'skilltable'}">{{l.skillyear}}</a> Year(s) <a href="#" class="editskill" data-type="select" data-source="/ajax/fillcombo/skillmon/" data-title="Months" data-pk="{{l.pk}}" data-url="/ajax/update/" data-name="skillmon" data-params="{curtable:'skilltable'}">{{l.skillmon}}</a> Month(s)</td>
      <td><a class="btn btn-mini btn-danger deleteskill" data-skillid="{{ l.pk }}" href="#">delete</a>
      </td>
    </tr>
  '''
  t = Template(str_html)
  #print t.render(Context({'l':md}))
  return HttpResponse(t.render(Context({'l':md})))
def Update_emp_after_add(md):
  str_html='''
    
    <table  class="table table-striped info" id="emp{{l.pk}}" >
    <tr><th  colspan="4"><a href="#" class="editemp" data-type="text" data-title="Enter Company name" data-pk="{{l.pk}}" data-url="/ajax/update/" data-name="employer_name" data-params="{curtable:'emptable'}">{{ l.employer_name }}</a> -  <a href="#" class="editemp" data-type="text" data-title="Enter Company status" data-pk="{{l.pk}}" data-url="/ajax/update/" data-name="empstatus" data-params="{curtable:'emptable'}">{{ l.empstatus }}</a></th></tr>
      <tr><th style="width:25%">Duration</th><td style="width:25%"><a href="#" data-type="date" data-pk="{{l.pk}}" data-viewformat="mm-yyyy" data-format="mm-yyyy" data-title="Start date" class="editemp" data-url="/ajax/update/" data-name="empstartdate" data-params="{curtable:'emptable'}">{{l.empstartdate}}</a> to {% ifequal l.empstatus 'currentemployer' %}Today{% else %}<a href="#" data-type="date" data-pk="{{l.pk}}" data-viewformat="mm-yyyy" data-format="mm-yyyy" data-title="Start date" class="editemp" data-url="/ajax/update/" data-name="emptodate" data-params="{curtable:'emptable'}">{{l.emptodate}}</a>{% endifequal %}</td>
      <th style="width:25%">Designation</th><td style="width:25%"><a href="#" class="editemp" data-type="text" data-title="Enter Designation" data-pk="{{l.pk}}" data-url="/ajax/update/" data-name="designation" data-params="{curtable:'emptable'}">{{l.designation}}</a></td></tr>
      <tr id="emp{{l.pk}}"><th>Jobprofile</th><td colspan="3"><a href="#" class="editemp" data-type="text" data-title="Enter Jobprofile" data-pk="{{l.pk}}" data-url="/ajax/update/" data-name="jobprofile" data-params="{curtable:'emptable'}">{{l.jobprofile}}</a></td></tr>
      <tr colspan="4"><td><a class="deleteemp" data-empid="{{l.pk}}" href="#">delete</a></td>
      <td></td><td></td><td></td></tr></table>
      

  '''
  t = Template(str_html)
  return HttpResponse(t.render(Context({'l':md})))
# def Update_emp_after_add(md):
#   str_html='''
#      <div id="emp{{l.pk}}" class="emps">
#         <a class="deleteemp" data-empid="{{ l.pk }}" href="#">delete</a>
#         <p class="lead">{{l.designation}},{{ l.employer_name }}</p>
#         <p>Status:<i>{{ l.empstatus }}</i></p>
#         <p style="font-style:italic;">{{l.empstartdate}} - {% ifequal l.empstatus 'currentemployer' %}Today{% else %}{{l.emptodate}}{% endifequal %}</p>
#         <p>{{l.jobprofile|safe}}</p>
#       </div>
#   '''
#   t = Template(str_html)
#   print t.render(Context({'l':md}))
#   return HttpResponse(t.render(Context({'l':md})))


# def Update_project_after_add(md):
#   print 'project'
#   str_html='''
#   <div id="project{{l.pk}}" class="projects">
#       <a class="deleteproject" data-projectid="{{ l.pk }}" href="#">delete</a>
#       <div class="row" style="text-align:left">
#         <div class="span6">
#           <p class="lead">Client: {{l.client}}</p>
#         <p>Project Title:<i>{{ l.project_title }}</i></p>

#         <p style="font-style:italic;">{{l.projstartdate}} - {{l.projtodate}}</p>
#         <p class="lead">Location: {{l.project_loc}}({{l.on_offsite}})</p>
#         <p>Employment Type: {{ l.emp_type }}</p>

#         <p><strong>Skills:</strong>{{l.skill_used}}</p>
#         <p><strong>Role:</strong>{{l.role}}, <strong>Team Size</strong>{{l.teamsize}}</p>

#         </div>
#         <div class="span6">
#           <p style="text-decoration:underline;"><strong>Project Details</strong></p>
#         <p>{{l.project_details|safe}}</p>

#         <p style="text-decoration:underline;"><strong>Your Role:</strong></p>
#         <p>{{l.role_desc|safe}}</p>
#         </div>
#       </div>      
#     </div>
#     <hr>
#   '''
#   t = Template(str_html)
#   print t.render(Context({'l':md}))
#   return HttpResponse(t.render(Context({'l':md})))
def Update_project_after_add(md):
  str_html='''
  <table  class="table table-striped info" id="project{{l.pk}}">
    <tr><th  colspan="4"><a href="#" class="editproject" data-type="text" data-title="Enter Client" data-pk="{{l.pk}}" data-url="/ajax/update/" data-name="client" data-params="{curtable:'projecttable'}">{{ l.client }}</a> , <a href="#" class="editproject" data-type="text" data-title="Enter location" data-pk="{{l.pk}}" data-url="/ajax/update/" data-name="project_loc" data-params="{curtable:'projecttable'}">{{ l.project_loc}}</a> ,  <a href="#" class="editproject" data-type="text" data-title="Enter onsite or offsite" data-pk="{{l.pk}}" data-url="/ajax/update/" data-name="on_offsite" data-params="{curtable:'projecttable'}">{{l.on_offsite}}</a></th></tr>
    <tr><th colspan="2"><a href="#" class="editproject" data-type="text" data-title="Enter project title" data-pk="{{l.pk}}" data-url="/ajax/update/" data-name="project_tilte" data-params="{curtable:'projecttable'}">{{l.project_title}}</a></th>
    <th>Duration</th><td><a href="#" data-type="date" data-pk="{{l.pk}}" data-viewformat="mm-yyyy" data-format="mm-yyyy" data-title=" Project Start date" class="editproject" data-url="/ajax/update/" data-name="projstartdate" data-params="{curtable:'projecttable'}">{{l.projstartdate}}</a> to <a href="#" data-type="date" data-pk="{{l.pk}}" data-viewformat="mm-yyyy" data-format="mm-yyyy" data-title=" Project End date" class="editproject" data-url="/ajax/update/" data-name="projtodate" data-params="{curtable:'projecttable'}">{{l.projtodate}}</a></td></tr>
    <tr><th colspan="4"><a href="#" class="editproject" data-type="text" data-title="Enter project details" data-pk="{{l.pk}}" data-url="/ajax/update/" data-name="project_details" data-params="{curtable:'projecttable'}">{{l.project_details}}</a></th></tr>
    <tr><th>Role Description</th><td colspan="3"><a href="#" class="editproject" data-type="text" data-title="Enter Role Description" data-pk="{{l.pk}}" data-url="/ajax/update/" data-name="role_desc" data-params="{curtable:'projecttable'}">{{l.role_desc}}</a></td></tr>
    <tr><th style="width:25%;">Role</th><td style="width:25%;"><a href="#" class="editproject" data-type="select" data-source="/ajax/fillcombo/role/" data-title="Enter Role" data-pk="{{l.pk}}" data-url="/ajax/update/" data-name="role" data-params="{curtable:'projecttable'}">{{l.role}}</a></td><th style="width:25%;">Team size</th><td style="width:25%;"><a href="#" class="editproject" data-type="select" data-source="/ajax/fillcombo/teamsize/" data-title="Enter Teamsize" data-pk="{{l.pk}}" data-url="/ajax/update/" data-name="teamsize" data-params="{curtable:'projecttable'}">{{l.teamsize}}</a></td></tr>
    <tr><th style="width:25%;">Skills used</th><td style="width:25%;"><a href="#" class="editproject" data-type="text" data-title="Enter Skills used" data-pk="{{l.pk}}" data-url="/ajax/update/" data-name="skill_used" data-params="{curtable:'projecttable'}">{{l.skill_used}}</a></td><th style="width:25%;">Employment type</th><td style="width:25%;"><a href="#" class="editproject" data-type="text" data-title="Enter Employment type" data-pk="{{l.pk}}" data-url="/ajax/update/" data-name="emp_type" data-params="{curtable:'projecttable'}">{{l.emp_type}}</a></td></tr>
    <tr colspan="4"><td><a class="deleteproject" data-projectid="{{ l.pk }}" href="#">delete</a></td></td><td></td><td></td><td></td></tr></table>
  '''
  t = Template(str_html)
  return HttpResponse(t.render(Context({'l':md})))

def Update_secret_after_add(md):
  str_html='''
  <table class="table table-striped">
      <tr>
        <th >Security Clearance</th>
        <td id='secretopts'>{{secretclr.jssecretclear}}</td>
      </tr>
      <tr>
        <th>From Date</th>
        <td id="fdate">{{secretclr.jsfromdate|date:'Y-m-d'}}</td>
      </tr>
      <tr>
        <th>Expire Date</th>
        <td id="tdate">{{secretclr.jstodate|date:'Y-m-d'}}</td>
      </tr>
    </table>
  '''
  t = Template(str_html)
  #print t.render(Context({'secretclr':md}))
  return HttpResponse(t.render(Context({'secretclr':md})))
def Update_otherdetails_after_add(md):
  str_html='''
  <table class="table table-striped">
      <tr>
        <th >Employment type</th>
        <td id='secretopts'>{{otherdetails.emptype}}</td>
      </tr>
      <tr>
        <th>Work permit for USA</th>
        <td id="fdate">{{otherdetails.workpermit}}</td>
      </tr>
      <tr>
        <th>Othercountries</th>
        <td id="tdate">{{otherdetails.workother}}</td>
      </tr>
      <tr>
        <th >Willing to relocation</th>
        <td id='secretopts'>{{otherdetails.relocate}}</td>
      </tr>
      <tr>
        <th >Willing to telecommunicate</th>
        <td id='secretopts'>{{otherdetails.telecommunicate}}</td>
      </tr>
      <tr>
        <th >Willing to travel</th>
        <td id='secretopts'>{{otherdetails.travel}}</td>
      </tr>
      <tr>
        <th >Relocation choice</th>
        <td id='secretopts'>{{otherdetails.relocatechoice}}</td>
      </tr>
    </table>
  '''
  t = Template(str_html)
  #print t.render(Context({'secretclr':md}))
  return HttpResponse(t.render(Context({'otherdetails':md})))
def Update_language_after_add(md):
  str_html=''' 
    <tr id="language{{l.pk}}">
        <td>
    <a href="#" class="editlanguage" data-type="text" data-title="Language" data-pk="{{l.pk}}" data-url="/ajax/update/" data-name="language" data-params="{curtable:'languagetable'}">{{ l.language }}</a>
        </td>
        <td>
    <a href="#" class="editlanguage" data-type="select" data-source="/ajax/fillcombo/proficiency/" data-title="Proficiency" data-pk="{{l.pk}}" data-url="/ajax/update/" data-name="proficiency" data-params="{curtable:'languagetable'}">{{ l.proficiency }}</a>
        </td>
        <td>
    <a href="#" class="editlanguage" data-type="select" data-source="/ajax/fillcombo/read/" data-title="Read" data-pk="{{l.pk}}" data-url="/ajax/update/" data-name="read" data-params="{curtable:'languagetable'}">{{l.read}}</a></td>
        <td>
    <a href="#" class="editlanguage" data-type="select" data-source="/ajax/fillcombo/read/" data-title="Write" data-pk="{{l.pk}}" data-url="/ajax/update/" data-name="write" data-params="{curtable:'languagetable'}">{{l.write}}</a></td>
        <td>
    <a href="#" class="editlanguage" data-type="select" data-source="/ajax/fillcombo/read/" data-title="Speak" data-pk="{{l.pk}}" data-url="/ajax/update/" data-name="speak" data-params="{curtable:'languagetable'}">{{l.speak}}</a></td>

        <td><a class="btn btn-mini btn-danger deletelanguage" data-languageid="{{ l.pk }}" href="#">delete</a> 
  '''
  t = Template(str_html)
  return HttpResponse(t.render(Context({'l':md})))
def Update_resume_after_add(md):
  str_html='''
  <tr id="resume{{l.pk}}">
    <td id="resumetitle">{{ l.resumeTitle }}</a></td>
    <td id="resumefile">{{ l.resumeFile }}</a></td>
    <td><a class="btn btn-mini btn-danger deleteresume" data-resumeid="{{ l.pk }}" href="#">delete</a></td><td></td><td></td><td></td><td></td>
  '''
  t = Template(str_html)
  return HttpResponse(t.render(Context({'l':md})))
#url =views
class UserProfileAjax(View):
  #tfolder='jsprofile/ajaxhtmls/'
  def education(self,req,tp):
    usr=req.user
    if tp=='view':
      qual = JSQualification.objects.filter(user=usr)
      cert = JSCertificate.objects.filter(user=usr)
      return {'qualification':qual,'certificate':cert}

  def get(self,request):
    tfolder='jsprofile/ajaxhtmls/'
    userpk=request.user.id
    if request.GET['menu']=='1':
      try:res=JSResume.objects.filter(user_id=userpk)
      except:res=''
      try:txtres=JSTextResume.objects.get(user_id=userpk)
      except:txtres=''
      d=dict(resumes=res,textresume=txtres)
      return render(request,tfolder+'1_resumes.html',d)
    elif request.GET['menu']=='2':
      try:pers=JSPersonal.objects.get(user_id=userpk)
      except:pers=''
      d=dict(personal =pers )
      return render(request,tfolder+'2_personalinfo.html',d)
    elif request.GET['menu']=='3':
      edus = JSQualification.objects.filter(user_id=userpk)
      cert = JSCertificate.objects.filter(user_id=userpk)      
      d={'edus':edus,'certificate':cert}
      return render(request,tfolder+'3_education.html',d)
    elif request.GET['menu']=='4':
      d=dict(skills= JSSkills.objects.filter(user_id=userpk))
      return render(request,tfolder+'4_skills.html',d) 
    elif request.GET['menu']=='5':
      try:d=dict(summary=JSProfileSummary.objects.get(user_id=userpk))
      except:d=dict(summary='')
      return render(request,tfolder+'5_summary.html',d)
    elif request.GET['menu']=='6':
      d=dict(emp=JSEmployerDetails.objects.filter(user_id=userpk))
      return render(request,tfolder+'6_empdetails.html',d)
    elif request.GET['menu']=='7':
      d=dict(project=JSProjectDetails.objects.filter(user_id=userpk))
      return render(request,tfolder+'7_projectdetails.html',d)
    elif request.GET['menu']=='8':  
      try:d=dict(secretclr=JSsecurity.objects.get(user_id=userpk))
      except:d=dict(secretclr='')
      return render(request,tfolder+'8_secretclearence.html',d)
    elif request.GET['menu']=='9':
      otherdetails = JSDetailOther.objects.filter(user_id=userpk)
      language = JSLanguage.objects.filter(user_id=userpk)     
      d={'otherdetails':otherdetails,'lang':language}
      return render(request,tfolder+'9.otherdetails.html',d)

  def post_save_curform(self,req,md):
    d=dict()
    for i in req.POST.keys():
      if i in ['curform','csrfmiddlewaretoken']:continue
      if i in ['first_name','last_name']:
        setattr(req.user,i,req.POST[i].capitalize())
        req.user.save()
        d[i]=req.POST[i]
        continue
      if i in ['jsfromdate','jstodate']:
        fd=datetime.strptime(req.POST[i],"%m-%d-%Y")
        setattr(md,i,fd)
        continue
      # if i in ['year']:
      #   fd=datetime.strptime(req.POST[i],"%m/%Y")
      #   setattr(md,i,fd)
      #   continue
      if i in ['workother']:
        wo=''
        for j in req.POST.getlist('workother'):
          wo+=j+','
        workother=wo[:-1]
        setattr(md,i,workother)
        md.save()
        d[i]=req.POST[i]
        continue
      if i in ['relocatechoice']:
        rc=''
        for j in req.POST.getlist('relocatechoice'):
          rc+=j+','
        relocatechoice=rc[:-1]
        setattr(md,i,relocatechoice)
        md.save()
        d[i]=req.POST[i]
        continue
      setattr(md,i,req.POST[i]) #setattr(md,i,req.POST[i].capitalize())
      d[i]=req.POST[i]
    md.save()
    if req.POST['curform']=='eduform':      
      return Update_education_after_add(md)      
    elif req.POST['curform']=='skillform':
      return Update_skills_after_add(md)
    elif req.POST['curform']=='empform':
      return Update_emp_after_add(md)
    elif req.POST['curform']=='projectform':
      return Update_project_after_add(md)
    elif req.POST['curform']=='secretform':
      return Update_secret_after_add(md)
    elif req.POST['curform']=='otherdetailsform':
      return Update_otherdetails_after_add(md)
    elif req.POST['curform']=='languageform':
      return Update_language_after_add(md)
    
    d['pk']=md.pk
    return HttpResponse(json.dumps(d), mimetype="application/json")

  def post(self,request):
    curform=request.POST['curform']
    usr=request.user
    if not JSDetails.objects.filter(user=request.user):JSDetails(user_id=request.user.id,post_date=datetime.now(),update_date=datetime.now()).save()
    if curform=='skillform':
      tb=JSSkills(user=usr,JS=usr.jsdetails)    
    elif curform=='eduform':
      tb=JSQualification(user=usr,JS=usr.jsdetails)
    elif curform=='profform':
      tb,created=JSPersonal.objects.get_or_create(user=usr,JS=usr.jsdetails)
    elif curform=='summaryform':
      tb,created=JSProfileSummary.objects.get_or_create(user=usr,JS=usr.jsdetails)
    elif curform=='empform':
      tb=JSEmployerDetails(user=usr,JS=usr.jsdetails)
    elif curform=='projectform':
      tb=JSProjectDetails(user=usr,JS=usr.jsdetails)
    elif curform=='secretform':
      tb,created=JSsecurity.objects.get_or_create(user=usr,JS=usr.jsdetails)
    elif curform=='otherdetailsform':
      tb,created=JSDetailOther.objects.get_or_create(user=usr,JS=usr.jsdetails)
    elif curform=='languageform':
      tb=JSLanguage(user=usr,JS=usr.jsdetails)
    elif curform=='textresumeform':
      tb,created=JSTextResume.objects.get_or_create(user=usr,JS=usr.jsdetails)
    return self.post_save_curform(request,tb)

#url =del
def delete(request):
  if 'skillid' in request.GET:
    JSSkills.objects.get(pk=request.GET['skillid']).delete()    
  elif 'eduid' in request.GET:
    JSQualification.objects.get(pk=request.GET['eduid']).delete()
  elif 'empid' in request.GET:
    JSEmployerDetails.objects.get(pk=request.GET['empid']).delete()
  elif 'projectid' in request.GET:
    JSProjectDetails.objects.get(pk=request.GET['projectid']).delete()
  elif 'languageid' in request.GET:
    JSLanguage.objects.get(pk=request.GET['languageid']).delete()
  elif 'resumeid' in request.GET:
    v=JSResume.objects.get(pk=request.GET['resumeid'])
    file_todelete=v.resumeFile
    if JSResumeActive.objects.filter(resumeActive_id=request.GET['resumeid']):
      striped_file=str(file_todelete).strip("documents").strip("/").strip(".").strip("pdf").strip("docx").strip("odt").strip("rtf").strip("txt").strip("doc")
      os.remove(settings.CURRENT_DIR+"/tagging/templates/documents/"+str(striped_file)+".html")
    JSResume.objects.get(pk=request.GET['resumeid']).delete()   
  return HttpResponse(request.GET.items()[0][1])

def update(request):  
  curtable=request.GET['curtable']
  curpk=request.GET['pk']
  itemname=request.GET['name']
  itemval=request.GET['value']
  if curtable=='edutable':
    tb=JSQualification.objects.get(id=curpk)
  elif curtable=='skilltable':
    tb=JSSkills.objects.get(id=curpk)
  elif curtable=='emptable':
    tb=JSEmployerDetails.objects.get(id=curpk)
  elif curtable=='projecttable':
    tb=JSProjectDetails.objects.get(id=curpk)
  elif curtable=='languagetable':
    tb=JSLanguage.objects.get(id=curpk)
  # elif curtable=='resumetable':
  #   tb=JSResume.objects.get(id=curpk)
  setattr(tb,itemname,itemval)
  tb.save()
  return HttpResponse('s')

def fillcombo(request,nm):
  from jsprofile.comboitems import *
  newlist=eval('{0}_list'.format(nm))
  return HttpResponse(json.dumps([dict(value=cont,text=cont) for cont in newlist]), mimetype="application/json")
# def filesave(request):
#   if request.POST:
#     count=JSResume.objects.filter(user=request.user,JS=request.user.jsdetails).count()
#     if  count < 5:
#       print "entered"
#       JSResume(user=request.user,JS=request.user.jsdetails,resumeTitle=request.POST['jsResumeTitle'],resumeFile=request.FILES['jsResumeFile']).save()
#       count+=1
#       resumes=JSResume.objects.all()
#       st='''
#       {% for l in resumes %}
#               <tr id="resume{{l.pk}}">
#               <td>{{ l.resumeTitle }}
#               </td>
#               <td>{{ l.resumeFile }}
#               </td>
#               <td><a class="btn btn-mini btn-danger deleteresume" data-resumeid="{{ l.pk }}" href="#">delete</a>
#               </td><td></td><td></td><td></td><td></td></tr>
#       {% endfor %}
#       '''
#       t=Template(st)
#       c=Context({"resumes":resumes})
#       return HttpResponse(json.dumps(t.render(c)),mimetype='application/json')
#     return render(request,'1_resumes.html',{'count':count})                                                                                                                                             

def filesave(request):
  userpk=request.user.id
  if request.POST['curform']=='resumeaddform':
    if not JSDetails.objects.filter(user=request.user):JSDetails(user=request.user,post_date=datetime.now(),update_date=datetime.now()).save()
    count=JSResume.objects.filter(user=request.user,JS=request.user.jsdetails).count()
    if count < 5:
      JSResume(user=request.user,JS_id=2,resumeTitle=request.POST['jsResumeTitle'],resumeFile=request.FILES['jsResumeFile']).save()
      count+=1
  if request.POST['curform']=='resumeeditform':
    res=JSResume.objects.get(id=request.POST['resumeid'],user=request.user)
    res.resumeTitle=request.POST.get('jsResumeTitle')
    res.resumeFile=request.FILES.get('jsResumeFile')
    res.save()
  # JSResume(resumeTitle=request.POST['jsResumeTitle'],resumeFile=request.FILES['jsResumeFile']).save()
  resumes=JSResume.objects.filter(user=request.user)
  st=' <table class="table table-striped" id="resumeTable"> <tr class="info"><th>Resume Title</th><th>Uploaded Resume</th><th>Active/Inactive</th><th>Action1</th><th>Action2</th></tr>'
  for i in resumes:
    if JSResumeActive.objects.filter(resumeActive_id=i.id):
      st+='<tr id="resume%d"><td>%s</td><td>%s</td><td><a class="btn btn-mini btn-success activeresume" data-resumeid="%d" href="#">Make it deactive</a></td><td><a class="btn btn-mini btn-danger deleteresume" data-resumeid="%d" href="#">delete</a></td><td><a href="#myModal1" role="button" data-toggle="modal" class="btn btn-mini btn-default editresume" data-resumeid="%d" href="#">edit</a></td></tr>' %(i.id,i.resumeTitle,i.resumeFile,i.id,i.id,i.id)
    else:
      st+='<tr id="resume%d"><td>%s</td><td>%s</td><td><a class="btn btn-mini btn-danger activeresume" data-resumeid="%d" href="#">Make it Aactive</a></td><td><a class="btn btn-mini btn-danger deleteresume" data-resumeid="%d" href="#">delete</a></td><td><a href="#myModal1" role="button" data-toggle="modal" class="btn btn-mini btn-default editresume" data-resumeid="%d" href="#">edit</a></td></tr>' %(i.id,i.resumeTitle,i.resumeFile,i.id,i.id,i.id)
      
  d={'table':st,'count':count}
  return HttpResponse(json.dumps(d),mimetype='application/json')  
def resumeactivation(request):
  if 'txtactres' in request.GET:
    txtres=JSTextResume.objects.get(user=request.user)
    if request.GET['txtactres'] == '1':txtres.activetext_resume=False
    if request.GET['txtactres'] == '2':txtres.activetext_resume=True
    txtres.save()
    if JSResumeActive.objects.filter(user=request.user):
      v=JSResumeActive.objects.get(user_id=request.user.id)
      activatedfile=v.resumeActive.resumeFile
      striped_file=str(activatedfile).strip("documents").strip("/").strip(".").strip("pdf").strip("docx").strip("odt").strip("rtf").strip("txt").strip("doc")
      os.remove(settings.CURRENT_DIR+"/tagging/templates/documents/"+str(striped_file)+".html")
      JSResumeActive.objects.filter(user=request.user).delete()
    return HttpResponse('Success')
    #txtres.activetext_resume=
  else:
    activatedfile=""
    striped_file=""
    if JSTextResume.objects.filter(user=request.user):
      tr=JSTextResume.objects.get(user=request.user)
      tr.activetext_resume=False
      tr.save()
    if JSResumeActive.objects.filter(user=request.user):
      v=JSResumeActive.objects.get(user_id=request.user.id)
      activatedfile=v.resumeActive.resumeFile
      striped_file=str(activatedfile).strip("documents").strip("/").strip(".").strip("pdf").strip("docx").strip("odt").strip("rtf").strip("txt").strip("doc")
      os.remove(settings.CURRENT_DIR+"/tagging/templates/documents/"+str(striped_file)+".html")
    edit, created=JSResumeActive.objects.get_or_create(user_id=request.user.id)
    edit.JS_id=request.user.jsdetails.id
    edit.resumeActive_id=request.GET['resumeid']
    edit.save()
    res=JSResume.objects.get(id=request.GET['resumeid'],user=request.user)
    call(["unoconv","-f","html","-o",settings.CURRENT_DIR+"/tagging/templates/documents/",settings.CURRENT_DIR+"/media/"+str(res.resumeFile)])
    return HttpResponse('success')
    resumes=JSResume.objects.filter(user=request.user)
    st=' <table class="table table-striped" id="resumeTable"> <tr class="info"><th>Resume Title</th><th>Uploaded Resume</th><th>Active/Inactive</th><th>Action1</th><th>Action2</th></tr>'
    for i in resumes:
      if JSResumeActive.objects.filter(resumeActive_id=i.id):
        st+='<tr id="resume%d"><td>%s</td><td>%s</td><td><a class="btn btn-mini btn-success activeresume" data-resumeid="%d" href="#">Make it deactive</a></td><td><a class="btn btn-mini btn-danger deleteresume" data-resumeid="%d" href="#">delete</a></td><td><a href="#myModal1" role="button" data-toggle="modal" class="btn btn-mini btn-default editresume" data-resumeid="%d" href="#">edit</a></td></tr>' % (i.id,i.resumeTitle,i.resumeFile,i.id,i.id,i.id)
      else:
        st+='<tr id="resume%d"><td>%s</td><td>%s</td><td><a class="btn btn-mini btn-danger activeresume" data-resumeid="%d" href="#">Make it active</a></td><td><a class="btn btn-mini btn-danger deleteresume" data-resumeid="%d" href="#">delete</a></td><td><a href="#myModal1" role="button" data-toggle="modal" class="btn btn-mini btn-default editresume" data-resumeid="%d" href="#">edit</a></td></tr>' % (i.id,i.resumeTitle,i.resumeFile,i.id,i.id,i.id)
    d={'st':st}
    return HttpResponse(json.dumps(st),mimetype='application/json')

@user_passes_test(is_jobseeker,login_url='/accounts/login/')
def edit_profilepic_info(request):
  if request.method == "POST":
    profilepic,created=JSProfileSummary.objects.get_or_create(user=request.user,JS_id=request.user.jsdetails.id)
    if profilepic.profile_pic:os.remove(settings.CURRENT_DIR+"/media/"+str(profilepic.profile_pic))
    profilepic.profile_pic=request.FILES['profile_pic']
    profilepic.save()

    edit1 = JSDetails.objects.get(user=request.user)
    edit1.update_date=datetime.now()
    edit1.save()
    
    messages.success(request, 'Your profile updated successfully')
    return HttpResponseRedirect('/ajax/profile/')
    # except:
    #   print "in except"
    #   if profile_pics:
    #     p = JSProfileSummary(user_id=userid,profile_pic=profile_pics,JS_id=request.user.jsdetails.id)
    #     p.save()
    #     d = JSDetails(user_id=userid,visiblity=True,post_date=datetime.now(),update_date=datetime.now())
    #   messages.success(request, 'Your profile updated successfully')
    #   return HttpResponseRedirect('/ajax/profile/')
  else:
    details = User.objects.filter(id=request.user.id)
    details1 = JSProfileSummary.objects.filter(user_id=request.user.id)
    return render(request,'jsprofile/ajaxhtmls/profilepic_update.html', {"details":details, "details1":details1})
@user_passes_test(is_jobseeker,login_url='/accounts/login/')
def remove_profilepic_info(request):
  if 'rmprfpics' in request.GET:
    profilepic,created=JSProfileSummary.objects.get_or_create(user=request.user,JS_id=request.user.jsdetails.id)
    profilepic.profile_pic.delete()
    if profilepic.profile_pic:os.remove(settings.CURRENT_DIR+"/media/"+str(profilepic.profile_pic))
  return HttpResponse()
@user_passes_test(is_jobseeker,login_url='/accounts/login/')
def NewProfilePictures(request):
  if request.method=="POST":
    userid=request.POST.get('userid')
    upimages=request.FILES.get('uploadimage')
    jsdedit,jsdcreate=JSDetails.objects.get_or_create(user_id=userid)
    jsdedit.update_date=datetime.now()
    jspedit,jspcreate=JSProfileSummary.objects.get_or_create(user_id=userid,JS_id=jsdedit.id)
    jspedit.profile_pic=upimages
    jspedit.save()
    jsdedit.save()
    messages.success(request, 'Profile has been edited successfully')
    return HttpResponseRedirect('/ajax/profile/')



