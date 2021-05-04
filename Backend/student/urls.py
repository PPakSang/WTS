from os import name
import django
from django.urls import path,include
from .views import *
from django.contrib.auth import views as auth_views



urlpatterns=[
    path('',mainview,name='main'),
    path('student/',test_form,name='add'), #등록하기 이미 등록했을경우 조회하기로 바뀌어야함
    path('student/form',post,name='post'), #테스트 폼
    path('student/signup/',signup,name='signup'), #회원가입
    path('student/signin/',signin,name='signin'), #로그인
    path('student/',include('django.contrib.auth.urls')) #로그아웃만 쓰려고 우선은

]
