from django import template
from quorum.models import Topic,Followings, Question,Favourites
from django.contrib.auth.models import User

register = template.Library()

@register.filter(name='find_total_score')
def totscore(value):
	total=0
	for rr in value:total+=int(rr.score)
	return total

@register.filter(name='topic_following')
def is_user_following_topic(value,arg):
	try:
		tp=Topic.objects.get(id=int(value))
		usr=User.objects.get(id=int(arg))
		Followings.objects.get(user=usr,topic=tp)
		return 'btn-success'
	except:
		return 'btn-inverse'

@register.filter
def question_count(value):
	try:
		tp_pk=int(value)
		return Question.objects.topicspecific_count(tp_pk)
	except:
		return 0

@register.simple_tag
def question_last(pval):
	tp_pk=int(pval)
	quest=Question.objects.get_last_question(tp_pk)
	if quest:
		dt=quest.created.strftime("%A, %d. %B %Y %I:%M%p")
		qst=quest.question
		if len(qst)>103: qst=qst[:100]+'...'
		str_q="<p>%s.</p><p><small>(%s)</small></p>" %(qst,dt)		
	else:str_q="<p>No Questions Found.<p>"
	return str_q

@register.simple_tag
def user_following_topics(usr_pk):
	usr=User.objects.get(pk=int(usr_pk))
	#tp=Topic.objects.get(id=int(tp_pk))
	follows=Followings.objects.filter(user=usr)
	str_r=""
	for f in follows:
		str_tp="<a href='/quorum/topic/%s/'>%s</a><br>" %(f.topic.pk,f.topic.topic)
		str_r+=str_tp
	return str_r

@register.simple_tag
def user_favourites(usr_pk):
	usr=User.objects.get(pk=int(usr_pk))
	#tp=Topic.objects.get(id=int(tp_pk))
	favs=Favourites.objects.filter(user=usr)
	str_r=""
	for f in favs:
		qst=f.question.question
		if len(qst)>103: qst=qst[:100]+'...'
		str_fv="<a href='/quorum/question/%s/'>%s</a><br>" %(f.question.pk,qst)
		str_r+=str_fv
	return str_r

@register.filter(name='nrounds') 
def nrounds(value):
    return range(int(value))

@register.filter(name='commetcount') 
def commetcount(value):
    return range(int(value))

