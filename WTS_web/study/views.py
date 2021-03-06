from datetime import timedelta
from typing import ContextManager
from django.db.models.query import QuerySet
from django.http import response,HttpResponse
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
from django.contrib import messages

import json
# Create your views here.






def only_admin(request,option):
    if request.user.is_staff:

        if option == 'all':
            new_students = Student.objects.filter(deposit = '1')
            students = Student.objects.all().exclude(deposit= '1')
            return render(request,'study/admin.html',{'students':students, 'new_students':new_students})

        if option == 'today':
            new_students = Student.objects.filter(day1 = datetime.date.today())
            students = Student.objects.filter(day2 = datetime.date.today())
            students = students | Student.objects.filter(day3 = datetime.date.today())
            students = students | Student.objects.filter(day4 = datetime.date.today())
            return render(request,'study/admin.html',{'new_students': new_students,'students':students})
            

        if option == 'name':
            if request.method == 'POST' :
                students = Student.objects.filter(name = request.POST['name'])
                return render(request,'study/admin.html',{'students':students})

        if option == 'number':
            if request.method == 'POST' :
                students = Student.objects.filter(number = request.POST['number'])
                return render(request,'study/admin.html',{'students':students})
        if option == 'new':
            new_students = Student.objects.filter(day1 = datetime.date.today())
            return render(request,'study/admin.html',{'new_students':new_students})
    else:
        return redirect('index')


def check_deposit(request,option,user_id):
    if request.user.is_staff:
        student = Student.objects.get(pk = user_id)
        student.deposit = option
        student.save()
        return redirect('deposit_view','all')
    else:
        return redirect('index')

def deposit_view(request,option):
    if request.user.is_staff:
        if option == 'name':
            if request.method == 'POST':
                students = Student.objects.filter(name = request.POST['name'])
                return render(request,'study/depositview.html',{"students" : students})
        if option == 'number':
            if request.method == 'POST':
                students = Student.objects.filter(number = request.POST['number'])
                return render(request,'study/depositview.html',{"students" : students})
        if option == 'not':
            students = Student.objects.all().exclude(deposit = "3")
            return render(request,'study/depositview.html',{"students" : students})
        if option == 'today':
            students = Student.objects.all().exclude(deposit = '3')
            students = students.filter(day1 = datetime.date.today())
            return render(request,'study/depositview.html',{"students" : students})

        students = Student.objects.all()
        return render(request,'study/depositview.html',{"students" : students})
    else:
        return redirect('index')


def check_in(request,user_id):
    if request.user.is_staff:
        student = Student.objects.get(pk = user_id)
        student.check_in = str(student.check_in) + str(datetime.date.today())+'/'
        print()
        student.save()
        return redirect('adminpage','today')
    else:
        return redirect('index')



            # studetns =Student.objects.all()

    #         return render(request,'admin.html',{'students':studetns})
    #     elif option == 'today':
    #         if request.method 
    # else:
    #     return redirect('index')






# @login_required(login_url='/login/')
# def change_day(request):  #????????????
#     try:
#         student = Student.objects.get(user_id = request.user.id)
#         if request.method == 'POST':
#             form = Select_day_form(request.POST)
#             if form.is_valid():
#                 # ?????? 2??? ??? ??????
#                 if (form.cleaned_data['changed_day'] - datetime.date.today()).days <2 : 
#                     return HttpResponse('????????? ?????? ??????????????????')
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




    

############################ view??? ?????? ????????????


def get_basedates(student): #??? ?????? ?????????
    arr = []
    for i in range(0,4):
        arr.append(str(student.base_date + timedelta(weeks=i)))
    return arr

def get_days(student): #????????? ??????
    arr = []
    arr.append(student.day1)
    arr.append(student.day2)
    arr.append(student.day3)
    arr.append(student.day4)
    return arr

############################  



############### ??????????????? ????????? ???  ################

#function_view

def get_left_day(student):
    days = get_days(student)
    left_day = 4
    for i in days :
        if (i - datetime.date.today()).days>=0:
            break
        left_day -= 1
    return left_day


def index(request): # ?????? ??????
    try:
        student = Student.objects.get(user_id = request.user.pk)
        left_day = get_left_day(student)
        if left_day == 0 :
            return render(request, 'study/main/index.html',{"enroll" : "???????????????","is_zero" : True})
        else:
            return render(request, 'study/main/index.html',{"enroll" : "???????????????","is_zero" : False})
    except:
        return render(request, 'study/main/index.html',{"enroll" : "????????????"})



