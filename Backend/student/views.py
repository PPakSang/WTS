from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views import generic
from django.views.generic import *
import os

# Create your views here.


class KakaoLoginTest(View):
    def get(self,request):
        REST_API_KEY = '977f61e5094b61a35368e56ded503b70'
        REDIRECT_URI = 'http://localhost:8000'

        API_HOST = f'https://kauth.kakao.com/oauth/authorize?client_id={REST_API_KEY}&redirect_uri={REDIRECT_URI}&response_type=code'

        return redirect(API_HOST)


def main(request):
    return HttpResponse('Main')
