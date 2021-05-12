from django import forms
from .models import Student



class TestForm(forms.Form):
    name = forms.CharField(widget=forms.select)