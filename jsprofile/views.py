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
from video_resume.models import VideoResume

def is_jobseeker(user):
  try:
    user.usertype
    if user.usertype=='jobseeker':return True
    else:return False
  except:return False
def deleteuserdetails(request):
  if 'resid' in request.GET:
    v=JSResume.objects.get(id=request.GET['resid'])
    file_todelete=v.resumeFile
    if JSResumeActive.objects.filter(resumeActive_id=request.GET['resid']):
      striped_file=str(file_todelete).replace('documents','').replace('/','').replace('.odt','').replace('.docx','').replace('.doc','').replace('.pdf','').replace('.rtf','').replace('.txt','')
      os.remove(settings.CURRENT_DIR+"/tagging/templates/documents/"+str(striped_file)+".html")
    JSResume.objects.get(id=request.GET['resid']).delete()
    return HttpResponse()
  elif 'eduid' in request.GET:
    JSQualification.objects.get(id=request.GET['eduid']).delete()
    return HttpResponse()
  elif 'skillid' in request.GET:
    JSSkills.objects.get(id=request.GET['skillid']).delete()
    return HttpResponse()
  elif 'empid' in request.GET:
    JSEmployerDetails.objects.get(id=request.GET['empid']).delete()
    return HttpResponse()
  elif 'projectid' in request.GET:
    JSProjectDetails.objects.get(id=request.GET['projectid']).delete()
    return HttpResponse()
  elif 'languageid' in request.GET:
    JSLanguage.objects.get(id=request.GET['languageid']).delete()
    return HttpResponse()
@user_passes_test(is_jobseeker,login_url='/accounts/login/')


def home(request,link):
  menus=['Resume', 'VideoResume', 'Personal Details','Educational Details',
  'Technical Skill Set','Profile Summary','Employment Details',
  'Project Details','Secret Clearance Section','Other Details']
  edt,crt=JSDetails.objects.get_or_create(user=request.user)
  edt.save()
  ed,cr=JSProfileSummary.objects.get_or_create(user=request.user,JS_id=request.user.jsdetails.id)
  ed.save()
  if link == 'Dashboard':
    progress=0
    resactid=''
    resume=''
    if JSDetails.objects.filter(user_id=request.user.id):
      jsinfo = JSDetails.objects.filter(user_id=request.user.id)
      personal=JSPersonal.objects.filter(user_id=request.user.id)
      certificates=JSCertificate.objects.filter(user_id=request.user.id)
      jsemployer=JSEmployerDetails.objects.filter(user_id=request.user.id)
      jssecret=JSsecurity.objects.filter(user_id=request.user.id)
      jslang=JSLanguage.objects.filter(user_id=request.user.id)
      jsresume=JSResume.objects.filter(user_id=request.user.id)
      education=JSQualification.objects.filter(user_id=request.user.id)
      other=JSDetailOther.objects.filter(user_id=request.user.id)
      skills=JSSkills.objects.filter(user_id=request.user.id)
      projectdetails=JSProjectDetails.objects.filter(user_id=request.user.id)
      profilesummary=JSProfileSummary.objects.filter(user_id=request.user.id)
      tresume=JSTextResume.objects.filter(user_id=request.user.id)
      if tresume:
        if tresume[0].activetext_resume:progress=progress+15      
      resume=""
      if JSResumeActive.objects.filter(user_id=request.user.id):
        res=JSResumeActive.objects.get(user_id=request.user.id)
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
      return render(request,'jsprofile/home.html',{'navs':menus,'jsinfo':jsinfo,'jsresume':jsresume,'education':education,'certificates':certificates,'skills':skills,'jsemployer':jsemployer,'projectdetails':projectdetails,'jssecret':jssecret,'jslang':jslang,'other':other,'resume':resume,'personal':personal,'profilesum':profilesummary,'progress':progress,'tresume':tresume})
    else:
      msg="ADD USER DETAILS"
      return render(request,'jsprofile/home.html', {'msg':msg,'navs':menus})
  elif link == 'Resume':
    res=JSResume.objects.filter(user=request.user)
    txtres=JSTextResume.objects.filter(user=request.user)
    d=dict(resumes=res,textresume=txtres,navs=menus)
    return render(request,'jsprofile/ajaxhtmls/1_resumes.html',d)
  
  elif link == 'VideoResume':
    resumes = VideoResume.objects.filter(user=request.user)
    data = {
      "navs": menus,
      "resumes": resumes
    }
    return render(request,'jsprofile/ajaxhtmls/1a_video_resumes.html', data)    

  elif link == 'Personal_Details':
    pers=JSPersonal.objects.filter(user=request.user)
    print pers
    d=dict(personal=pers,navs=menus)
    print d
    return render(request,'jsprofile/ajaxhtmls/2_personalinfo.html',d)
  
  elif link == 'Educational_Details':
    edus=JSQualification.objects.filter(user=request.user)
    d=dict(edus=edus,navs=menus)
    return render(request,'jsprofile/ajaxhtmls/3_education.html',d)
  elif link == 'Technical_Skill_Set':
    skills=JSSkills.objects.filter(user=request.user)
    d=dict(skills=skills,navs=menus)
    return render(request,'jsprofile/ajaxhtmls/4_skills.html',d)
  elif link == 'Profile_Summary':
    summary=JSProfileSummary.objects.filter(user=request.user)
    print summary
    d=dict(summary=summary,navs=menus)
    print d
    print "in profile summary"
    return render(request,'jsprofile/ajaxhtmls/5_summary.html',d)
  
  
  elif link == 'Employment_Details':
    emp=JSEmployerDetails.objects.filter(user=request.user)
    is_currentjob=0
    for e in emp:
      if e.empstatus=='Current Employer':is_currentjob=1
    d=dict(emp=emp,navs=menus,curjob=is_currentjob)
    return render(request,'jsprofile/ajaxhtmls/6_empdetails.html',d)  
  elif link == 'Project_Details':
    project=JSProjectDetails.objects.filter(user=request.user)
    d=dict(project=project,navs=menus)
    return render(request,'jsprofile/ajaxhtmls/7_projectdetails.html',d) 
  elif link == 'Secret_Clearance_Section':
    secretclr=JSsecurity.objects.filter(user=request.user)
    d=dict(secretclr=secretclr,navs=menus)
    return render(request,'jsprofile/ajaxhtmls/8_secretclearence.html',d) 
  elif link == 'Other_Details':
    lang=JSLanguage.objects.filter(user=request.user)
    otherdetails=JSDetailOther.objects.filter(user=request.user)
    d=dict(lang=lang,otherdetails=otherdetails,navs=menus)
    return render(request,'jsprofile/ajaxhtmls/9.otherdetails.html',d)
