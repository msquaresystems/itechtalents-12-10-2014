from datetime import datetime,timedelta
from celery.decorators import periodic_task
from django.template import Context, loader
from django.core.mail import send_mail, EmailMultiAlternatives
from registration.models import *
from django.contrib.auth.models import User
import urlparse
from math import sin, cos, radians, degrees, acos
from django.conf import settings
from geopy import geocoders
#gn = geocoders.GeoNames()#username=settings.GEONAMES_ORG_USERNAME)
gn = geocoders.GeoNames(username=settings.GEONAMES_ORG_USERNAME)
from email.mime.image import MIMEImage
from django.db.models import Q
@periodic_task(run_every=timedelta(seconds=86400))
def my_task():
    query=Q(marklive__lte=datetime.now().date()) & Q(todate__gte=datetime.now().date()) & Q(is_delete=False) & Q(is_active=True)
    for i in JSsavesearch.objects.all():
        urls=i.searchlink
        fname=i.user.first_name
        tomail=i.user.email
        searchname=i.searchname
        lastupdate=i.user.jsdetails.update_date
        p=urlparse.parse_qs(urls.split('?')[1])
        if p:
            if 'keywords' in p:
                list_result=[]
                str1 = ''.join(p['keywords'])
                s=str1.replace(' ','').replace(","," ")
                ss=s.split()
                for a in ss:
                    for res in jobs.objects.filter(Q(employerkeyskills__keyskills__icontains=a) | Q(title__icontains=a) | Q(city__icontains=a) | Q(state__icontains=a) | Q(country__icontains=a) | Q(zipcode__icontains=a),query):
                        if not res in list_result:
                            list_result.append(res)
            else:
                industry,functionalarea,jobtype,workpermit,salary_range,min_exp,max_exp,city,ranges,fromrange,torange,secretclear='','','','','','','','','','','',''
                if 'industry' in p:industry=p['industry'][0]
                if 'functionalarea' in p:functionalarea=p['functionalarea'][0]
                if 'jobtype' in p:jobtype=p['jobtype'][0]
                if 'workpermit' in p:workpermit=p['workpermit'][0]
                if 'salary_range' in p:salary_range=p['salary_range'][0]
                if 'min_exp' in p:min_exp=p['min_exp'][0]
                if 'max_exp' in p:max_exp=p['max_exp'][0]
                if 'city' in p:city=p['city'][0]
                if 'miles' in p:ranges=p['miles'][0]
                if 'secretclear' in p:secretclear=p['secretclear'][0]
                if 'fromrange' in p:fromrange=p['fromrange'][0]
                if 'torange' in p:torange=p['torange'][0]
                list_result=[]
                query=Q(industry__icontains=industry) | Q(functionalarea__icontains=functionalarea) | Q(jobtype=jobtype) | Q(workpermit=workpermit) | Q(salary_range=salary_range) | Q(empsecretclear=secretclear)
                if 'city' in p:
                    for res in jobs.objects.filter(Q(city__icontains=city) | Q(state__icontains=city) | Q(country__icontains=city) | Q(zipcode__icontains=city),query,is_active=True,is_delete=False):
                        if not res in list_result:list_result.append(res)
                if 'min_exp' in p and 'max_exp' in p:
                    for res in jobs.objects.filter(query,min_exp__gte=int(min_exp),max_exp__lte=int(max_exp),is_active=True,is_delete=False):
                        if not res in list_result:list_result.append(res)
                elif 'min_exp' in p:
                    for res in jobs.objects.filter(query,min_exp__gte=int(min_exp),is_active=True,is_delete=False):
                        if not res in list_result:list_result.append(res)
                elif 'max_exp' in p:
                    for res in jobs.objects.filter(query,max_exp__lte=int(max_exp),is_active=True,is_delete=False):
                        if not res in list_result:list_result.append(res)
                if 'fromrange' in p and 'torange' in p:
                    for res in jobs.objects.filter(query,marklive__gte=datetime.strptime(fromrange,"%m-%d-%Y").date(),marklive__lte=datetime.strptime(torange,"%m-%d-%Y").date(),is_active=True,is_delete=False):
                        if not res in list_result:list_result.append(res)
                elif 'fromrange' in p:
                    for res in jobs.objects.filter(query,marklive__gte=datetime.strptime(fromrange,"%m-%d-%Y").date(),is_active=True,is_delete=False):
                        if not res in list_result:list_result.append(res)
                elif 'torange' in p:
                    for res in jobs.objects.filter(query,marklive__lte=datetime.strptime(torange,"%m-%d-%Y").date(),is_active=True,is_delete=False):
                        if not res in list_result:
                            list_result.append(res)
                if 'key_skills' in p:
                    str1 = ''.join(p['key_skills'])
                    s=str1.replace(' ','').replace(","," ")
                    ss=s.split()
                    for a in ss:
                        for res in jobs.objects.filter(query,Q(employerkeyskills__keyskills__icontains=a) | Q(title__icontains=a),is_active=True,is_delete=False):
                            if not res in list_result:list_result.append(res)
                if 'miles' in p:
                    if 'city' in p:
                        results = Geocoder.geocode(city)
                        lat1=(results[0].coordinates)[0]
                        log1=(results[0].coordinates)[1]
                        result=[]
                        for i in list_result:
                            lon1, lat1, lon2, lat2 = map(radians, [log1, lat1, i.lng, i.lat])
                            dlon = lon2 - lon1
                            dlat = lat2 - lat1
                            a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
                            c = 2 * asin(sqrt(a))
                            mi = 3959 * c
                            if int(mi) <= int(radius):result.append(i)
                        list_result=result
        current_domain = Site.objects.get_current().domain
        contxt=Context({'d':list_result,'fname':fname,'searchname':searchname,'now':datetime.now().date(),'lastupdate':lastupdate,'current_domain':current_domain})
        message_template = loader.get_template('registration/job_alert_mail.html')
        message=message_template.render(contxt)
        msg=EmailMultiAlternatives('iTechTalents.com Job Alerts',message,'itechtalentalerts@itechtalents.com',[tomail])
        msg.attach_alternative(message, "text/html")
        msg.send()
        continue
