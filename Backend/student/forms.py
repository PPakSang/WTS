from django import forms
from django.db import models
from django.db.models import fields
from .models import Test

class TestForm(forms.ModelForm):

    class Meta:
        model=Test
        fields = ('name','age')
