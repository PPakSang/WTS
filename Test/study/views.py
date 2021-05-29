from datetime import timedelta
from typing import ContextManager
from django import http
from django.http import response
from django.http.response import HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views import generic
from django.contrib import auth
from .models import *
from .forms import *


import bcrypt
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes,force_text
from django.contrib.auth.tokens import default_token_generator


# Create your views here.


def activate(request,uid64,token):
    uid = force_text(urlsafe_base64_decode(uid64))
    user = User.objects.get(pk = uid)
    
    if user is not None and default_token_generator.check_token(user,token):
        user.is_active = True
        user.save()
        auth.login(request,user)
        return redirect('index')
    return redirect('index')





    

def only_admin(request):
    if request.user.is_staff:
        if request.method == 'POST' :
            students = Student.objects.filter(name = request.POST['name'])
            return render(request,'student/admin.html',{'students':students})
        studetns =Student.objects.all()
        

        return render(request,'student/admin.html',{'students':studetns})
    else:
        return redirect('main')






# @login_required(login_url='/login/')
# def change_day(request):  #요일변경
#     try:
#         student = Student.objects.get(user_id = request.user.id)
#         if request.method == 'POST':
#             form = Select_day_form(request.POST)
#             if form.is_valid():
#                 # 최소 2일 전 신청
#                 if (form.cleaned_data['changed_day'] - datetime.date.today()).days <2 : 
#                     return HttpResponse('날짜를 다시 선택해주세요')
#                 student.changed_day = form.cleaned_data['changed_day']
#                 student.save()
#                 return redirect('detail')
#             else:
#                 return render(request,'student/change_day.html',{'form':form})
#         else:
#             form = Select_day_form()
#             return render(request,'student/change_day.html',{'form':form})
#     except :
#         return render(request,'student/error.html',{'is_study':False})




    

############################


def get_basedates(student): #첫 고정 참여일
    arr = []
    for i in range(0,4):
        arr.append(str(student.base_date + timedelta(weeks=i)))
    return arr

def get_days(student): #변경한 날짜
    arr = []
    arr.append(student.day1)
    arr.append(student.day2)
    arr.append(student.day3)
    arr.append(student.day4)
    return arr


# 여기서부터 템플릿 테스트 뷰
def index(request): # 메인 화면
    
    return render(request, 'index.html')

@login_required(login_url='/login/')
def enroll(request): # 등록하기 화면
    try:
        Student.objects.get(user_id = request.user.id)
        return HttpResponse('이미 등록했습니다')
    except:
        if request.method == 'POST':
            print(request.POST)
            form = Enroll_form(request.POST)
            if form.is_valid():
                form = form.save(commit = False)
                for i in range(2,5):
                    setattr(form,f'day{i}',form.day1 + timedelta(weeks=i-1))
                form.base_date = form.day1
                form.user_id = request.user.id
                form.name = request.user.first_name
                form.save()

                return redirect('index')
        return render(request, 'enroll.html')



# class Enroll(LoginRequiredMixin,generic.CreateView): #등록하기
#     model = Student
#     fields=['name','number','level','day1']
#     template_name = 'student/enroll.html'
#     login_url = '/login/'
    
#     def get(self, request, *args, **kwargs) :
#         try:
            
#             Student.objects.get(user_id = self.request.user.id)
#             return render(request,'student/error.html',{'is_enroll':True})
#         except:
#             return super().get(request,*args,**kwargs)

#     def form_valid(self, form):
        
#         form = form.save(commit = False)
#         for i in range(2,5):
#             setattr(form,f'day{i}',form.day1 + timedelta(weeks=i-1))
#         form.base_date = form.day1
#         form.user_id = self.request.user.id
#         form.save()

#         return redirect('main')

@login_required(login_url='/login/')
def inquire(request): # 조회하기 화면
    try:
        student = Student.objects.get(user_id = request.user.id)
        days =get_days(student)
        left_day = 4 
        for i in days :
            if (i - datetime.date.today()).days>=0:
                next_day = i
                break
            left_day -= 1
        if next_day == None:
            next_day = '추가등록이 필요합니다'
        base_dates = get_basedates(student)
        print(base_dates)

    except :
        redirect('enroll')

    return render(request,'inquire.html',
    {'student' : student,'days' : days,'next_day': next_day, 'left_day' : left_day, 'base_dates' : base_dates}
    )   


# @login_required(login_url='/login/')
# def my_study(request): #조회하기

#     try:
#         student = Student.objects.get(user_id = request.user.id)
#         days =get_days(student)
#         for i in days :
#             if (i - datetime.date.today()).days>=0:
#                 next_day = i
#                 break
#         if next_day == None:
#             next_day = '추가등록이 필요합니다'
        

#     except :
#         return render(request,'student/error.html',{'is_study':False})

#     return render(request,'student/detail.html',{'student':student,'days':days,'next_day':next_day})
   
