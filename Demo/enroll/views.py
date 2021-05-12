from django import http
from django.db.models.query import QuerySet
from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views import generic
from .models import *

# Create your views here.


# class main_view(generic.TemplateView) :
#     template_name = 'enroll/main.html'

#     def get_context_data(self, **kwargs):

#         user_enroll = Student.objects.filter(user_id = self.request.user.id)
#         if bool(user_enroll) : #있으면
#             kwargs['ok'] = True
            
#         else :
#             kwargs['ok'] = False
           

#         return super().get_context_data(**kwargs)
    


# def enroll_view(request) :
#     return render(request,'enroll/enroll.html')


# class init_enroll(generic.CreateView):  #등록하기
#     model = Student
#     fields = ('name','is_new','fixed_day','phone_number')
#     template_name = 'enroll/enroll.html'
    
    
    
    

#     def form_valid(self, form) :
#         user_enroll = Student.objects.filter(user_id = self.request.user.id)
#         if bool(user_enroll) : #있으면
            
#             return HttpResponse('이미 등록되었습니다') # 뒤로가기로 재등록 방지
#         else : 
#             self.object = form.save(commit = False)
#             self.object.user_id = self.request.user.id
#             self.object.save()

        


#         return redirect('/')



# def detail_view(request):
#     detail = Student.objects.filter(user_id = request.user.id)
    
#     return render(request,'enroll/detail.html',{'student' : detail[0]})


# class update_enroll(generic.UpdateView):
#     model = Student
#     fields = ('name','is_new','fixed_day','phone_number')
#     template_name = 'enroll/update.html'
#     success_url ='/'
    
#     def get_object(self): 
#         student = Student.objects.get(user_id = self.request.user.id)

#         return student


# def testview(request):
#     return render(request,'main_page/main.html')



class init_enroll(generic.CreateView):
    model = Student
    fields = ('name','is_new','fixed_day','phone_number')
    template_name ='registration/login.html'


    def form_valid(self, form) :
        self.object = form.save(commit = False)
        self.object.user_id = 5378 
        if bool(Student.objects.filter(name = self.object.name,user_id = self.object.user_id)):
            return HttpResponse('이미 있는 계정입니다')
        else :
            self.object.user_id = 5378
            self.object.save()
            return redirect('list')


class enroll_list(generic.ListView):
    model = Student
    fields = '__all__'
    template_name ='list.html'


    
def is_enroll(request):
    if request.method == 'POST':
        name = request.POST['name']
        user_id = request.POST['password']

        user = Student.objects.filter(name=name,user_id = user_id)

        if bool(user):
            return render(request,'list.html',{'object_list' : user})
        else:
            return HttpResponse('실패')
    
    return render(request,'inputtest.html')