def Update_education_after_add(md): 
  str_html='''    
    <tr id="edu{{l.pk}}"><td><a href="#" class="editdegree" data-type="select" data-source="/fillcombo/degree/" data-title="Enter degree" data-pk="{{l.pk}}" data-url="/updateedu/" data-name="degree" data-params="{curtable:'edutable'}">{{ l.degree }}</a></td>
      <td><a href="#" data-type="text" data-pk="{{l.pk}}" data-title="Specialization" class="editdegree editable editable-click" data-url="/updateedu/" data-name="special" data-params="{curtable:'edutable'}">{{l.special}}</a></td>
      <td><a href="#" data-type="text" data-pk="{{l.pk}}" data-title="University/Board" class="editdegree editable editable-click" data-url="/updateedu/" data-name="institution" data-params="{curtable:'edutable'}">{{l.institution}}</a></td>
      <td><a href="#" data-type="text" data-pk="{{l.pk}}" data-title="City/State" class="editdegree editable editable-click" data-url="/updateedu/" data-name="location" data-params="{curtable:'edutable'}">{{l.location}}</a></td>
      <td><a href="#" class="editdegree editable editable-click" data-type="select" data-source="/fillcombo/country/" data-title="Enter Country" data-pk="{{l.pk}}" data-url="/updateedu/" data-name="country" data-params="{curtable:'edutable'}">{{ l.country }}</a></td>
      <td><a href="#" data-type="date" data-pk="{{l.pk}}" data-viewformat="mm-yyyy" data-title="Year of Passing" class="monthview editable editable-click" data-url="/updateedu/" data-name="year" data-params="{curtable:'edutable'}">{{l.year}}</a></td>
      <td><a class="btn btn-mini btn-danger deleteedu" data-eduid="{{ l.pk }}" href="#">delete</a></td>
    </tr>
  '''
  t = Template(str_html)  
  return HttpResponse(t.render(Context({'l': md})))
