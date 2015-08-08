
#then goto main directory(ie directory contains manage.py)
#then execute $: python manage.py shell
#you will enter into python shell >>
# >>> import cii
# >>> cii.initd()
from django.contrib.auth.models import User
# from initfixtures import TOPICS_DATA,USERS_DATA,QUESTIONS_DATA,ANSWERS_DATA,FEEDLINKS
# from quorum import models
# from registration.models import EmployerReg_Form
# def add_topics(M):
# 	#topics
# 	for i in TOPICS_DATA:
# 		p=M.Topic(creator_id=1,topic=i[0],imgurl=i[1])
# 		p.save()

# def add_questions(M):
# 	#Question(user, topic, question)
# 	for i in QUESTIONS_DATA:
# 		usr=User.objects.get(username=i[0])
# 		tp=M.Topic.objects.get(pk=i[1])
# 		p=M.Question(user=usr,topic=tp,question=i[2])
# 		p.save()

# def add_answers(M):
# 	#Answer(user,question,answer)
# 	for i in ANSWERS_DATA:
# 		usr=User.objects.get(username=i[0])
# 		qst=M.Question.objects.get(pk=i[1])
# 		p=M.Answer(user=usr,question=qst,answer=i[2])
# 		p.save()



# def add_users():
# 	#USERS_DATA=[['js','suhailvs@gmail.com','jobseeker'],
# 	##['emp','jani@gmail.com','employer']
# 	#]
	
# 	for i in USERS_DATA:
# 		p=User.objects.create_user(username=i[0],email=i[1],
# 			password='s')#,first_name=i[2],last_name=i[3])
# 		p.is_activate = True
# 		p.save()
# 		if i[2] in ['employer','jobseeker']:
# 			p.usertype=i[2]
# 		else:
# 			ust={'e':'employer','j':'jobseeker'}
# 			p.usertype=ust[i[4]]


# 		p.save()
# 		if i[4]=='e':
# 			#from registration.models import EmployerReg_Form
# 			emt=EmployerReg_Form(user=p,companytype='Company',contactno='99',contactperson=i[2],companyurl="http://sample.com")
# 			emt.save()
# 		#if i[4]=='e':p1=Employer(user=p)
# 		#else:p1=Jobseeker(user=p)
# 		#p1.save()

def add_feedlinks():
	from initfixtures import FEEDLINKS
	from feeds.models import FeedList
	for i in FEEDLINKS:
		fd=FeedList(name=i[0],link=i[1])
		fd.save()

def initd():
	#add_topics(models)
	#add_users()
	#add_questions(models)
	#add_answers(models)
	add_feedlinks()
def idt():
	from feeds.models import UsrFeeds
	for i in FEEDLINKS:
		fd=UsrFeeds(user=User.objects.get(username='s'),name=i[0],link=i[1])
		fd.save()