from collections import namedtuple
from django.contrib.auth.models import AnonymousUser
from django.urls import path
from .views import *

urlpatterns = [
    path('',main_view,name='main'),
    path('signup/',signup,name='signup'),
    path('login',login)

]