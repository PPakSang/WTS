from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Student)
class Student_Admin(admin.ModelAdmin):
    
    pass
    
@admin.register(Study)
class Student_Admin(admin.ModelAdmin):
    
    pass