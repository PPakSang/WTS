from django.urls import path
from django.urls.conf import include
from .views import *
from django.contrib.auth import views as auth_view


urlpatterns = [
    
    path('accounts/', include('allauth.urls')),
    path('enroll/',init_enroll.as_view(),name='enroll'),
    path('list/',enroll_list.as_view(),name='list'),
    path('isenroll/',is_enroll,name='isenrolls')
    
    
]