@periodic_task(run_every=timedelta(seconds=86400))
def my_task1():
    for j in RecSaveSearch.objects.all():
        urls=j.savedsearch
        name=j.searchname
        fname=j.employer.companyname
        tomail=j.employer.email
        p=urlparse.parse_qs(urls.split('?')[1])
        if p:
            if 'keywords' in p:
                query_visibility = Q(jsdetails__visiblity=True) | Q(jsdetails__visiblepassive=True)
                list_result=[]
                str1 = ''.join(p['keywords'])
                s=str1.replace(' ','').replace(","," ")
                ss=s.split()
                for a in ss:
                    for res in User.objects.filter(Q(jsskills__skill__icontains=a) | Q(jspersonal__zipcode__icontains=a) | Q(jspersonal__country__icontains=a) | Q(jspersonal__state__icontains=a) | Q(jspersonal__city__icontains=a) | Q(jsdetailother__relocatechoice__icontains=a),query_visibility):
                        if not res in list_result:
                            list_result.append(res)
            else:
                key_skills,functional_area,emp_type,workpermit,telecommute,min_exp,max_exp,location,miles='','','','','','','','',''
                if 'functional_area' in p:functional_area=p['functional_area']
                if 'emp_type' in p:emp_type=p['emp_type']
                if 'workpermit' in p:workpermit=p['workpermit']
                if 'telecommute' in p:telecommute=p['telecommute']
                if 'min_exp' in p:min_exp=p['min_exp']
                if 'max_exp' in p:max_exp=p['max_exp']
                if 'location' in p:location=p['location']
                if 'miles' in p:miles=p['miles']
                query=Q(jspersonal__functional_area=functional_area) | Q(jsdetailother__emptype=emp_type) | Q(jsdetailother__workpermit=workpermit) | Q(jsdetailother__telecommunicate=telecommute)
                list_result=[]
                if 'key_skills' in p:
                    str1 = ''.join(p['key_skills'])
                    s=str1.replace(' ','').replace(","," ")
                    ss=s.split()
                    for a in ss:
                        for res in User.objects.filter(query,Q(jsskills__skill__icontains=a),jsdetails__visiblepassive=True,jsdetails__visiblity=True):
                            if not res in list_result:list_result.append(res)
                if 'location' in p:
                    for res in User.objects.filter(query,Q(jspersonal__state__icontains=p['location']) | Q(jspersonal__city__icontains=p['location']) | Q(jspersonal__country__icontains=p['location']) | Q(jspersonal__zipcode__icontains=p['location']) | Q(jsdetailother__relocatechoice__icontains=p['location']),jsdetails__visiblepassive=True,jsdetails__visiblity=True):
                        if not res in list_result:list_result.append(res)
                if 'work_expmin' in p and 'work_expmax' in p:
                    for res in User.objects.filter(query,jspersonal__work_expyears__gte=work_expmin,jspersonal__work_expyears__lte=work_expmax,jsdetails__visiblity=True,jsdetails__visiblepassive=True):
                        if not res in list_result:list_result.append(res)
                elif 'work_expmin' in p:
                    for res in User.objects.filter(query,jspersonal__work_expyears__gte=work_expmin,jsdetails__visiblity=True,jsdetails__visiblepassive=True):
                        if not res in list_result:list_result.append(res)
                elif 'work_expmax' in p:
                    for res in User.objects.filter(query,jspersonal__work_expyears__lte=work_expmax,jsdetails__visiblity=True,jsdetails__visiblepassive=True):
                        if not res in list_result:list_result.append(res)
                if 'miles' in p:
                    if 'location' in p:
                        results = Geocoder.geocode(location)
                        lat1=(results[0].coordinates)[0]
                        log1=(results[0].coordinates)[1]
                        result=[]
                        for i in list_result:
                            lon1, lat1, lon2, lat2 = map(radians, [log1, lat1, i.lng, i.lat])
                            dlon = lon2 - lon1
                            dlat = lat2 - lat1
                            a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
                            c = 2 * asin(sqrt(a))
                            mi = 3959 * c
                            if int(mi) <= int(radius):result.append(i)
                        list_result=result
            current_domain = Site.objects.get_current().domain
            contxt=Context({'d':list_result,'fname':fname,'searchname':name,'now':datetime.now().date(),'current_domain':current_domain})
            message_template = loader.get_template('registration/new_matching_profile_alert.html')
            message=message_template.render(contxt)
            msg=EmailMultiAlternatives('iTechTalents.com Job Alerts',message,'itechtalentalerts@itechtalents.com',[tomail])
            msg.attach_alternative(message, "text/html")
            msg.send()
            continue            