def Update_skills_after_add(md):
  str_html='''
    <tr id="skill{{l.pk}}">
      <td><a href="#" class="editskill" data-type="text" data-title="Enter skill" data-pk="{{l.pk}}" data-url="/updateskill/" data-name="skill" data-params="{curtable:'skilltable'}">{{ l.skill }}</a></td>
      <td><a href="#" class="editskill" data-type="text" data-title="Enter the Version" data-pk="{{l.pk}}" data-url="/updateskill/" data-name="version" data-params="{curtable:'skilltable'}">{{ l.version }}</a></td>
      <td><a href="#" class="editskill" data-type="select" data-source="/fillcombo/lastused/" data-title="last Used Year?" data-pk="{{l.pk}}" data-url="/updateskill/" data-name="lastused" data-params="{curtable:'skilltable'}">{{l.lastused}}</a></td>
      <td><a href="#" class="editskill" data-type="select" data-source="/fillcombo/skillyear/" data-title="Years of Experience." data-pk="{{l.pk}}" data-url="/ajax/update/" data-name="skillyear" data-params="{curtable:'skilltable'}">{{l.skillyear}}</a> Year(s) <a href="#" class="editskill" data-type="select" data-source="/fillcombo/skillmon/" data-title="Months" data-pk="{{l.pk}}" data-url="/updateskill/" data-name="skillmon" data-params="{curtable:'skilltable'}">{{l.skillmon}}</a> Month(s)</td>
      <td><a class="btn btn-mini btn-danger deleteskill" data-skillid="{{ l.pk }}" href="#">delete</a>
      </td>
    </tr>
  '''
  t = Template(str_html)
  return HttpResponse(t.render(Context({'l':md})))
def Update_emp_after_add(md):
  str_html='''    
    <table  class="table table-striped info" id="emp{{l.pk}}" >
    <tr><th  colspan="4"><a href="#" class="editemp" data-type="text" data-title="Enter Company name" data-pk="{{l.pk}}" data-url="/updateemp/" data-name="employer_name" data-params="{curtable:'emptable'}">{{ l.employer_name }}</a> -  <a href="#" class="editemp" data-type="text" data-title="Enter Company status" data-pk="{{l.pk}}" data-url="/updateemp/" data-name="empstatus" data-params="{curtable:'emptable'}">{{ l.empstatus }}</a></th></tr>
      <tr><th style="width:25%">Duration</th><td style="width:25%"><a href="#" data-type="date" data-pk="{{l.pk}}" data-viewformat="mm-yyyy" data-format="mm-yyyy" data-title="Start date" class="editemp" data-url="/updateemp/" data-name="empstartdate" data-params="{curtable:'emptable'}">{{l.empstartdate}}</a> to {% ifequal l.empstatus 'currentemployer' %}Today{% else %}<a href="#" data-type="date" data-pk="{{l.pk}}" data-viewformat="mm-yyyy" data-format="mm-yyyy" data-title="Start date" class="editemp" data-url="/updateemp/" data-name="emptodate" data-params="{curtable:'emptable'}">{{l.emptodate}}</a>{% endifequal %}</td>
      <th style="width:25%">Designation</th><td style="width:25%"><a href="#" class="editemp" data-type="text" data-title="Enter Designation" data-pk="{{l.pk}}" data-url="/updateemp/" data-name="designation" data-params="{curtable:'emptable'}">{{l.designation}}</a></td></tr>
      <tr id="emp{{l.pk}}"><th>Jobprofile</th><td colspan="3"><a href="#" class="editemp" data-type="text" data-title="Enter Jobprofile" data-pk="{{l.pk}}" data-url="/updateemp/" data-name="jobprofile" data-params="{curtable:'emptable'}">{{l.jobprofile}}</a></td></tr>
      <tr colspan="4"><td><a class="deleteemp" data-empid="{{l.pk}}" href="#">delete</a></td>
      <td></td><td></td><td></td></tr></table>
  '''
  t = Template(str_html)
  return HttpResponse(t.render(Context({'l':md})))
