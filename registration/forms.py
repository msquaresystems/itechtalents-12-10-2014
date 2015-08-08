"""
Form and validation code for user registration.

"""

from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from registration.models import RecruiterFolder, EmployerReg_Form, PREFERRED_COMPANYTYPE
import re


# I put this on all required fields, because it's easier to pick up
# on them with CSS or JavaScript if they have a class of "required"
# in the HTML. Your mileage may vary.
attrs_dict = { 'class': 'required' }
IMP_CHOICES = (
    ('1', "What is your first grade class teacher name?"),
    ('2', "What is your best friend's last name?"),
    ('3', "What street name you lived when you born?"),
    ('4', "What is your grand father's last name?"),
    ('5', "Set your own security question")
)
class RegistrationForm(forms.Form):
    """
    Form for registering a new user account.
    
    Validates that the password is entered twice and matches,
    and that the username is not already taken.
    
    """
    first_name= forms.CharField(max_length=30,widget=forms.TextInput(attrs={'placeholder': 'Firstname','class': 'required'}),label=u'Firstname')
    last_name = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'placeholder': 'Lastname','class': 'required'}),label=u'Lastname')
    username = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'placeholder': 'Username','class': 'required'}),label=u'Username')
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email','class': 'required'}),label=u'Email address')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password','class': 'required'}),label=u'Password')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password','class': 'required'}),label=u'Password (again, to catch typos)')
    selectquestion=forms.ChoiceField(choices=IMP_CHOICES)
    question = forms.CharField(max_length=270,widget=forms.HiddenInput)
    answer = forms.CharField(max_length=60)
    usertype = forms.CharField(widget=forms.HiddenInput)
    tos = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'requred1'}),label=u'I have read and agree to the Terms of Service')

    def clean_username(self):
        """
        Validates that the username is not already in use.
        
        """
        if self.cleaned_data.get('username', None):
            try:
                user = User.objects.get(username__exact=self.cleaned_data['username'])
            except User.DoesNotExist:
                return self.cleaned_data['username']
            raise forms.ValidationError(u'Username is unavailable.')


    def clean_email(self):
        """
        Validates that the email is not already in use.
        
        """
        if self.cleaned_data.get('email', None):
            try:
                user = User.objects.get(email__exact=self.cleaned_data['email'])
            except User.DoesNotExist:
                return self.cleaned_data['email']
            raise forms.ValidationError(u'Email already exists.')
    
    def clean_password2(self):
        """
        Validates that the two password inputs match.
        
        """
        if self.cleaned_data.get('password1', None) and self.cleaned_data.get('password2', None) and \
           self.cleaned_data['password1'] == self.cleaned_data['password2']:
            return self.cleaned_data['password2']
        raise forms.ValidationError(u'Password Mismatched')
    
    def clean_tos(self):
        """
        Validates that the user accepted the Terms of Service.
        
        """
        if self.cleaned_data.get('tos', False):
            return self.cleaned_data['tos']
        raise forms.ValidationError(u'You must agree to the terms to register')



class EmpRegistrationForm(forms.Form):
    
    username = forms.CharField(max_length=30,
                               widget=forms.TextInput(attrs=dict(attrs_dict,placeholder="Username")),
                               label=u'Username')
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(attrs_dict,placeholder="abc@corporatemailid.com",
                            maxlength=200)),
                            label=u'Email address')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=dict(attrs_dict,placeholder="Password")),
                                label=u'Password')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=dict(attrs_dict,placeholder="Re-type password")),
                                label=u'Password (again, to catch typos)')
    usertype = forms.CharField(widget=forms.HiddenInput)

    companyname = forms.CharField(widget=forms.TextInput(attrs=dict(attrs_dict,placeholder="Company Name")))

    companytype = forms.ChoiceField(choices=PREFERRED_COMPANYTYPE, widget=forms.RadioSelect())
    
    companyurl=forms.URLField(widget=forms.TextInput(attrs=dict(attrs_dict,placeholder="Company URL")))

    contactno = forms.CharField(widget=forms.TextInput(attrs=dict(attrs_dict,placeholder="Mobile No/Phone No",maxlength="10")))

    contactperson = forms.CharField(widget=forms.TextInput(attrs=dict(attrs_dict,placeholder="Contact Person")))

    tos = forms.BooleanField(widget=forms.CheckboxInput(attrs=attrs_dict),
                             label=u'I have read and agree to the Terms of Service')

    #tos = forms.BooleanField(widget=forms.CheckboxInput(attrs=attrs_dict),label=u'Password (again, to catch typos)')

    def clean_username(self):
        """
        Validates that the username is not already in use.
        
        """
        if self.cleaned_data.get('username', None):
            try:
                user = User.objects.get(username__exact=self.cleaned_data['username'])
            except User.DoesNotExist:
                return self.cleaned_data['username']
            raise forms.ValidationError(u'Username is unavailable.')

    
    def clean_email(self):
        """
        Validates that the email is not already in use.

        """
        data = self.cleaned_data['email']
        domain = data.split('@')[1].split('.')[0]
        domain_list = ["gmail", "yahoo", "hotmail","sify","outlook",""]
        if domain in domain_list:
          raise forms.ValidationError("Enter Corporate Email")
        if self.cleaned_data.get('email', None):
            try:
                user = User.objects.get(email__exact=self.cleaned_data['email'])
                
            except User.DoesNotExist:
                return self.cleaned_data['email']
            raise forms.ValidationError(u'Email already exists.')

    def clean_companyname(self):
        """
        Validates that the email is not already in use.
        
        """
        
        if self.cleaned_data.get('companyname', None):
            try:
                user = EmployerReg_Form.objects.get(companyname__exact=self.cleaned_data['companyname'])
                
            except EmployerReg_Form.DoesNotExist:
                return self.cleaned_data['companyname']
            raise forms.ValidationError(u'Companyname already exists.')

    
    
    def clean_companyurl(self):
        """
        Validates that the email is not already in use.
        
        """
        
        try:
            user = EmployerReg_Form.objects.get(companyurl__exact=self.cleaned_data['companyurl'])
            
        except EmployerReg_Form.DoesNotExist:
            return self.cleaned_data['companyurl']
        raise forms.ValidationError(u'companyurl already exists.')
    
    def clean_password2(self):
        """
        Validates that the two password inputs match.
        
        """
        if self.cleaned_data.get('password1', None) and self.cleaned_data.get('password2', None) and \
           self.cleaned_data['password1'] == self.cleaned_data['password2']:
            return self.cleaned_data['password2']
        raise forms.ValidationError(u'Password Mismatched')
    
    def clean_tos(self):
        """
        Validates that the user accepted the Terms of Service.
        
        """
        if self.cleaned_data.get('tos', False):
            return self.cleaned_data['tos']
        raise forms.ValidationError(u'You must agree to the terms to register')


