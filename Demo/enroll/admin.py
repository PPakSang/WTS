from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *
# Register your models here.



@admin.register(Student)
class Admin_model(admin.ModelAdmin):
    list_display = ['name','is_new','content_size']
    
    def content_size(self,obj):
        return mark_safe(f"<u>{obj.phone_number}</u>") #보안 때문에 mark_safe 로 html 집어넣기 
    content_size.short_description ='Test'