def Update_project_after_add(md):
  str_html='''
  <table  class="table table-striped info" id="project{{l.pk}}">
    <tr><th  colspan="4"><a href="#" class="editproject" data-type="text" data-title="Enter Client" data-pk="{{l.pk}}" data-url="/updateproject/" data-name="client" data-params="{curtable:'projecttable'}">{{ l.client }}</a> , <a href="#" class="editproject" data-type="text" data-title="Enter location" data-pk="{{l.pk}}" data-url="/updateproject/" data-name="project_loc" data-params="{curtable:'projecttable'}">{{ l.project_loc}}</a> ,  <a href="#" class="editproject" data-type="text" data-title="Enter onsite or offsite" data-pk="{{l.pk}}" data-url="/updateproject/" data-name="on_offsite" data-params="{curtable:'projecttable'}">{{l.on_offsite}}</a></th></tr>
    <tr><th colspan="2"><a href="#" class="editproject" data-type="text" data-title="Enter project title" data-pk="{{l.pk}}" data-url="/updateproject/" data-name="project_title" data-params="{curtable:'projecttable'}">{{l.project_title}}</a></th>
    <th>Duration</th><td><a href="#" data-type="date" data-pk="{{l.pk}}" data-viewformat="mm-yyyy" data-format="mm-yyyy" data-title=" Project Start date" class="editproject" data-url="/updateproject/" data-name="projstartdate" data-params="{curtable:'projecttable'}">{{l.projstartdate}}</a> to <a href="#" data-type="date" data-pk="{{l.pk}}" data-viewformat="mm-yyyy" data-format="mm-yyyy" data-title=" Project End date" class="editproject" data-url="/updateproject/" data-name="projtodate" data-params="{curtable:'projecttable'}">{{l.projtodate}}</a></td></tr>
    <tr><th colspan="4"><a href="#" class="editproject" data-type="text" data-title="Enter project details" data-pk="{{l.pk}}" data-url="/updateproject/" data-name="project_details" data-params="{curtable:'projecttable'}">{{l.project_details}}</a></th></tr>
    <tr><th>Role Description</th><td colspan="3"><a href="#" class="editproject" data-type="text" data-title="Enter Role Description" data-pk="{{l.pk}}" data-url="/updateproject/" data-name="role_desc" data-params="{curtable:'projecttable'}">{{l.role_desc}}</a></td></tr>
    <tr><th style="width:25%;">Role</th><td style="width:25%;"><a href="#" class="editproject" data-type="select" data-source="/fillcombo/role/" data-title="Enter Role" data-pk="{{l.pk}}" data-url="/updateproject/" data-name="role" data-params="{curtable:'projecttable'}">{{l.role}}</a></td><th style="width:25%;">Team size</th><td style="width:25%;"><a href="#" class="editproject" data-type="select" data-source="/fillcombo/teamsize/" data-title="Enter Teamsize" data-pk="{{l.pk}}" data-url="/updateproject/" data-name="teamsize" data-params="{curtable:'projecttable'}">{{l.teamsize}}</a></td></tr>
    <tr><th style="width:25%;">Skills used</th><td style="width:25%;"><a href="#" class="editproject" data-type="text" data-title="Enter Skills used" data-pk="{{l.pk}}" data-url="/updateproject/" data-name="skill_used" data-params="{curtable:'projecttable'}">{{l.skill_used}}</a></td><th style="width:25%;">Employment type</th><td style="width:25%;"><a href="#" class="editproject" data-type="text" data-title="Enter Employment type" data-pk="{{l.pk}}" data-url="/updateproject/" data-name="emp_type" data-params="{curtable:'projecttable'}">{{l.emp_type}}</a></td></tr>
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
  return HttpResponse(t.render(Context({'otherdetails':md})))
def Update_language_after_add(md):
  str_html=''' 
    <tr id="language{{l.pk}}">
        <td>
    <a href="#" class="editlanguage" data-type="text" data-title="Language" data-pk="{{l.pk}}" data-url="/updatelanguage/" data-name="language" data-params="{curtable:'languagetable'}">{{ l.language }}</a>
        </td>
        <td>
    <a href="#" class="editlanguage" data-type="select" data-source="/fillcombo/proficiency/" data-title="Proficiency" data-pk="{{l.pk}}" data-url="/updatelanguage/" data-name="proficiency" data-params="{curtable:'languagetable'}">{{ l.proficiency }}</a>
        </td>
        <td>
    <a href="#" class="editlanguage" data-type="select" data-source="/fillcombo/read/" data-title="Read" data-pk="{{l.pk}}" data-url="/updatelanguage/" data-name="read" data-params="{curtable:'languagetable'}">{{l.read}}</a></td>
        <td>
    <a href="#" class="editlanguage" data-type="select" data-source="/fillcombo/read/" data-title="Write" data-pk="{{l.pk}}" data-url="/updatelanguage/" data-name="write" data-params="{curtable:'languagetable'}">{{l.write}}</a></td>
        <td>
    <a href="#" class="editlanguage" data-type="select" data-source="/fillcombo/read/" data-title="Speak" data-pk="{{l.pk}}" data-url="/updatelanguage/" data-name="speak" data-params="{curtable:'languagetable'}">{{l.speak}}</a></td>

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
class UserProfileAjax(View):
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
      setattr(md,i,req.POST[i])
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
    print usr,"usr"
    print curform, "cur form"
    v=JSTextResume.objects.get(user=usr,JS=usr.jsdetails)
    print v.resumeFile
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
      print "place"
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
    v=JSResume.objects.get(id=request.GET['resumeid'])
    file_todelete=v.resumeFile
    if JSResumeActive.objects.filter(resumeActive_id=request.GET['resumeid']):
      striped_file=str(file_todelete).replace('documents','').replace('/','').replace('.odt','').replace('.ODT','').replace('.docx','').replace('.DOCX','').replace('.doc','').replace('.DOC','').replace('.pdf','').replace('.PDF','').replace('.rtf','').replace('.RTF','').replace('.txt','').replace('.TXT','')
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
  setattr(tb,itemname,itemval)
  tb.save()
  return HttpResponse()
