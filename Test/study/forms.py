from django import forms
from django.core import validators


class check_enroll(forms.Form):
    name = forms.CharField(max_length=10)
    number = forms.CharField(max_length=11,validators=[validators.MinLengthValidator(10)])
    
    
class Signup_form(forms.Form):
    username = forms.CharField(max_length=10)
    password = forms.CharField(max_length=10)
    
class Login_form(forms.Form):
    username = forms.CharField(max_length=10)
    password = forms.CharField(max_length=10)
    