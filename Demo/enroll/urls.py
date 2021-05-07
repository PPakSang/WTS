from django.urls import path
from django.urls.conf import include
from .views import *
from django.contrib.auth import views as auth_view


urlpatterns = [
    path('',main_view.as_view(),name='main'),
    path('student/enroll',init_enroll.as_view(),name='enroll'),
    path('accounts/', include('allauth.urls')),
    path('student/detail',detail_view,name='detail')
    
]