def fillcombo(request,nm):
  from jsprofile.comboitems import *
  newlist=eval('{0}_list'.format(nm))
  return HttpResponse(json.dumps([dict(value=cont,text=cont) for cont in newlist]), mimetype="application/json")
def filesave(request):
  if 'restit' in request.GET:
    msg=0
    if request.GET['resid']=='addres':
      if JSResume.objects.filter(user_id=request.GET['userid'],resumeTitle=request.GET['restit']):msg=1
    else:
      if JSResume.objects.filter(user_id=request.GET['userid'],resumeTitle=request.GET['restit']).exclude(id=request.GET['resid']):msg=1
    return HttpResponse(json.dumps(dict(msg=msg,resid=request.GET['resid'])), mimetype="application/json")
  userpk=request.user.id
  if request.POST['curform']=='resumeaddform':
    if not JSDetails.objects.filter(user=request.user):JSDetails(user=request.user,post_date=datetime.now(),update_date=datetime.now()).save()
    count=JSResume.objects.filter(user=request.user,JS=request.user.jsdetails).count()
    if count < 5:
      JSResume(user=request.user,JS_id=request.user.jsdetails.id,resumeTitle=request.POST['jsResumeTitle'],resumeFile=request.FILES['jsResumeFile']).save()
      count+=1
    return HttpResponse('')
  if request.POST['curform']=='resumeeditform':
    res=JSResume.objects.get(id=request.POST['resumeid'],user=request.user)
    if JSResumeActive.objects.filter(user=request.user,resumeActive_id=request.POST['resumeid']):
      if 'jsResumeFile' in request.FILES:
        v=JSResumeActive.objects.get(user_id=request.user.id)
        activatedfile=v.resumeActive.resumeFile
        striped_file=str(activatedfile).replace('documents','').replace('/','').replace('.odt','').replace('.ODT','').replace('.docx','').replace('.DOCX','').replace('.doc','').replace('.DOC','').replace('.pdf','').replace('.PDF','').replace('.rtf','').replace('.RTF','').replace('.txt','').replace('.TXT','')
        print striped_file
        os.remove(settings.CURRENT_DIR+"/tagging/templates/documents/"+str(striped_file)+".html")
        os.remove(settings.CURRENT_DIR+"/media/"+str(res.resumeFile))
        res.resumeFile=request.FILES.get('jsResumeFile')
      if 'jsResumeTitle' in request.POST:res.resumeTitle=request.POST.get('jsResumeTitle')       
      res.save()
      if 'jsResumeFile' in request.FILES:call(["unoconv","-f","html","-o",settings.CURRENT_DIR+"/tagging/templates/documents/",settings.CURRENT_DIR+"/media/"+str(res.resumeFile)])
    else:
      if request.FILES.get('jsResumeFile'):
        os.remove(settings.CURRENT_DIR+"/media/"+str(res.resumeFile))
        res.resumeFile=request.FILES.get('jsResumeFile')
      if 'jsResumeTitle' in request.POST:res.resumeTitle=request.POST.get('jsResumeTitle')
      res.save()
    return HttpResponse('')
