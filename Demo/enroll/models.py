from time import time
from django.db import models
from django.db.models.base import Model
from django.shortcuts import redirect
from datetime import date
from django.utils import timezone

# Create your models here.



class Student(models.Model):
    name = models.CharField(max_length=10)
    status_new = (('o','신규'),('x','재등록'))
    is_new = models.CharField(max_length=1,choices=status_new,default='o')
    status_day = (('1','월요일'),('2','화요일'),('3','수요일'),('4','목요일'),('5','금요일'),('6','토요일'),('7','일요일'))
    fixed_day = models.CharField(max_length=1,choices=status_day,default='1')
    first_day =  models.DateField(null=True)
    phone_number = models.CharField(max_length=13)
    user_id = models.CharField(default=0,max_length=10)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return redirect('main',self.id)

