from .models import *
from django import forms
from django.core import validators


class Enroll_form(forms.ModelForm):
    
    class Meta:
        model = Student
        fields = ['level','number','day1','time']
    
    
    
class Signup_form(forms.Form):
    username = forms.CharField(max_length=10)
    password = forms.CharField(max_length=10)
    password2 = forms.CharField(max_length=10)
    
class Login_form(forms.Form):
    username = forms.CharField(max_length=10)
    password = forms.CharField(max_length=10)
    
class Select_day_form(forms.Form):
    changed_day = forms.DateField()