from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from app.models import *
from django.urls import *
from django.urls import reverse_lazy
# Create your views here.


class Home(TemplateView):
    template_name='app/home.html'


class SchoolList(ListView):
    model=School
    context_object_name='School'

class School_detail(DetailView):
    model=School
    context_object_name='school'



class SchoolCreate(CreateView):
    model=School
    fields='__all__'


class SchoolUpdate(UpdateView):
    model=School
    fields='__all__'

class SchoolDelete(DeleteView):
    model=School
    success_url=reverse_lazy('SchoolList')


    