def resumeactivation(request):
  if 'txtactres' in request.GET:
    txtres=JSTextResume.objects.get(user=request.user)
    if txtres.activetext_resume:txtres.activetext_resume=False
    else:txtres.activetext_resume=True
     #txtres.activetext_resume == 'false':txtres.activetext_resume=True
    txtres.save()
    if JSResumeActive.objects.filter(user=request.user):
      v=JSResumeActive.objects.get(user_id=request.user.id)
      activatedfile=v.resumeActive.resumeFile
      striped_file=str(activatedfile).replace('documents','').replace('/','').replace('.odt','').replace('.ODT','').replace('.docx','').replace('.DOCX','').replace('.doc','').replace('.DOC','').replace('.pdf','').replace('.PDF','').replace('.rtf','').replace('.RTF','').replace('.txt','').replace('.TXT','')
      os.remove(settings.CURRENT_DIR+"/tagging/templates/documents/"+str(striped_file)+".html")
      JSResumeActive.objects.filter(user=request.user).delete()
    return HttpResponse()
    #txtres.activetext_resume=
  if 'resumeid' in request.GET:
    activatedfile=""
    striped_file=""
    if JSTextResume.objects.filter(user=request.user):
      tr=JSTextResume.objects.get(user=request.user)
      tr.activetext_resume=False
      tr.save()
    if JSResumeActive.objects.filter(user=request.user):
      if JSResumeActive.objects.filter(resumeActive_id=request.GET['resumeid']):
        v=JSResumeActive.objects.get(user_id=request.user.id,resumeActive_id=request.GET['resumeid'])
        activatedfile=v.resumeActive.resumeFile
        v.delete()
      else:
        v=JSResumeActive.objects.get(user_id=request.user.id)
        activatedfile=v.resumeActive.resumeFile
        edit, created=JSResumeActive.objects.get_or_create(user_id=request.user.id)
        edit.JS_id=request.user.jsdetails.id
        edit.resumeActive_id=request.GET['resumeid']
        edit.save()
        res=JSResume.objects.get(id=request.GET['resumeid'],user=request.user)
        call(["unoconv","-f","html","-o",settings.CURRENT_DIR+"/tagging/templates/documents/",settings.CURRENT_DIR+"/media/"+str(res.resumeFile)])
      striped_file=str(activatedfile).replace('documents','').replace('/','').replace('.odt','').replace('.ODT','').replace('.docx','').replace('.DOCX','').replace('.doc','').replace('.DOC','').replace('.pdf','').replace('.PDF','').replace('.rtf','').replace('.RTF','').replace('.txt','').replace('.TXT','')
      os.remove(settings.CURRENT_DIR+"/tagging/templates/documents/"+str(striped_file)+".html")
      return HttpResponse('success')
    if not JSResumeActive.objects.filter(user=request.user):
      edit, created=JSResumeActive.objects.get_or_create(user_id=request.user.id)
      edit.JS_id=request.user.jsdetails.id
      edit.resumeActive_id=request.GET['resumeid']
      edit.save()
      res=JSResume.objects.get(id=request.GET['resumeid'],user=request.user)
      call(["unoconv","-f","html","-o",settings.CURRENT_DIR+"/tagging/templates/documents/",settings.CURRENT_DIR+"/media/"+str(res.resumeFile)])
      return HttpResponse('success')
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
    messages.success(request, 'Your profile has been updated successfully')
    return HttpResponseRedirect('/js/Dashboard/')    
  else:
    menus=['Resume','Personal Details','Educational Details','Technical Skill Set','Profile Summary','Employment Details','Project Details','Secret Clearance Section','Other Details']
    details = User.objects.filter(id=request.user.id)
    details1 = JSProfileSummary.objects.filter(user_id=request.user.id)
    return render(request,'jsprofile/ajaxhtmls/profilepic_update.html', {"details":details, "details1":details1,'navs':menus})
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
    return HttpResponseRedirect('/js/Dashboard/')
@user_passes_test(is_jobseeker,login_url='/accounts/login/')
def editresume(request):
  if request.POST['curform']=='textresumeform':
    if not JSDetails.objects.filter(user=request.user):JSDetails(user=request.user).save()
    tb,created=JSTextResume.objects.get_or_create(user=request.user,JS=request.user.jsdetails)
    tb.resumeFile=request.POST['resumeFile']
    tb.save()
    return HttpResponse()