@login_required(login_url='/login/')
def change(request): # 변경하기 화면
    student = Student.objects.get(user_id = request.user.id)
    if request.method == 'POST':
        student = Student.objects.get(user_id = request.user.id)

        i = int(request.POST['i']) #몇주차 변경하는지
        date = datetime.date.fromisoformat(request.POST['day'])
        today = datetime.date.today()

        base_date = student.base_date #기준 주차 첫 참여일
        first_date = base_date - timedelta(weeks=1-i,days=base_date.isoweekday()-1) #해당 주차의 첫째주
        last_date = base_date - timedelta(weeks=1-i,days=base_date.isoweekday()-7)
        
        if (date - today).days >= 2 and first_date <= date <= last_date: #2일 뒤부터 and 그 주의 첫날과 마지막날 사이여야함
            setattr(student,f'day{i}',request.POST['day'])
            student.save()
            return redirect('inquire')
        else:
            return render(request,'change.html',{'student' : student, 'error':'규정에 따른 날짜를 다시 입력해주세요'})
    return render(request,'change.html',{'student' : student})
    


# @login_required(login_url='/login/')
# def change_day(request,i): #요일변경
#     if request.method == 'POST':
#         student = Student.objects.get(user_id = request.user.id)
#         date = datetime.date.fromisoformat(request.POST['day'])
#         today = datetime.date.today()
#         base_date = student.base_date #기준 주차 첫 참여일
#         first_date = base_date - timedelta(weeks=1-i,days=base_date.isoweekday()-1) #해당 주차의 첫째주
#         last_date = base_date - timedelta(weeks=1-i,days=base_date.isoweekday()-7)
#         if (date - today).days >= 2 and first_date <= date <= last_date: #2일 뒤부터 and 그 주의 첫날과 마지막날 사이여야함
#             setattr(student,f'day{i}',request.POST['day'])
#             student.save()
#             return redirect('detail')
#         else:
#             return render(request,'student/change_day.html',{'error':'날짜를 다시 입력해주세요'})
#     return render(request,'student/change_day.html')





def login_hw(request): # 로그인 화면
    if request.method == 'POST':
        form = Login_form(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username = username , password = password)

            if user is not None :
                auth.login(request,user)
                return redirect('index')
           
            return render(request,'login.html',{'error':'아이디 혹은 비밀번호가 틀렸습니다'})    
       
    else:
        return render(request,'login.html')


# def login(request): #로그인
#     if request.method == 'POST':
#         form = Login_form(request.POST)

#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(username = username , password = password)

#             if user is not None :
#                 auth.login(request,user)
#                 return redirect('main')
           
#             return render(request,'student/login.html',{'form':form})    
       
#     else:
#         form = Login_form()
#         return render(request,'student/login.html',{'form':form})  

@login_required(login_url='/login/')
def logout(request): #로그아웃
    auth.logout(request)
    return redirect('index')



def signup_hw(request): # 회원가입 화면
    if request.method == 'POST':
        form = Signup_form(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            password2 = form.cleaned_data['password2']
            email = form.cleaned_data['email']
            name = form.cleaned_data['name']
            if password == password2:
                user = User.objects.create_user(first_name = name,email = email, username = username, password = password)
                user.is_active = False
                user.save()
                
                current_site = get_current_site(request) 
                # localhost:8000
                message = render_to_string('activate.html',{
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token' : default_token_generator.make_token(user)
                })

                act_email = EmailMessage('인증을 위한 메일입니다',message,to=[email])
                act_email.send()
                # user = authenticate(username = username , password = password)
                # auth.login(request,user)
                return redirect('index')
            else:
                return render(request,'signup.html',{'password_error' : '비밀번호를 다시 확인해주세요', 'username' : username})
        else:
            return render(request,'signup.html',{'form_error' : '양식을 정확히 다시 작성해주세요'})
    else:
        return render(request,'signup.html')

    

# def signup(request): #회원가입
#     if request.method == 'POST':
#         form = Signup_form(request.POST)

#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             password2 = form.cleaned_data['password2']
#             if password == password2:
#                 user = User.objects.create_user(username = username,password = password)
#                 user.is_active = False
#                 user.save()
                
#                 current_site = get_current_site(request) 
#                 # localhost:8000
#                 message = render_to_string('activate.html',{
#                     'user': user,
#                     'domain': current_site.domain,
#                     'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#                     'token' : default_token_generator.make_token(user)
#                 })

#                 email = EmailMessage('인증을 위한 메일입니다',message,to=['ppm5377@naver.com'])
#                 email.send()
#                 # user = authenticate(username = username , password = password)
#                 # auth.login(request,user)
#                 return redirect('main')
#             else:
#                 form = Signup_form(initial ={'username':username}) #비밀번호 새로입력받기
                
#                 return render(request,'student/signup.html',{'form' : form})

            
            
           
#         else:
#             return render(request,'student/signup.html',{'form' : form})
#     else:
#         form = Signup_form()
#         return render(request,'student/signup.html',{'form' : form})




def faq(request): # 자주묻는질문 화면
    return render(request, 'faq.html')