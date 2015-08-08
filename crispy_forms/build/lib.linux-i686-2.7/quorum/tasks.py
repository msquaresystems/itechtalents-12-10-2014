import datetime
from datetime import timedelta

from celery.decorators import periodic_task
from django.template import Context, loader
from django.core.mail import send_mail, EmailMultiAlternatives
from registration.models import *
from django.contrib.auth.models import User
import urlparse
from math import sin, cos, radians, degrees, acos
from geopy import geocoders
gn = geocoders.GeoNames()
from email.mime.image import MIMEImage
@periodic_task(run_every=timedelta(seconds=20))
def my_task():
    now=datetime.datetime.now()
    query1=Q(marklive__lte=now) & Q(todate__gte=now)
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
                for search in p['keywords'][0].split(','):
                    if search=='':continue
                    for res in jobs.objects.filter(Q(employerkeyskills__keyskills__icontains=search) | Q(title__icontains=search) | Q(city__icontains=search) | Q(state__icontains=search) | Q(country__icontains=search) | Q(zipcode__icontains=search),query1):
                        if not res in list_result:
                            list_result.append(res)
                details=list_result
            else:
                indus=''
                funca=''
                jobty=''
                worpr=''
                qualf=''
                sarng=''
                minex=''
                maxex=''
                city=''
                ranges=''
                if 'industry' in p:
                    indus=p['industry'][0]
                if 'functionalarea' in p:
                    funca=p['functionalarea'][0]
                if 'jobtype' in p:
                    jobty=p['jobty'][0]
                if 'workpermit' in p:
                    worpr=p['workpermit'][0]
                if 'qualification' in p:
                    qualf=p['qualification'][0]
                if 'salary_range' in p:
                    sarng=p['salary_range'][0]
                if 'min_exp' in p:
                    minex=p['min_exp'][0]
                if 'max_exp' in p:
                    maxex=p['max_exp'][0]
                if 'city' in p:
                    city=p['city'][0]
                if 'miles' in p:
                    ranges=p['miles'][0]
                list_result=[]
                if 'key_skills' in p:
                    for search in p['key_skills'][0].split(','):
                        if search=='':continue
                        if 'min_exp' in p and 'max_exp' in p:
                            query=Q(employerkeyskills__keyskills__icontains=search) & Q(functionalarea__icontains=funca) & Q(industry__icontains=indus) & Q(jobtype__icontains=jobty) & Q(workpermit__icontains=worpr) & Q(qualification__icontains=qualf) & Q(salary_range__icontains=sarng) & Q(min_exp__gte=int(minex)) & Q(max_exp__lte=int(maxex))
                            for res in jobs.objects.filter(query,query1):
                                print res.title
                                if not res in list_result:
                                    list_result.append(res)
                        elif 'max_exp' in p:
                            query=Q(employerkeyskills__keyskills__icontains=search) & Q(functionalarea__icontains=funca) & Q(industry__icontains=indus) & Q(jobtype__icontains=jobty) & Q(workpermit__icontains=worpr) & Q(qualification__icontains=qualf) & Q(salary_range__icontains=sarng) & Q(max_exp__lte=int(maxex))
                            for res in jobs.objects.filter(query,query1):
                                print res.title
                                if not res in list_result:
                                    list_result.append(res)
                        elif 'min_exp' in p:
                            query=Q(employerkeyskills__keyskills__icontains=search) & Q(functionalarea__icontains=funca) & Q(industry__icontains=indus) & Q(jobtype__icontains=jobty) & Q(workpermit__icontains=worpr) & Q(qualification__icontains=qualf) & Q(salary_range__icontains=sarng) & Q(min_exp__gte=int(minex))
                            for res in jobs.objects.filter(query,query1):
                                print res.title
                                if not res in list_result:
                                    list_result.append(res)
                        else:
                            query=Q(employerkeyskills__keyskills__icontains=search) & Q(functionalarea__icontains=funca) & Q(industry__icontains=indus) & Q(jobtype__icontains=jobty) & Q(workpermit__icontains=worpr) & Q(qualification__icontains=qualf) & Q(salary_range__icontains=sarng)
                            for res in jobs.objects.filter(query,query1):
                                print res.title
                                if not res in list_result:
                                    list_result.append(res)
                if not 'key_skills' in p:
                    if 'min_exp' in p and 'max_exp' in p:
                        query=Q(functionalarea__icontains=funca) & Q(industry__icontains=indus) & Q(jobtype__icontains=jobty) & Q(workpermit__icontains=worpr) & Q(qualification__icontains=qualf) & Q(salary_range__icontains=sarng) & Q(min_exp__gte=int(minex)) & Q(max_exp__lte=int(maxex))
                        for res in jobs.objects.filter(query,query1):
                            print res.title
                            if not res in list_result:
                                list_result.append(res)
                    elif 'max_exp' in p:
                        query=Q(functionalarea__icontains=funca) & Q(industry__icontains=indus) & Q(jobtype__icontains=jobty) & Q(workpermit__icontains=worpr) & Q(qualification__icontains=qualf) & Q(salary_range__icontains=sarng) & Q(max_exp__lte=int(maxex))
                        for res in jobs.objects.filter(query,query1):
                            print res.title
                            if not res in list_result:
                                list_result.append(res)
                    elif 'min_exp' in p:
                        query=Q(functionalarea__icontains=funca) & Q(industry__icontains=indus) & Q(jobtype__icontains=jobty) & Q(workpermit__icontains=worpr) & Q(qualification__icontains=qualf) & Q(salary_range__icontains=sarng) & Q(min_exp__gte=int(minex))
                        for res in jobs.objects.filter(query,query1):
                            print res.title
                            if not res in list_result:
                                list_result.append(res)
                    else:
                        query=Q(functionalarea__icontains=funca) & Q(industry__icontains=indus) & Q(jobtype__icontains=jobty) & Q(workpermit__icontains=worpr) & Q(qualification__icontains=qualf) & Q(salary_range__icontains=sarng)
                        for res in jobs.objects.filter(query,query1):
                            print res.title
                            if not res in list_result:
                                list_result.append(res)
                    
                    for res in jobs.objects.filter(query,query1):
                        print res.title
                        if not res in list_result:
                            list_result.append(res)

                details=list_result
                if ranges:
                    if city:
                        latlng=gn.geocode(city, exactly_one=False)[0]
                        result=[]
                        for i in details:
                            lats=i.lat
                            rlat=radians(float(lats))
                            slat=radians(latlng[1][0])
                            long_diff = radians(float(i.lng) - latlng[1][1])
                            distance = (sin(rlat) * sin(slat) + cos(rlat) * cos(slat) * cos(long_diff))
                            distance=degrees(acos(distance)) * 69.09
                            if distance <= int(ranges):
                                result.append(i)
                        details=result                    

            contxt=Context({'d':details,'fname':fname,'searchname':searchname,'now':now,'lastupdate':lastupdate})            
            message_template = loader.get_template('registration/job_alert_mail.html')    
            message=message_template.render(contxt)
            msg=EmailMultiAlternatives('iTechTalents.com Job Alerts',message,'itechtalentalerts@itechtalents.com',[tomail])
            msg.attach_alternative(message, "text/html")
            msg.send()