@login_required(login_url='/user/login/')
def enroll(request): # ???????????? ??????
    try:
        student = Student.objects.get(user_id = request.user.id)
        left_day = get_left_day(student)
        if left_day != 0 : #?????? ????????????
            messages.error(request, "?????? ?????????????????????!")
            return render(request, 'study/function/enroll.html',{"error" : "????????? ?????? ????????? ????????? ????????? ?????? ??? ???????????????."})
        else:
            student.user_id = 0
            student.save()
            return render(request, 'study/function/enroll.html')
    except:
        if request.method == 'POST':
            form = Enroll_form(request.POST)
            day1 = datetime.date.fromisoformat(request.POST['day1'])

            if  day1 < datetime.date.today(): #?????? ??? ????????? ???
                messages.error(request, "?????? ??????!")
                return render(request,'study/function/enroll.html',{"error" : "???????????? ????????? ??? ????????????."})

            if day1 == datetime.date.today() + timedelta(days=1) and datetime.datetime.today().hour >=22: #?????? 10??? ????????? ????????? ????????? ???
                messages.error(request, "?????? ??????!")
                return render(request,'study/function/enroll.html',{"error" : "22??? ???????????? ????????? ????????? ???????????????."})

            if form.is_valid() :
                form = form.save(commit = False)
                for i in range(2,5):
                    setattr(form,f'day{i}',form.day1 + timedelta(weeks=i-1))
                for i in range(2,5):
                    setattr(form,f'time{i}',form.time1)
                form.base_date = form.day1
                form.user_id = request.user.id
                form.name = request.user.first_name
                form.save()

                return redirect('inquire')
            else:
                messages.error(request,'?????? ??????!')
                return render(request,'study/function/enroll.html')
        return render(request, 'study/function/enroll.html')



# class Enroll(LoginRequiredMixin,generic.CreateView): #????????????
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

@login_required(login_url='/user/login/')
def inquire(request): # ???????????? ??????
    try:
        student = Student.objects.get(user_id = request.user.id)
        days =get_days(student)
        left_day = 4
        day = 1
        next_day = None
        for i in days :
            if (i - datetime.date.today()).days>=0:
                next_day = i
                next_time = getattr(student,f'time{day}')
                break
            day += 1
            left_day -= 1
        if next_day == None:
            next_time = '??????????????? ???????????????'
            next_day = '??????????????? ???????????????'
        else:
            times = ['??????','??????1???','??????4???']
            next_time = times[int(next_time)]
        base_dates = get_basedates(student)
    except Exception as e :
        print(e)
        return redirect('enroll')

    return render(request,'study/function/inquire.html',
    {'student' : student,
    'days' : days,
    'next_day': next_day,
    'left_day' : left_day,
    'base_dates' : base_dates,
    'next_time' : next_time}
    )   


# @login_required(login_url='/login/')
# def my_study(request): #????????????

#     try:
#         student = Student.objects.get(user_id = request.user.id)
#         days =get_days(student)
#         for i in days :
#             if (i - datetime.date.today()).days>=0:
#                 next_day = i
#                 break
#         if next_day == None:
#             next_day = '??????????????? ???????????????'
        

#     except :
#         return render(request,'student/error.html',{'is_study':False})

#     return render(request,'student/detail.html',{'student':student,'days':days,'next_day':next_day})
   
@login_required(login_url='/user/login/')
def change(request): # ???????????? ??????
    try:
        student = Student.objects.get(user_id = request.user.id)
    except:
        return redirect('enroll')
    if request.method == 'POST':
        student = Student.objects.get(user_id = request.user.id)

        try:
            i = int(request.POST['i']) #????????? ???????????????
            if  getattr(student,f'day{i}')<= datetime.date.today(): #???????????? ??????
                messages.error(request, "?????? ??????!")
                return render(request, 'study/function/change.html', {'student': student})
            date = datetime.date.fromisoformat(request.POST['day'])
            today = datetime.date.today()
        except:
            messages.error(request, "?????? ??????!")
            return render(request, 'study/function/change.html', {'student': student})

        base_date = student.base_date #?????? ?????? ??? ?????????
        first_date = base_date - timedelta(weeks=1-i,days=base_date.isoweekday()-1) #?????? ????????? ?????????
        last_date = base_date - timedelta(weeks=1-i,days=base_date.isoweekday()-7)
        

        if (date - today).days >= 2 and first_date <= date <= last_date: #2??? ????????? and ??? ?????? ????????? ???????????? ???????????????
            setattr(student,f'day{i}',request.POST['day'])
            setattr(student,f'time{i}',request.POST['time'])
            student.save()
            return redirect('inquire')
        else:
            messages.error(request, "?????? ??????!")
            return render(request, 'study/function/change.html', {'student': student})
    return render(request,'study/function/change.html',{'student' : student})

    


def faq_view(request): # ?????????????????? ??????
    if request.method == 'POST':
        if request.user.is_authenticated == False :
            return redirect('login')
        else:
            name = request.user.first_name
            answer_to = request.POST['answer_to']
            text = request.POST['text']

            faq = Faq(name = name, answer_to = answer_to, text = text)
            faq.save()
    return render(request, 'study/function/faq.html')



