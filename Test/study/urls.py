from collections import namedtuple
from django.contrib.auth.models import AnonymousUser
from django.urls import path
from django.utils.timezone import activate
from .views import *

urlpatterns = [
    # path('',main_view,name='main'),
    # path('signup/',signup,name='signup'),
    # path('login/',login,name='login'),
    path('logout/',logout,name='logout'),
    #path('detail/',my_study,name='detail'),
    # path('enroll/',Enroll.as_view(),name='enroll'),
    # path('change/',change_day,name='change'),
    path('activate/<uid64>/<token>',activate,name='activate'),


    # 아래는 템플릿 테스트
    path('', index, name='index'),
    path('enroll/', enroll, name='enroll'),
    path('inquire/', inquire, name='inquire'),
    path('change/', change, name='change'),
    path('login/', login_hw, name='login'),
    path('signup/', signup_hw, name='signup'),
    path('faq/', faq, name='faq'),
    path('findid/',find_id,name='find_id'),
    path('findpw/',find_pw,name='find_pw'),
    path('resetpw/<uid64>/<token>',reset_pw,name='reset_pw'),
    path('checkemail/', checkemail, name='check_email'),
]