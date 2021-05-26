from collections import namedtuple
from django.contrib.auth.models import AnonymousUser
from django.urls import path
from django.utils.timezone import activate
from .views import *

urlpatterns = [
    # path('',main_view,name='main'),
    path('signup/',signup,name='signup'),
    path('login/',login,name='login'),
    path('logout/',logout,name='logout'),
    path('detail/',my_study,name='detail'),
<<<<<<< HEAD
    path('enroll/',Enroll.as_view(),name='enroll'),
    path('change/<int:i>',change_day,name='change'),
    path('wtslist/',only_admin,name='adminpage'),
    path('activate/<slug:uid64>/<slug:token>',activate,name='activate'),

    
=======
    # path('enroll/',Enroll.as_view(),name='enroll'),
    path('change/',change_day,name='change'),
>>>>>>> template_version


    # 아래는 템플릿 테스트
    path('', index, name='index'),
    path('enroll/', enroll, name='enroll'),
]