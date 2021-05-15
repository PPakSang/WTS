from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import fields
from django.views import generic
from django.contrib import auth
import django
from .models import *
from .forms import *


# Create your views here.


def signup(request): #회원가입
    if request.method == 'POST':
        form = Signup_form(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username = username,password = password)
            user.save()
            user = authenticate(username = username , password = password)
            auth.login(request,user)
            
            
            return redirect('main')
        else:
            return render(request,'student/signup.html',{'form' : form})
    else:
        form = Signup_form()
        return render(request,'student/signup.html',{'form' : form})

def login(request): #로그인
    if request.method == 'POST':
        form = Login_form(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username = username , password = password)

            if user is not None :
                auth.login(request,user)
                return redirect('main')
           
            return render(request,'student/login.html',{'form':form})    
       
    else:
        form = Login_form()
        return render(request,'student/login.html',{'form':form})  
    

def logout(request): #로그아웃
    if request.method == 'POST': #logout check

        auth.logout(request)
        return redirect('main')
    else:
        return render(request,'student/checklogout.html')


@login_required(login_url='/login/')
def my_study(request): #조회하기

    try:
        student = Student.objects.get(user_id = request.user.id)
    except :
        return render(request,'student/error.html',{'is_study':False})

    return render(request,'student/detail.html',{'student':student})
    
    

class Enroll(LoginRequiredMixin,generic.CreateView): #등록하기
    model = Student
    fields=['name','number','level','study','first_day']
    template_name = 'student/enroll.html'
    login_url = '/login/'
    
    def get(self, request, *args, **kwargs) :
        try:
            Student.objects.get(user_id = self.request.user.id)
            return render(request,'student/error.html',{'is_enroll':True})
        except:
            return super().get(request,*args,**kwargs)

    def form_valid(self, form):
        
        form = form.save(commit = False)
        form.user_id = self.request.user.id
        form.save()

        return redirect('main')
        


def main_view(request): #메인 화면
    
    if request.user.is_authenticated:

        student = Student.objects.filter(user_id = request.user.id)
    else:
        return render(request,'main.html')

    if bool(student):
        
        return render(request,'main.html',{'is_student':True})
    else:
        return render(request,'main.html',{'is_student':False})


