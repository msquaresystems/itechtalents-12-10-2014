from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class LetterTemplate(models.Model):
    employer = models.ForeignKey(User)
    title = models.CharField(max_length=100, blank=True)
    replayto=models.CharField(max_length=200, blank=True,verbose_name="Reply To")
    #autoresponse=models.BooleanField(default=False)
    subject=models.CharField(max_length=100,blank=True)
    body=models.TextField()

class SendLetters(models.Model):
	employer = models.ForeignKey(User)
	title = models.CharField(max_length=100, blank=True)
	replayto=models.CharField(max_length=200, blank=True,verbose_name="Reply To")
	sendto= models.CharField(max_length=100, blank=True)
	subject=models.CharField(max_length=100,blank=True)
	body=models.TextField()	
	date=models.DateTimeField(auto_now=True)

from django.contrib import admin
admin.site.register(LetterTemplate)
admin.site.register(SendLetters)
