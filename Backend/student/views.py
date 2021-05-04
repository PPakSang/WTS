from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404,render
from django import http
from django.http import HttpResponse
from django.views import generic
from django.views.generic import *
from .models import *
from .forms import *
import os

# Create your views here.


def mainview(request):
    if Test.objects.filter(user_id=request.user.id):
         ok=True
    else :
         ok=False
    return render(request,'main.html',{'ok':ok})

def test_form(request):
    
    if request.method =='POST':
        form = TestForm(request.POST)
        if form.is_valid() :
            form.save(id = request.user.id)
           
            return redirect('main')
            
    else:
        form = TestForm()
        
        
        return render(request,'test_form.html',{'form':form})


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
        form1 = Signup()
        form2 = PasswordConfirm()
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            User.objects.create_user(username=username,email=email,password=password)
            return HttpResponse('회원가입이 완료되었습니다')
        else :
            return HttpResponse('회원가입이 실패했습니다') 
    else :
        form1 =  Signup()
        form2 = PasswordConfirm()
        return render(request,'signup.html',{'form1':form1,'form2' : form2})


def signin(request):
    if request.method == 'POST':
        form = Signin(request.POST)
        username=request.POST['username']
        password=request.POST['password']
        new_user=authenticate(username=username,password=password)
        if new_user is not None:
            login(request,new_user)
            return redirect('main')
        else :
            ok=True
            return render(request,'signin.html',{'form' : form, 'ok':ok})
    else :
        form = Signin()
        return render(request,'signin.html',{'form' : form})


