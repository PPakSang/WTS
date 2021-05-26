from time import time
from django.db import models
from django.db.models.base import Model
from django.shortcuts import redirect
from datetime import date
from django.utils import timezone

# Create your models here.



class Student(models.Model):
    name = models.CharField(max_length=10,verbose_name='성명')

    status_new = (('신규','신규'),('재등록','재등록'))
    is_new = models.CharField(max_length=5,choices=status_new,default='o',verbose_name='신규여부')

    status_day = (('월요일','월요일'),('화요일','화요일'),('수요일','수요일'),('목요일','목요일'),('금요일','금요일'),('토요일','토요일'),('일요일','일요일'))
    fixed_day = models.CharField(max_length=5,choices=status_day,default='1',verbose_name='고정요일')

    first_day =  models.DateField(null=True)

    phone_number = models.CharField(max_length=13,verbose_name='전화번호')
    
    user_id = models.CharField(default=0,max_length=10)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return redirect('detail',self.id)