# @login_required(login_url='/login/')
# def change_day(request,i): #????????????
#     if request.method == 'POST':
#         student = Student.objects.get(user_id = request.user.id)
#         date = datetime.date.fromisoformat(request.POST['day'])
#         today = datetime.date.today()
#         base_date = student.base_date #?????? ?????? ??? ?????????
#         first_date = base_date - timedelta(weeks=1-i,days=base_date.isoweekday()-1) #?????? ????????? ?????????
#         last_date = base_date - timedelta(weeks=1-i,days=base_date.isoweekday()-7)
#         if (date - today).days >= 2 and first_date <= date <= last_date: #2??? ????????? and ??? ?????? ????????? ???????????? ???????????????
#             setattr(student,f'day{i}',request.POST['day'])
#             student.save()
#             return redirect('detail')
#         else:
#             return render(request,'student/change_day.html',{'error':'????????? ?????? ??????????????????'})
#     return render(request,'student/change_day.html')







#sign_view

def login_hw(request): # ????????? ??????
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        form = Login_form(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username = username , password = password)

            if user is not None :
                auth.login(request,user)
                return redirect('index')

            messages.error(request, "?????? ??????????????????!")
            return render(request,'study/sign/login.html')
       
    else:
        return render(request,'study/sign/login.html')




def find_id(request):  #id??????
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        user = User.objects.filter(first_name = name, email = email)
        if user.count() != 0: # ==0 ?????? ?????? ????????? ??????
            return render(request,'study/sign/find_id.html',{'username' : 'ID : ' + user[0].username + '?????????'}) 
        else :
            return render(request,'study/sign/find_id.html',{'error' : '?????? ?????? ???????????? ?????? ??????????????????'})        
    return render(request,'study/sign/find_id.html')





def find_pw(request):  #password??????
    if request.method == 'POST':
        name = request.POST['username']
        email = request.POST['email']
        user = User.objects.filter(username = name, email = email)
        if user.count() != 0: # ==0 ?????? ?????? ????????? ??????
            message = render_to_string('reset_pw_message.html',{
                "domain" : get_current_site(request),
                "uid" : urlsafe_base64_encode(force_bytes(user[0].pk)),
                "token" : default_token_generator.make_token(user[0]),
            }) 
            
            email = EmailMessage('???????????? ???????????? ?????????',message,to=[email])
            try:
                if user.last_name == '2' :
                    return render(request,'study/error.html')    
                else:
                    email.send()
                    user.last_name = 2
                    user.save()
            except:
                return render(request,'study/error.html')
            return render(request,'study/sign/find_pw.html',{'message' : '???????????? ?????????????????????'}) 
        else :
            return render(request,'study/sign/find_pw.html',{'error' : '????????? ?????? ???????????? ?????? ??????????????????'})        
    return render(request,'study/sign/find_pw.html')






def reset_pw(request,uid64,token): #password ?????????
    #uid64 ??? ?????? byte ??? ??? uid ?????? ????????? ????????????, ?????? ?????? ?????????
    #????????? ????????? ??? ?????? ?????? str??? ????????????
    uid = force_text(urlsafe_base64_decode(uid64))
    try :
        user = User.objects.get(pk = uid)
        if user is not None and default_token_generator.check_token(user,token): #?????? pk ??? ?????? user??? ????????????, ????????? ????????? ???
            if request.method == 'POST':
                user = User.objects.get(pk = uid)
                password = request.POST['password']
                password2 = request.POST['password2']
                if password == password2:
                    user.set_password(password)
                    user.last_name = 1
                    user.save()
                    return redirect('login')
                else:
                    return render(request,'study/sign/reset_pw.html',{'error' : "??????????????? ?????? ??????????????????"})
            else:
                return render(request,'study/sign/reset_pw.html')
    except:
        return render(request, 'study/error.html')

# def login(request): #?????????
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

@login_required(login_url='/user/login/')
def logout(request): #????????????
    auth.logout(request)
    return redirect('index')

def validate_password(password): #password ???????????????
    validate_list = [
        lambda p : len(p)>= 4,
        lambda p : len(p)<=20,
        lambda p : all(x.islower() or x.isupper() or (x in ['!', '@', '#', '$', '%', '^', '&', '*', '_']) or x.isdigit() for x in p),
        lambda p : any(x.islower() for x in p)
    ]
    for validator in validate_list:
        if not validator(password):
            return True


