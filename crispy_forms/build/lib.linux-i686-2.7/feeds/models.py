from django.db import models
from django.contrib import admin

class FeedList(models.Model):
	name=models.CharField(max_length=50, blank=True)
	link=models.CharField(max_length=100, blank=True)#

	#checks weather user have the feed
	def have_feed(self,usr):
		#fd=UsrFeeds.objects.filter(user=usr)
		return self in [fd.feed  for fd in UsrFeeds.objects.filter(user=usr)]

from django.contrib.auth.models import User

class UsrFeeds(models.Model):
	user=models.ForeignKey(User)
	feed=models.ForeignKey(FeedList)

