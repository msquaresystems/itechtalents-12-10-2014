#usage
#---------

# commet out these lines in file quorum/models
# admin.site.register(Topic)
#open cmd. 
#then goto main directory(ie directory contains manage.py)
#then execute $: python manage.py shell
#you will enter into python shell >>
# >>> import cii
# >>> cii.initd()


# now uncommet these lines in file quorum/models
# admin.site.register(Topic)
#
# now uncommet these in registration/models 
# admin.site.register(Employer), admin.site.register(Jobseeker)

from quorum import models

from django.contrib.auth.models import User
from registration.models import Employer, Jobseeker

from initfixtures import TOPICS_DATA,USERS_DATA,QUESTIONS_DATA,ANSWERS_DATA
def add_topics(M):
	#topics
	for i in TOPICS_DATA:
		p=M.Topic(topic=i[0],imgurl=i[1])
		p.save()

def add_users(M):
	for i in USERS_DATA:
		p=User.objects.create_user(username=i[0],email=i[1],
			password='s')#,first_name=i[2],last_name=i[3])
		p.is_staff = True
		p.save()
		if i[4]=='e':p1=Employer(user=p)
		else:p1=Jobseeker(user=p)
		p1.save()


def add_questions(M):
	#Question(user, topic, question)
	for i in QUESTIONS_DATA:
		usr=User.objects.get(username=i[0])
		tp=M.Topic.objects.get(pk=i[1])
		p=M.Question(user=usr,topic=tp,question=i[2])
		p.save()

def add_answers(M):
	#Answer(user,question,answer)
	for i in ANSWERS_DATA:
		usr=User.objects.get(username=i[0])
		qst=M.Question.objects.get(pk=i[1])
		p=M.Answer(user=usr,question=qst,answer=i[2])
		p.save()

def add_letter_templates():
	from initfixtures import LETTERTEMPLATES
	from lettertemplate.models import LetterTemplate
	for i in LETTERTEMPLATES:
		usr=User.objects.get(username=i[0])
		tpl=LetterTemplate(employer=usr.employer,title=i[1],subject="just testing",body=i[2])
		tpl.save()

def add_captcha():
	from initfixtures import CAPTCHAS
	from captcha.models import Captcha
	for i in CAPTCHAS:
		cp=Captcha(question=i[0],answer=i[1])
		cp.save()

def add_feedlinks():
	from initfixtures import FEEDLINKS
	from feeds.models import FeedList
	for i in FEEDLINKS:
		fd=FeedList(name=i[0],link=i[1])
		fd.save()

def initd():
	add_topics(models)
	add_users(models)
	add_questions(models)
	add_answers(models)
	add_letter_templates()
	add_captcha()
	add_feedlinks()




#----------captca from website---------------
def initcaps(n=10):
	import re,urllib
	fp=open('captchas.txt','a')
	for i in range(n):
		try:
			qst=urllib.urlopen('http://api.textcaptcha.com/47v6jb6y8zgg8ok0kcwg88gok2qk6je9').readlines()
			q=re.match('<captcha><question>(.+)</question>',qst[0]).group(1)
			fp.write('("'+q.replace('"',"'")+'",""),\n')
		except:continue
	fp.close()