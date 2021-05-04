from django import forms
from django.db import models
from django.db.models import fields
from .models import Test


class TestForm(forms.ModelForm):
    
    class Meta:
        model = Test
        fields = ('name','enroll')
    
    def save(self,**kwargs):
        test = super().save(commit=False)
        test.user_id = kwargs.get('id',None)
        test.save()

        





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