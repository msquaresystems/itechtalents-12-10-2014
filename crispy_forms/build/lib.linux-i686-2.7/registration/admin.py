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

# ------------------1st JUNE ------------

admin.site.register(emppacks)
admin.site.register(emp_subscribed_packs)
admin.site.register(emppack_activation)

admin.site.register(jspacks)
admin.site.register(jssubscribed_packs)
admin.site.register(newsletter,newsletteradmin)

