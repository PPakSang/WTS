from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404,render
from django import http
from django.http import HttpResponse
from django.views import generic
from django.views.generic import *
from .models import *
from .forms import TestForm, Signup
import os

# Create your views here.


def test(request,name):
    
    a=get_object_or_404(Test,name=name)

    return render(request,'test.html',{'a':a})


def post(request):

    if request.method == "POST":
        form = TestForm(request.POST) # request.POST -> post 로 들어온 kwargs 정보
        
        if form.is_valid():
            
            test_object=form.save(commit=False)
            #내부에서 저장할 데이터가 있을수도 있으므로
            #DB저장 지연
            test_object.check=10
            test_object.save()
            return redirect('detail',2)

    else :
        form = TestForm()  #form 오브젝트 생성
        return render(request,'test_form.html',{'form':form})


def signup(request):

    if request.method == 'POST':
        form = Signup(request.POST)
        
        if form.is_valid(): 
            User.objects.create_user(**form.cleaned_data)
            return HttpResponse('회원가입이 완료되었습니다')
        
    else :
        form =  Signup()
        return render(request,'signup.html',{'form':form})
