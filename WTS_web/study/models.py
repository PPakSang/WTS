from time import time
from django.contrib.auth.backends import ModelBackend
from django.core import validators
from django.db import models
from django.db.models.base import Model
from django.core.validators import *
from django.shortcuts import redirect, render
import datetime
from django.utils import timezone
# Create your models here.


class Student(models.Model): 
    name = models.CharField(max_length=10,validators=[MinLengthValidator(2)])
   
    number = models.CharField(max_length=11, validators=[MinLengthValidator(10)])
    
    level_status = (('1','왕초급'),('2','초급'),('3','중급'))
    level = models.CharField(max_length=1,choices=level_status,blank=True)
    time_status = (('1','평일'),('2','주말1시'),('3','주말4시'))
    time = models.CharField(max_length=1,choices=time_status,blank=True)
    
    base_date = models.DateField(default=datetime.date.today(),verbose_name='기준 주차')
    
    day1 = models.DateField(default=datetime.date.today(),verbose_name='첫번째 참여일')
    day2 = models.DateField(default=datetime.date.today(),verbose_name='두번째 참여일')
    day3 = models.DateField(default=datetime.date.today(),verbose_name='세번째 참여일')
    day4 = models.DateField(default=datetime.date.today(),verbose_name='네번째 참여일')
    plus_day = models.DateField(default=datetime.date.today(),verbose_name='보너스 참여일')
    
    changed_day = models.DateField(default=datetime.date.today(),verbose_name='등록하기 한날')
    
    user_id = models.IntegerField(default=0)



    def __str__(self) -> str:
        return self.name + f'({self.number[3:]})'

    def get_absolute_url(self):
        return redirect('detail',pk = self.id)



class Faq(models.Model):
    name = models.CharField(max_length=10)
    answer_to = models.CharField(max_length=100)
    text = models.TextField()


    def __str__(self) -> str:
        return self.name + f'({self.answer_to})'
        