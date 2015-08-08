# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,render_to_response
from django.contrib.auth.decorators import user_passes_test
from addressbook.models import AddressBook
import json
#from jobseeker.views import usertype_check
##---addressbook-----
#employer/pages/lettertemplates/addressbook.html
#@user_passes_test(usertype_check,login_url='/accounts/login/employer/')
def addressbk(request):
	if request.GET:
		task=request.GET['task']
		if task=='del':
			print "delete"
			print request.GET['fid']
			ad=AddressBook.objects.get(pk=request.GET['fid']).delete()
			return HttpResponse('deleted')
		elif task=='edit':ad=AddressBook.objects.get(pk=request.GET['fid'])
		elif task=='add':ad=AddressBook(user=request.user)
		elif task=='exist':
			if request.GET['fid']:
				for a in AddressBook.objects.exclude(id=request.GET['fid']).filter(user=request.user):
					if a.email != request.GET['vals']:n={'vals':1,'msg':''}
					else:n={'vals':0,'msg':'Email already exist'}
			elif AddressBook.objects.filter(email=request.GET['vals'],user=request.user):n={'vals':0,'msg':'Email already exist'}
			else:n={'vals':1,'msg':''}
			return HttpResponse(json.dumps(n), mimetype="application/json")
		ad.name=request.GET['name']
		ad.email=request.GET['email']
		ad.phone=request.GET['phone']
		ad.fax=request.GET['fax']
		try:
			ad.save()
			fid=ad.pk
		except:fid=''
		return HttpResponse(fid)#json.dumps(n), mimetype="application/json")
	#user,name,link
	ad=AddressBook.objects.filter(user=request.user)
	return render(request,'lettertemplates/addressbook.html',{'addressitems':ad})
