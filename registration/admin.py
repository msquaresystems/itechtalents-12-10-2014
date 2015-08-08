from django.contrib import admin
from registration.models import *



class newsletteradmin(admin.ModelAdmin):
	model = newsletter
	readonly_fields = ['link']

	#list_display=('topics','content','sentdate','usertype','sentnewsletter')
	
	def link(self,obj):
		return '<input type="submit" >'
	link.allow_tags = True

admin.site.register(jobs)
admin.site.register(EmployerReg_Form)
admin.site.register(BlogTopics)
admin.site.register(Blog)
admin.site.register(BComments)
admin.site.register(Interview)
admin.site.register(Reschedule)

admin.site.register(InterviewRounds)
admin.site.register(JSDetails)
admin.site.register(JSResume)
admin.site.register(JSProjectDetails)
admin.site.register(JSEmployerDetails)

# ------------------1st JUNE ------------

admin.site.register(emppacks)
admin.site.register(emp_subscribed_packs)
admin.site.register(emppack_activation)
admin.site.register(EmpSubscription)
admin.site.register(jspacks)
admin.site.register(jssubscribed_packs)
admin.site.register(newsletter,newsletteradmin)

from video_resume.models import VideoResume
admin.site.register(VideoResume)