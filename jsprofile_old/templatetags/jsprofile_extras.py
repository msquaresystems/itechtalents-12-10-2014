#from django import template
from django.template import Template, Context,Library
register = Library()

@register.simple_tag
def create_select(name='country'):
	from jsprofile.comboitems import *
	#if name=='country':
	#	select_list = country_list
	#elif name=='degree':
	#	from jsprofile.c

	#print 'sssss'
	select_list=eval('{0}_list'.format(name))
	str_html='''
		<select name="{{fname}}" required>
		    <option value="">Select</option>
		    {% for item in items %}
		       <option value="{{item}}">{{item}}</option>
		    {% endfor %}
		</select>
	'''
	t = Template(str_html)
	x=t.render(Context({'items': select_list,'fname':name}))	
	return x
@register.simple_tag
def SelectEmploymentType(sel):
	str_q='<select id="emptype"  name="emptype" size="4" style="width:250px;"><option value="">Select</option>'
	for i in ('Full time','Contract - Corp to Corp','Contract - Independent','Contract - W2','Contract to Hire - Corp to Corp','Contract to Hire - Independent','Contract to Hire - W2','Part time'):
		if i==sel:str_q+='<option selected="selected" value="%s">%s</option>' %(i,i)
		else:str_q+='<option value="%s">%s</option>' %(i,i)
	str_q+='</select>'
	return str_q
# @register.simple_tag
# def SelectCountry(sel):
# 	str_q='<select name="country" id="country" onChange="setStates();" style="width:235px;" ><option value="">SelectCountry</option>'
# 	for i in ("Australia","Bangladesh","Canada","India","Malaysia","Mexico","Saudi Arabia","United Arab Emirates","United Kingdom","United States"):
# 		if i==sel:str_q+='<option selected="selected" value="%s">%s</option>' %(i,i)
# 		else:str_q+='<option value="%s">%s</option>' %(i,i)
# 	str_q+='</select>'
# 	return str_q
	