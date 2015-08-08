# Create your views here.
#from feeds.furls import filtered_urls
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import json
from feeds.models import UsrFeeds,FeedList

def guest(request):
	fds=FeedList.objects.all()
	if 'feedid' in request.GET:curfeed=int(request.GET['feedid'])
	else:curfeed=fds[0].id
	return render(request,'feed/guest.html',{'feedlist':fds,'url':fds.get(id=curfeed)})

@login_required(login_url='/feeds/guest/')
def home(request):	
	if 'multisel' in request.POST:	 
		sel_feeds=[int(i) for i in request.POST.getlist('multisel')]
		to_dels=set([f.feed.id for f in UsrFeeds.objects.filter(user=request.user)])-set(sel_feeds)
		for to_del in list(to_dels):
			UsrFeeds.objects.get(user=request.user,feed__id=to_del).delete()

		#return HttpResponse(list(to_del))
		for feedid in request.POST.getlist('multisel'):
			newfeed=FeedList.objects.get(id=feedid)			
			if not newfeed.have_feed(request.user):
				fd_to_save=UsrFeeds(user=request.user,feed=newfeed)
				fd_to_save.save()

	fd=UsrFeeds.objects.filter(user=request.user)	# to fill the side bar
	
	if not fd: return render(request,'feed/home.html')
	if 'feedid' in request.GET:curfeed=FeedList.objects.get(id=int(request.GET['feedid']))	#show a perticular feed
	else:curfeed=fd[0].feed
	return render(request,'feed/home.html',{'feedlist':fd,'url':curfeed})

def settrans(request):	
	if 'trans' in request.GET:
		request.session['django_language'] = request.GET['trans']
		output = 't'
	else: output='f'
	return HttpResponse(output)