class EmployerLoginForm(forms.Form):
    email=forms.CharField()
    password=forms.CharField()

    def clean_email(self):

       if self.cleaned_data.get('username', None) and self.cleaned_data.get('password', None):
            try:
                emp = EmployerReg_Form.objects.get(username=self.cleaned_data['email'],password=self.cleaned_data['password']) 
            except EmployerReg_Form.DoesNotExist:
                return self.cleaned_data['password']

            raise forms.ValidationError(u'The username "%s" is unavailable. Try another.' % self.cleaned_data['username']) 

class socialpassresetform(forms.Form):
    username = forms.CharField(max_length=30,widget=forms.TextInput(attrs=attrs_dict))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=attrs_dict))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=attrs_dict))
    usertype = forms.CharField(widget=forms.HiddenInput)
    userid = forms.CharField(widget=forms.HiddenInput)

    def clean_username(self):
        """
        Validates that the username is not already in use.
        
        """
        if self.cleaned_data.get('username', None):
            try:
                user = User.objects.get(username__exact=self.cleaned_data['username'])
            except User.DoesNotExist:
                return self.cleaned_data['username']
            raise forms.ValidationError(u'Username is unavailable.')

    def clean_password2(self):
        """
        Validates that the two password inputs match.
        
        """
        if self.cleaned_data.get('password1', None) and self.cleaned_data.get('password2', None) and \
           self.cleaned_data['password1'] == self.cleaned_data['password2']:
            return self.cleaned_data['password2']
        raise forms.ValidationError(u'Password Mismatched')



class PasswordReset(forms.Form):
    oldpassword = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'span4','placeholder':'Old password'}),required=True)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'span4','placeholder':'New password'}),required=True)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'span4','placeholder':'Confirm password'}),required=True)
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(PasswordReset, self).__init__(*args, **kwargs)
    
    def clean_oldpassword(self):
        if self.user.check_password(self.cleaned_data['oldpassword']):
            return self.cleaned_data['oldpassword']
        raise forms.ValidationError('Wrong old password')
    def clean_password1(self):
        if len(self.cleaned_data['password1']) < 6:raise forms.ValidationError("Must be 1 Uppercase, Lowercase and Numeric with 6 digit length")
        if not re.search('[A-Z]', self.cleaned_data['password1']):raise forms.ValidationError("Must be 1 Uppercase, Lowercase and Numeric with 6 digit length")
        if not re.search('[a-z]', self.cleaned_data['password1']):raise forms.ValidationError("Must be 1 Uppercase, Lowercase and Numeric with 6 digit length")
        if not re.search('[0-9]', self.cleaned_data['password1']):raise forms.ValidationError("Must be 1 Uppercase, Lowercase and Numeric with min 6 digit length")
        if self.cleaned_data.get('password1') == self.cleaned_data.get('oldpassword'):raise forms.ValidationError(u'Old and New password should not be same')
        return self.cleaned_data['password1']
    def clean_password2(self):
        if not self.cleaned_data.get('password1') == self.cleaned_data.get('password2'):raise forms.ValidationError(u'Password Mismatched')        
        return self.cleaned_data['password2']

class MailForm(forms.Form):
        subject = forms.CharField(max_length=255)
        message = forms.CharField(widget=forms.Textarea)
        attachment = forms.FileField()


class RecruiterFolders(forms.Form):
    foldername = forms.CharField(max_length=30,widget=forms.TextInput(attrs=dict(attrs_dict,placeholder="Folder name",required=True)),
                               label=u'Folder Name')

    def clean_foldername(self):
        """
        Validates that the username is not already in use.
        
        """
        if self.cleaned_data.get('foldername', None):
            try:
                user = RecruiterFolder.objects.get(foldername__exact=self.cleaned_data['foldername'])
            except RecruiterFolder.DoesNotExist:
                return self.cleaned_data['foldername']
            raise forms.ValidationError(u'Folder name already exists')
