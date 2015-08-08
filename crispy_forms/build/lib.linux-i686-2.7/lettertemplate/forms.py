from django import forms
from crispy_forms.helper import FormHelper
from lettertemplate.models import LetterTemplate
from crispy_forms.layout import Layout,Fieldset,Field

class LetterTemplateForm(forms.ModelForm):    
    def __init__(self, *args, **kwargs):
    	super(LetterTemplateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
                Fieldset(
        			'Letter Template',
        			'title',        			
        			'replayto',        			       			
        		),
                Field('subject', css_class="input-xxlarge"),
                Field('body',css_class="input-xxlarge"),
        	)
        self.helper.form_tag = False
        
    class Meta:
        model=LetterTemplate
        exclude=['employer',]
