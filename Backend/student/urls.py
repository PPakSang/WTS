from django.urls import path,include
from .views import KakaoLoginTest


urlpatterns=[
    path('',KakaoLoginTest.as_view())

]
