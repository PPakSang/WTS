from os import name
from django.urls import path,include
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns=[
    path('',mainview,name='main'),
    path('student/<int:name>',test,name='detail'),
    path('student/form',post,name='post'),
    path('student/signup/',signup,name='signup'),
    path('student/signin/',signin,name='signin'),
    

]