@periodic_task(run_every=timedelta(seconds=20))
def my_task1():
    now=datetime.datetime.now()
    d1=datetime.datetime(now.year, now.month, now.day)
    d2=datetime.datetime(now.year, now.month, now.day-1)
    fd=d1.strftime('%m-%d-%Y')
    td=d2.strftime('%m-%d-%Y')
    query1=Q(marklive__lte=fd) & Q(todate__gte=fd)
    for j in RecSaveSearch.objects.all():
        urls=j.savedsearch
        name=j.searchname
        fname=j.employer.companyname
        tomail=j.employer.email
        p=urlparse.parse_qs(urls.split('?')[1])
        if p:
            if 'keywords' in p:
                list_result=[]
                query_visibility = Q(jsdetails__visiblity=True) | Q(jsdetails__visiblepassive=True)
                for search in p['keywords'][0].split(','):
                    if search=='':continue
                    for res in User.objects.filter(Q(jsskills__skill__icontains=search) | Q(jspersonal__zipcode__icontains=search) | Q(jspersonal__country__icontains=search) | Q(jspersonal__state__icontains=search) | Q(jspersonal__city__icontains=search) | Q(jsdetailother__relocatechoice__icontains=search),query_visibility):
                        if not res in list_result:
                            list_result.append(res)
                details=list_result
            else:
                list_result=[]
                functionalarea=''
                emptype=''
                work_permit=''
                city=''
                minexp=''
                maxexp=''
                tele_commute=''
                ranges=''
                if 'functional_area' in p:
                    functionalarea=p['functional_area'][0]
                if 'emp_type' in p:
                    emptype=p['emp_type'][0]
                if 'workpermit' in p:
                    work_permit=p['workpermit'][0]
                if 'location' in p:
                    city=p['location'][0]
                if 'min_exp' in p:
                    minexp=p['min_exp'][0]
                if 'max_exp' in p:
                    maxexp=p['max_exp'][0]
                if 'telecommute' in p:
                    tele_commute=p['telecommute'][0]
                if 'miles' in p:
                    ranges=p['miles'][0]
                query_function = Q(jspersonal__functional_area__icontains=functionalarea)
                query_jobtype = Q(jsdetailother__emptype__icontains=emptype)
                query_workpermit = Q(jsdetailother__workpermit__icontains=work_permit)
                query_loc = Q(jspersonal__state__icontains=city) | Q(jspersonal__city__icontains=city) | Q(jspersonal__country__icontains=city) | Q(jspersonal__zipcode__icontains=city) | Q(jsdetailother__relocatechoice__icontains=city)
                query_workexp = Q(jspersonal__work_expyears__gte=minexp) & Q(jspersonal__work_expyears__lte=maxexp)
                query_visibility = Q(jsdetails__visiblity=True) | Q(jsdetails__visiblepassive=True)
                query_telecomute=Q(jsdetailother__telecommunicate__icontains=tele_commute)
                if 'key_skills' in p:
                    for search in p['key_skills'][0].split(','):
                        if minexp and maxexp:
                            for res in User.objects.filter(Q(jsskills__skill__icontains=search),query_function,query_jobtype,query_workpermit,query_workexp,query_loc,query_telecomute,query_visibility):
                                if not res in list_result:
                                    list_result.append(res)
                        elif minexp:
                            for res in User.objects.filter(Q(jsskills__skill__icontains=search),query_function,query_jobtype,query_workpermit,Q(jspersonal__work_expyears__gte=minexp),query_loc,query_telecomute,query_visibility):
                                if not res in list_result:
                                    list_result.append(res)
                        elif maxexp:
                            for res in User.objects.filter(Q(jsskills__skill__icontains=search),query_function,query_jobtype,query_workpermit,Q(jspersonal__work_expyears__lte=maxexp),query_loc,query_telecomute,query_visibility):
                                if not res in list_result:
                                    list_result.append(res)
                        else:
                            for res in User.objects.filter(Q(jsskills__skill__icontains=search),query_function,query_jobtype,query_workpermit,query_telecomute,query_loc,query_visibility):
                                if not res in list_result:
                                    list_result.append(res)
                    details=list_result
                if not 'key_skills' in p:
                    #for search in p['keywords'][0].split(','):Q(jsskills__skill__icontains=search),                    
                    if minexp and maxexp:
                        for res in User.objects.filter(query_function,query_jobtype,query_workpermit,query_workexp,query_loc,query_telecomute,query_visibility):
                            if not res in list_result:
                                list_result.append(res)
                    elif minexp:
                        for res in User.objects.filter(query_function,query_jobtype,query_workpermit,Q(jspersonal__work_expyears__gte=minexp),query_loc,query_telecomute,query_visibility):
                            if not res in list_result:
                                list_result.append(res)
                    elif maxexp:
                        for res in User.objects.filter(query_function,query_jobtype,query_workpermit,Q(jspersonal__work_expyears__lte=maxexp),query_loc,query_telecomute,query_visibility):
                            if not res in list_result:
                                list_result.append(res)
                    else:
                        for res in User.objects.filter(query_function,query_jobtype,query_workpermit,query_telecomute,query_loc,query_visibility):
                            if not res in list_result:
                                list_result.append(res)
                    details=list_result
                if ranges:
                    if city:
                        latlng=gn.geocode(city, exactly_one=False)[0]
                        result=[]
                        for i in details:
                            lats=i.jspersonal.lat
                            rlat=radians(float(lats))
                            slat=radians(latlng[1][0])
                            long_diff = radians(float(i.jspersonal.lng) - latlng[1][1])
                            distance = (sin(rlat) * sin(slat) + cos(rlat) * cos(slat) * cos(long_diff))
                            distance=degrees(acos(distance)) * 69.09
                            if distance <= int(ranges):
                                result.append(i)
                        details=result
            current_domain = Site.objects.get_current().domain
            contxt=Context({'d':details,'fname':fname,'searchname':name,'now':now,'current_domain':current_domain})
            message_template = loader.get_template('registration/new_matching_profile_alert.html')
            message=message_template.render(contxt)
            msg=EmailMultiAlternatives('iTechTalents.com Job Alerts',message,'itechtalentalerts@itechtalents.com',[tomail])
            msg.attach_alternative(message, "text/html")
            msg.send()
@periodic_task(run_every=timedelta(seconds=20))
def deactivate_employerpack():
    now=datetime.datetime.now()
    for subscribe in emppack_activation.objects.all():
        if subscribe.is_active:
            for pack in emp_subscribed_packs.objects.filter(id=subscribe.subscribed_pack_id):
                if pack.pack_expire<now:
                    deactivate=emppack_activation.objects.get(subscribed_pack_id=pack.id)
                    deactivate.is_active=False
                    deactivate.totaljobpost=0
                    deactivate.totalresume=0
                    deactivate.save()
@periodic_task(run_every=timedelta(seconds=20))
def deactivate_activatejob():
    for job in jobs.objects.all():
        if job.is_active:
            if job.todate < datetime.datetime.now():
                job.is_active=False
                job.save()


