from django.forms import ModelForm,ValidationError
from quorum.models import Question
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field,Layout, ButtonHolder, Submit,HTML
from quorum.models import Question,Answer,Topic

class AnswerForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()

        self.helper.form_tag = False
        self.helper.layout = Layout(
            Field('answer',css_class="field span8"),
            ButtonHolder(
                Submit('submit', 'Submit', css_class='btn-primary pull-right')
            )
        )
        super(AnswerForm, self).__init__(*args, **kwargs)    

    class Meta:
        model = Answer
        fields=("answer",)#exclude = ["post"]

class QuestionForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'questionForm'
        self.helper.layout = Layout(
            Field('topic',css_class="input-xxlarge"),
            HTML("""
            If you want to create a New Topic, please click <strong>Add Topic</strong>"""),
            Field('question',css_class="input-xxlarge"),         
        )
        self.helper.add_input(Submit('submit', 'Post Your Question',css_class="btn-inverse"))
        super(QuestionForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Question
    	fields=("topic","question")