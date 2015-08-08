# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,render_to_response
from django.contrib.auth.decorators import user_passes_test
from addressbook.models import AddressBook
#from jobseeker.views import usertype_check
##---addressbook-----
#employer/pages/lettertemplates/addressbook.html
#@user_passes_test(usertype_check,login_url='/accounts/login/employer/')
def addressbk(request):
	if request.GET:
		task=request.GET['task']
		if task=='del':
			ad=AddressBook.objects.get(pk=request.GET['fid']).delete()
			return HttpResponse('deleted')
		elif task=='edit':ad=AddressBook.objects.get(pk=request.GET['fid'])
		elif task=='add':ad=AddressBook(user=request.user)
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