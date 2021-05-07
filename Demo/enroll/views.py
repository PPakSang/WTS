from django.db.models.query import QuerySet
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views import generic
from .models import *

# Create your views here.


class main_view(generic.TemplateView) :
    template_name = 'enroll/main.html'

    def get_context_data(self, **kwargs):

        user_enroll = Student.objects.filter(user_id = self.request.user.id)
        if bool(user_enroll) : #있으면
            kwargs['ok'] = True
            
        else :
            kwargs['ok'] = False
           

        return super().get_context_data(**kwargs)
    


def enroll_view(request) :
    return render(request,'enroll/enroll.html')


class init_enroll(generic.CreateView):  #등록하기
    model = Student
    fields = ('name','is_new','fixed_day','phone_number')
    template_name = 'enroll/enroll.html'
    
    
    

    def form_valid(self, form) :
        user_enroll = Student.objects.filter(user_id = self.request.user.id)
        if bool(user_enroll) : #있으면
            
            return HttpResponse('이미 등록되었습니다') # 뒤로가기로 재등록 방지
        else : 
            self.object = form.save(commit = False)
            self.object.user_id = self.request.user.id
            self.object.save()

        


        return render(self.request,'enroll/main.html')



def detail_view(request):
    detail = Student.objects.filter(user_id = request.user.id)
    
    return render(request,'enroll/detail.html',{'student' : detail[0]})