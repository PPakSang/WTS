from django.core import validators
from django.db import models
from django.db.models.base import Model
from django.core.validators import *
from django.shortcuts import redirect, render
from datetime import datetime
# Create your models here.

class Study(models.Model):
    name = models.CharField(max_length=10,unique=True)

    def __str__(self) -> str:
        return self.name
    
    

class Student(models.Model):
    name = models.CharField(max_length=4,validators=[MinLengthValidator(2)])
    number = models.CharField(max_length=11, validators=[MinLengthValidator(10)])
    level_status = (('왕초급','왕초급'),('초급','초급'),('중급','중급'))
    level = models.CharField(max_length=3,choices=level_status,blank=True)
    study = models.ForeignKey(Study, on_delete=models.SET_NULL,null=True)
    first_day = models.DateTimeField(default=datetime.today())
    user_id = models.IntegerField(default=0)
    


    def __str__(self) -> str:
        return self.name + f'({self.number[3:]})'

    def get_absolute_url(self):
        return redirect('detail',pk = self.id)

