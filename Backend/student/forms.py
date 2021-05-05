from django import forms
import django
from django.db import models
from django.db.models import fields
from django.forms import widgets
from .models import *





class TestForm(forms.ModelForm):
    
    class Meta:
        model = Test
        fields = ('name','enroll')
    
    def save(self,**kwargs):
        test = super().save(commit=False)
        test.user_id = kwargs.get('id',None)
        test.save()

BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]       

class TestForm2(forms.Form):
    
    favorite_colors = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=FAVORITE_COLORS_CHOICES,
    )



from django.contrib.auth.models import User

class Signup(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class PasswordConfirm(forms.Form):
    
    password2 = forms.CharField(max_length=128)



class Signin(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['username','password']