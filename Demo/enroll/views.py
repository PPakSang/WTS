from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import generic
from .models import *

# Create your views here.


class main_view(generic.TemplateView) :
    template_name = 'enroll/main.html'
    
    def get_context_data(self, **kwargs):

        user_enroll = Student.objects.filter(user_id = self.request.user.id)
        if user_enroll.__len__ == '0' :
            kwargs['ok'] = True
        else :
            kwargs['ok'] = False

        return super().get_context_data(**kwargs)
    


def enroll_view(request) :
    return render(request,'enroll/enroll.html')


class init_enroll(generic.CreateView):
    model = Student
    fields = ('name','is_new','fixed_day','phone_number')
    template_name = 'enroll/enroll.html'
    
    
    

    def form_valid(self, form) :
        self.object = form.save(commit = False)
        self.object.user_id = self.request.user.id
        self.object.save()


        return render(self.request,'main')
