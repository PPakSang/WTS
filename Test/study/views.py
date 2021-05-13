import django
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.views import generic
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.decorators import login_required


# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = Signup(request.POST)

        if form.is_valid():
            username = form.cleaned_data['user_name']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username = username,password = password)
            user.save()
            user = authenticate(username = username , password = password)
            auth.login(request,user)
            
            return redirect('main')
        else:
            return render(request,'student/signup.html',{'form' : form})
    else:
        form = Signup()
        return render(request,'student/signup.html',{'form' : form})


@login_required(login_url='signup')         
def main_view(request):

    return render(request,'main.html')

def login(request):
    
    user = authenticate(username = 'admin',password = 'admin')
    auth.login(request,user)
    return redirect('main')