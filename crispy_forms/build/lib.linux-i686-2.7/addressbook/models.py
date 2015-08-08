from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class AddressBook(models.Model):	
	user=models.ForeignKey(User)
	name=models.CharField(max_length=100)#, blank=True)
	email=models.EmailField(max_length=100)
	phone=models.CharField(max_length=20, blank=True)
	fax=models.CharField(max_length=20, blank=True)