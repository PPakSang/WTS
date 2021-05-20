from collections import namedtuple
from django.contrib.auth.models import AnonymousUser
from django.urls import path
from .views import *

urlpatterns = [
    # path('',main_view,name='main'),
    path('', index, name='index'),
    path('signup/',signup,name='signup'),
    path('login/',login,name='login'),
    path('logout/',logout,name='logout'),
    path('detail/',my_study,name='detail'),
    path('enroll/',Enroll.as_view(),name='enroll'),
    path('change/',change_day,name='change')
    

]