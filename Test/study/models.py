from time import time
from django.core import validators
from django.db import models
from django.db.models.base import Model
from django.core.validators import *
from django.shortcuts import redirect, render
import datetime
from django.utils import timezone
# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=4,validators=[MinLengthValidator(2)])
   
    number = models.CharField(max_length=11, validators=[MinLengthValidator(10)])
    
    level_status = (('왕초급','왕초급'),('초급','초급'),('중급','중급'))
    level = models.CharField(max_length=3,choices=level_status,blank=True)
    
    first_day = models.DateField(default=timezone.now())
    changed_day = models.DateField(default=timezone.now(),verbose_name='첫 참여날짜')
    
    user_id = models.IntegerField(default=0, unique=True)

    

    def __str__(self) -> str:
        return self.name + f'({self.number[3:]})'

    def get_absolute_url(self):
        return redirect('detail',pk = self.id)