@periodic_task(run_every=timedelta(seconds=86400))
def deactivate_employerpack():
    for subscribe in emppack_activation.objects.all():
        if subscribe.is_active:
            for pack in emp_subscribed_packs.objects.filter(id=subscribe.subscribed_pack_id):
                p=pack.pack_expire
                now=datetime.now().date()
                if p.date() <= now:
                    deactivate=emppack_activation.objects.get(subscribed_pack_id=pack.id)
                    deactivate.is_active=False
                    deactivate.totaljobpost=0
                    deactivate.totalresume=0
                    deactivate.save()
@periodic_task(run_every=timedelta(seconds=86400))
def deactivate_alertemppack():
    for subscribe in emppack_activation.objects.all():
        if subscribe.is_active:
            for pack in emp_subscribed_packs.objects.filter(id=subscribe.subscribed_pack_id):
                s=pack.pack_expire
                now=datetime.now().date()
                if s.date()-timedelta(days=23) == now:
                    current_domain = Site.objects.get_current().domain
                    contxt=Context({'activate':pack.pack_activate,'deactivate':pack.pack_expire,'packname':pack.pack.pack_name,'username':pack.employer.username,'companyname':pack.employer.companyname,'now':datetime.now().date(),'current_domain':current_domain})
                    message_template = loader.get_template('registration/packactivation_alertmail.html')
                    message=message_template.render(contxt)
                    msg=EmailMultiAlternatives('iTechTalents.com Pack Deactivation Alerts',message,'itechtalentalerts@itechtalents.com',[pack.employer.email])
                    msg.attach_alternative(message, "text/html")
                    msg.send()
                continue
@periodic_task(run_every=timedelta(seconds=86400))
def deactivate_activatejob():
    for job in jobs.objects.all():
        if job.is_active:
            j=job.todate.date()
            if j < datetime.now().date():
                job.is_active=False
                job.save()
            continue
@periodic_task(run_every=timedelta(seconds=86400))
def account_deactivate():
    for usr in User.objects.filter(is_active=False):
        dj=usr.date_joined
        d=dj+timedelta(hours=72)
        if datetime.now() > d:User.objects.filter(id=usr).delete()
