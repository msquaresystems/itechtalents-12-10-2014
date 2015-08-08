#from django import template
from django.template import Template, Context,Library
register = Library()

@register.simple_tag
def create_select(name='country'):
	from jsprofile.comboitems import *
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
@register.simple_tag
def sidebar(value):
	return value.replace(' ','_')
@register.simple_tag
def profileurl(n):
	val=''
	if n:val=n.replace('http://www.linkedin.com/','')
	return val
