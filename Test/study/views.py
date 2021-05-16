from datetime import timedelta
from django.db.models.query_utils import select_related_descend
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
        days =[]
        for i in range(4):
            days.append(student.first_day +timedelta(weeks=i))
        for i in days :
            if (i - datetime.date.today()).days>=0:
                next_day = i
                break
            

    except :
        return render(request,'student/error.html',{'is_study':False})

    return render(request,'student/detail.html',{'student':student,'days':days,'next_day':next_day})
    
    

class Enroll(LoginRequiredMixin,generic.CreateView): #등록하기
    model = Student
    fields=['name','number','level','first_day']
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
        form.changed_day = form.first_day
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


@login_required(login_url='/login/')
def change_day(request):
    try:
        student = Student.objects.get(user_id = request.user.id)
        if request.method == 'POST':
            form = Select_day_form(request.POST)
            if form.is_valid():
                student.changed_day = form.cleaned_data['changed_day']
                student.save()
                return redirect('detail')
            else:
                return render(request,'student/change_day.html',{'form':form})
        else:
            form = Select_day_form()
            return render(request,'student/change_day.html',{'form':form})
    except :
        return render(request,'student/error.html',{'is_study':False})

