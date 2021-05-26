from django.contrib import admin
from django.contrib.admin.decorators import action
from .models import *
# Register your models here.


@admin.register(Student)
class Student_Admin(admin.ModelAdmin):
    list_display = [Student.__str__,'changed_day']
    list_filter = ['changed_day']
    search_fields = ['name']
    
    

 