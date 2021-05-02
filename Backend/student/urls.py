from django.urls import path,include
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns=[
    path('',main),
    path('login/',auth_views.LoginView.as_view(),name='login'),

]