def signup_hw(request): # ???????????? ??????
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        form = Signup_form(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            password2 = form.cleaned_data['password2']
            email = form.cleaned_data['email']
            name = form.cleaned_data['name']

            if User.objects.filter(username = username).count() != 0 : #ID ?????????
                return render(request,'study/sign/signup.html',{'form_error' : '????????? ????????? ?????? ??????????????????'})
           
            if User.objects.filter(email = email).count() != 0 : #????????? ?????? ???
                return render(request,'study/sign/signup.html',{
                    'email_error' : '????????? ??????????????????', 
                    'username' : username,
                    'email' : email,
                    'name' : name,
                    're' : True}
                    )
            if validate_password(password):
                return render(request,'study/sign/signup.html',{
                    'password_error' : '4?????????, ???????????????, ??????, ???????????? ??????????????? ???????????????', 
                    'username' : username,
                    'email' : email,
                    'name' : name,
                    're' : True}
                    )
            if password == password2 :
                user = User(first_name = name,email = email, username = username)
                user.set_password(password)
                user.is_active = False
                user.save()
                
                
                current_site = get_current_site(request) 
                # localhost:8000
                message = render_to_string('study/sign/activate.html',{
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token' : default_token_generator.make_token(user)
                })
                
                act_email = EmailMessage('[????????????] ????????? ?????? ???????????????',message,to=[email])
                # try:
                #     act_email.send()
                    
                # except:
                #     return render(request, 'study/error.html')
                act_email.send()
                # user = authenticate(username = username , password = password)
                # auth.login(request,user)
                
                return render(request,'study/sign/checkemail.html',{"email" : email})
            else:
                return render(request,'study/sign/signup.html',{
                    'password_error' : '??????????????? ?????? ?????????????????? ', 
                    'username' : username,
                    'email' : email,
                    'name' : name,
                    're' : True}
                    )
        else:
            return render(request,'study/sign/signup.html',{'form_error' : '????????? ????????? ?????? ??????????????????'})
    else:
        return render(request,'study/sign/signup.html')


def re_send(request,email): #????????? ?????????
    try:
        user = User.objects.filter(email = email)[0]
        if(user.last_name == '1'):
            return HttpResponse('?????? ????????? ????????? ??????????????????.')
        user.last_name = 1
        user.save()
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)
        current_site = get_current_site(request)
        message =render_to_string('study/sign/activate.html',{
            "user" : user,
            "uid" : uid,
            "domain" : current_site.domain,
            "token" : token,
        })
        re_email = EmailMessage('[????????????] ???????????? ??????????????????',message,to=[email])
        re_email.send()
        return HttpResponse('success')
    except Exception as e:
        print(e)
        return render(request,'study/error.html')



def validate_username(username): #ID ???????????????
    validate_list = [
        lambda u : len(u)>=5,
        lambda u : len(u)<20,
        lambda u : any(l.islower() for l in u), #????????? ??????
        lambda u : all(l.islower() or l.isdigit() or l =='_' for l in u)] #????????????, ??????, ???????????? ???????????? ????????????
    
    for validator in validate_list :
        if not validator(username):
            return True



def is_duplicated(request): #ID ????????????
    username = request.GET['username']
    if User.objects.filter(username = username).count() != 0 :
        data ={
            "is_dp" : False,
            "message" : "?????? ???????????? ID ?????????"
        }
        return HttpResponse(json.dumps(data))
    elif validate_username(username) :
        data ={
            "is_dp" : False,
            "message" : "5??? ??????, ????????????, ??????, '_' ??????????????? ???????????????"
        }
        return HttpResponse(json.dumps(data))
    else:
        data ={
            "is_dp" : True,
            "message" : "??????????????? ID ?????????"
        }
        return HttpResponse(json.dumps(data))


def activate(request,uid64,token):
    try:
        uid = force_text(urlsafe_base64_decode(uid64))
        user = User.objects.get(pk = uid)
        
        if user is not None and default_token_generator.check_token(user,token):
            user.is_active = True
            user.save()
            auth.login(request,user)
            return redirect('index')
        return redirect('index')
    except Exception as e:
        print(e)
        return render(request,'study/error.html')

    

# def signup(request): #????????????
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

#                 email = EmailMessage('????????? ?????? ???????????????',message,to=['ppm5377@naver.com'])
#                 email.send()
#                 # user = authenticate(username = username , password = password)
#                 # auth.login(request,user)
#                 return redirect('main')
#             else:
#                 form = Signup_form(initial ={'username':username}) #???????????? ??????????????????
                
#                 return render(request,'student/signup.html',{'form' : form})

            
            
           
#         else:
#             return render(request,'student/signup.html',{'form' : form})
#     else:
#         form = Signup_form()
#         return render(request,'student/signup.html',{'form' : form})


def checkemail(request): #???????????? ?????? ?????? ?????????
    return render(request, 'study/sign/checkemail.html')

def testError(request): # ?????? ????????? ?????????
    return render(request, 'study/error.html')