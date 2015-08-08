# Create your views here.
from lettertemplate.models import LetterTemplate,SendLetters
from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from lettertemplate.forms import LetterTemplateForm
from django.contrib import messages

def home(request):
	tp=LetterTemplate.objects.filter(employer=request.user)
	return render(request,'lettertemplates/home.html',{'lettertemplates':tp})

def templateAddEditDel(request,task):
	if task == 'del':
		LetterTemplate.objects.get(id=request.GET['id']).delete()
		messages.success(request, 'Template has been deleted successfully')
		return HttpResponseRedirect("/accounts/RecruiterDashboard/")
	elif task=='edit':
		tempid=request.GET['id']
		let=LetterTemplate.objects.get(id=tempid)
		frm_let=LetterTemplateForm(instance=let)

	elif task=='add':
		frm_let=LetterTemplateForm()
		tempid=''
	return render(request,'lettertemplates/createtemplate.html',{'form':frm_let,'tempid':tempid})

def createtemplate(request):	
	if request.method=='POST':
		form = LetterTemplateForm(request.POST)
		if form.is_valid():
			#return HttpResponse('dsfsd')
			if 'tempid' in request.POST:p=LetterTemplate.objects.get(id=request.POST['tempid'])
			else:p=LetterTemplate(employer=request.user)
			fp=LetterTemplateForm(request.POST,instance=p)
			fp.save()
			messages.success(request, 'Template has been saved successfully')
			return HttpResponseRedirect('/accounts/RecruiterDashboard/')

def composeletter(request):
	form = LetterTemplateForm()
	tp=LetterTemplate.objects.filter(employer=request.user)
	d=dict(lettertemplates=tp,form=form)
	if request.POST:
		selKeys=request.POST['selkeys']
		if selKeys:
			from addressbook.models import AddressBook
			selmails=[]
			for i in selKeys.split(','):
				selmails.append(AddressBook.objects.get(id=i))
			d['selmails']=selmails
	return render(request,'lettertemplates/composeletter.html',d)

def sendletter(request):	
	if request.POST:
		bademails=request.POST['emails'] #it might contain ','
		emails=bademails[:-1] if bademails[-1] == ',' else bademails
		title=request.POST['title']
		subject=request.POST['subject']
		message=request.POST['body']
		from_email=request.user.email
		from django.core.mail import send_mail, BadHeaderError,EmailMessage
		try:
			msg=EmailMessage(subject, message, from_email,emails.split(','))
			msg.content_subtype="html"
			msg.send()
		except BadHeaderError:
			return HttpResponse('Invalid header found.')			
		SendLetters(employer=request.user,title=title,subject=subject,body=message,sendto=emails).save()
		return HttpResponseRedirect('/accounts/RecruiterDashboard/?next=2')	
	if 'del' in request.GET: 
		try:SendLetters.objects.get(id=request.GET['del']).delete()
		except:HttpResponse('Sorry Page not exist')
		return HttpResponseRedirect('/accounts/RecruiterDashboard/?next=2')
	senditems=SendLetters.objects.filter(employer=request.user)	
	return render(request,'lettertemplates/sendletters.html',{'items':senditems})