def editpersonal(request):
  
  if request.POST['curform']=='profform':
    print "checked"
    u=User.objects.get(id=request.user.id)
    u.first_name=request.POST['first_name']
    u.save()
    
    if not JSDetails.objects.filter(user=request.user):JSDetails(user=request.user).save()
    tb,created=JSPersonal.objects.get_or_create(user=request.user,JS=request.user.jsdetails)
    tb.sec_email=request.POST['sec_email']
    tb.dob=request.POST['dob']
    tb.address1=request.POST['address1']
    tb.address2=request.POST['address2']
    tb.country=request.POST['country']
    tb.state=request.POST['state']
    tb.city=request.POST['city']
    tb.zipcode=request.POST['zipcode']
    tb.lat=request.POST['lat']
    tb.lng=request.POST['lng']
    tb.typ=request.POST['typ']
    tb.handno=request.POST['handno']
    tb.workno=request.POST['workno']
    tb.homeno=request.POST['homeno']
    tb.prefertime=request.POST['prefertime']
    tb.gender=request.POST['gender']
    tb.maritalstatus=request.POST['maritalstatus']
    tb.work_expyears=request.POST['work_expyears']
    tb.work_expmonths=request.POST['work_expmonths']
    tb.salaryrange=request.POST['salaryrange']
    tb.industry=request.POST['industry']
    tb.functional_area=request.POST['functional_area']
    if 'profileurl' in request.POST:
      p = request.POST['profileurl']
      #v=request.POST['profileurl'].replace('http://','').replace('www.','').replace('linkedin.','').replace('com/','').replace('com','')
      if not p.split("/")[-1]:
        v = p.split("/")[-2]
      else:
        v = p.split("/")[-1]
      if v:tb.profileurl='http://www.linkedin.com/'+v
      else:tb.profileurl=''     
      
      #v=re.sub(r'linkedin.com/','',request.POST['profileurl'])
      # v=request.POST['profileurl'].replace('http://www.linkedin.com/','')
      # v=request.POST['profileurl'].replace('www.linkedin.com/','')
      # v=request.POST['profileurl'].replace('http://linkedin.com/','')
      # v=request.POST['profileurl'].replace('linkedin.com/','')
      # v=request.POST['profileurl'].replace('http://www.linkedin.com','')
      # v=request.POST['profileurl'].replace('www.linkedin.com','')
      # v=request.POST['profileurl'].replace('http://linkedin.com','')
      # v=request.POST['profileurl'].replace('linkedin.com','')
      # if v:tb.profileurl='http://www.linked.com/'+v
      # else:tb.profileurl=''      
    tb.save()
    return HttpResponse()
def check_SecEmail(request):
  tag=0
  msg=''
  if 'sec_emailid' in request.GET and 'username' in request.GET:
    if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", request.GET['sec_emailid']) == None:
      tag=1
      msg='Enter the valid email ID'
    elif User.objects.filter(username=request.GET['username'],email=request.GET['sec_emailid']):
      tag=1
      msg='Sec.email not same as Pri.email'
    elif User.objects.filter(email=request.GET['sec_emailid']):
      tag=1
      msg='This email ID already exists'
    n=dict(tag=tag,msg=msg)
    return HttpResponse(json.dumps(n), mimetype="application/json")
  
def editsummary(request):
  if request.POST['curform']=='summaryform':
    if not JSDetails.objects.filter(user=request.user):JSDetails(user=request.user).save()
    tb,created=JSProfileSummary.objects.get_or_create(user=request.user,JS=request.user.jsdetails)
    tb.profile_summary=request.POST['profile_summary']
    tb.save()
    return HttpResponse()
def editsecret(request):
  if request.POST['curform']=='secretform':
    if not JSDetails.objects.filter(user=request.user):JSDetails(user=request.user).save()
    tb,created=JSsecurity.objects.get_or_create(user=request.user,JS=request.user.jsdetails)
    tb.jssecretclear=request.POST['jssecretclear']
    tb.jsfromdate=datetime.strptime(request.POST['jsfromdate'],"%m-%d-%Y")
    tb.jstodate=datetime.strptime(request.POST['jstodate'],"%m-%d-%Y")
    tb.save()
    return HttpResponse()
def editedu(request):
  if request.POST['curform']=='eduform':
    if not JSDetails.objects.filter(user=request.user):JSDetails(user=request.user).save()
    JSQualification(user=request.user,JS_id=request.user.jsdetails.id,degree=request.POST['degree'],special=request.POST['special'],institution=request.POST['institution'],location=request.POST['location'],year=request.POST['year'],country=request.POST['country']).save()
    return HttpResponse()
