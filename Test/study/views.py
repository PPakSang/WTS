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
        days =get_days(student)
        for i in days :
            if (i - datetime.date.today()).days>=0:
                next_day = i
                break
        if next_day == None:
            next_day = '추가등록이 필요합니다'
        

    except :
        return render(request,'student/error.html',{'is_study':False})

    return render(request,'student/detail.html',{'student':student,'days':days,'next_day':next_day})
    



class Enroll(LoginRequiredMixin,generic.CreateView): #등록하기
    model = Student
    fields=['name','number','level','day1']
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
        for i in range(2,5):
            setattr(form,f'day{i}',form.day1 + timedelta(weeks=i-1))
        form.base_date = form.day1
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



def only_admin(request):
    if request.user.is_staff:
        if request.method == 'POST' :
            students = Student.objects.filter(name = request.POST['name'])
            return render(request,'student/admin.html',{'students':students})
        studetns =Student.objects.all()
        

        return render(request,'student/admin.html',{'students':studetns})
    else:
        return redirect('main')


@login_required(login_url='/login/')
def change_day(request,i):
    if request.method == 'POST':
        
        student = Student.objects.get(user_id = request.user.id)
        date = datetime.date.fromisoformat(request.POST['day'])
        today = datetime.date.today()
        base_date = student.base_date #기준 주차 첫 참여일
        first_date = base_date - timedelta(weeks=1-i,days=base_date.isoweekday()-1) #해당 주차의 첫째주
        last_date = base_date - timedelta(weeks=1-i,days=base_date.isoweekday()-7)
        if (date - today).days >= 2 and first_date <= date <= last_date:
            setattr(student,f'day{i}',request.POST['day'])
            student.save()
            return redirect('detail')
        else:
            return render(request,'student/change_day.html',{'error':'날짜를 다시 입력해주세요'})
    return render(request,'student/change_day.html')



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


def get_days(student):
    arr = [student.day1,student.day2,student.day3,student.day4]
    return arr
    