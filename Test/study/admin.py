from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Student)
class Student_Admin(admin.ModelAdmin):
    list_display = [Student.__str__,'changed_day']
    list_filter = ['changed_day']

 