def editskill(request):
  if request.POST['curform']=='skillform':
    if not JSDetails.objects.filter(user=request.user):JSDetails(user=request.user).save()
    JSSkills(user=request.user,JS_id=request.user.jsdetails.id,skill=request.POST['skill'],version=request.POST['version'],lastused=request.POST['lastused'],skillyear=request.POST['skillyear'],skillmon=request.POST['skillmon']).save()
    return HttpResponse()
def editemp(request):
  if request.POST['curform']=='empform':
    if not JSDetails.objects.filter(user=request.user):JSDetails(user=request.user).save()
    if 'empstatus' in request.POST:
      JSEmployerDetails(user=request.user,JS_id=request.user.jsdetails.id,employer_name=request.POST['employer_name'],empstatus=request.POST['empstatus'],empstartdate=request.POST['empstartdate'],designation=request.POST['designation'],jobprofile=request.POST['jobprofile']).save()
    else:
      a=request.POST['empstartdate'].split(' to ')
      JSEmployerDetails(user=request.user,JS_id=request.user.jsdetails.id,employer_name=request.POST['employer_name'],empstatus=request.POST['Iscurrentjob'],empstartdate=a[0],emptodate=a[1],designation=request.POST['designation'],jobprofile=request.POST['jobprofile']).save()
    return HttpResponse()
def editproject(request):
  print request.POST, "dfdfg"
  if request.POST['curform']=='projectform':
    
    if not JSDetails.objects.filter(user=request.user):
      js = JSDetails(user=request.user).save()
    else :
      js = JSDetails.objects.filter(user=request.user)[0]
    
    sod = request.POST['projstartdate']
    tod = request.POST['projtodate']
    #JSProjectDetails(user=request.user,JSid=request.user.jsde = tails.id,client=request.POST['client'],project_title=request.POST['project_title'],projstartdate=a[0],projtodate=a[1],project_loc=request.POST['project_loc'],on_offsite=request.POST['on_offsite'],emp_type=request.POST['emp_type'],project_details=request.POST['project_details'],role_desc=request.POST['role_desc'],skill_used=request.POST['skill_used'],role=request.POST['role'],teamsize=request.POST['teamsize']).save()
    try : tval = JSProjectDetails(user=request.user,JS=js,client=request.POST['client'],project_title=request.POST['project_title'],projstartdate=sod,projtodate=tod,project_loc=request.POST['project_loc'],on_offsite=request.POST['on_offsite'],emp_type=request.POST['emp_type'],project_details=request.POST['project_details'],role_desc=request.POST['role_desc'],skill_used=request.POST['skill_used'],role=request.POST['role'],teamsize=request.POST['teamsize']).save()
    except Exception as e :
      print str(e)
    print tval, "prabha" 
  return HttpResponse()
def editlanguage(request):
  if request.POST['curform']=='languageform':
    if not JSDetails.objects.filter(user=request.user):JSDetails(user=request.user).save()
    JSLanguage(user=request.user,JS_id=request.user.jsdetails.id,language=request.POST['language'],proficiency=request.POST['proficiency'],read=request.POST['Read'],write=request.POST['Write'],speak=request.POST['Speak']).save()
    return HttpResponse()
def editotherdetails(request):
  if request.POST['curform']=='otherdetailsform':
    if not JSDetails.objects.filter(user=request.user):JSDetails(user=request.user).save()
    tb,created=JSDetailOther.objects.get_or_create(user=request.user,JS=request.user.jsdetails)
    tb.emptype=request.POST['emptype']
    tb.workpermit=request.POST['workpermit']
    for i in request.POST.keys():
      if i in ['workother']:
        wo=''
        for j in request.POST.getlist('workother'):
          wo+=j+','
          workother=wo[:-1]
          tb.workother=workother

    tb.relocate=request.POST['reloc']
    tb.telecommunicate=request.POST['telecom']
    tb.travel=request.POST['travel']
    for i in request.POST.keys():
      if i in ['relocatechoice']:
        rc=''
        for j in request.POST.getlist('relocatechoice'):
          rc+=j+','
          relocatechoice=rc[:-1]
          tb.relocatechoice=relocatechoice
    tb.save()
    return HttpResponse()
