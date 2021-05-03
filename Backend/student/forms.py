from django import forms
from django.db import models
from django.db.models import fields
from .models import Test


class TestForm(forms.ModelForm):
    
    class Meta:
        model = Test
        fields = ('name','age')



from django.contrib.auth.models import User

class Signup(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']



class Signin(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['username','password']