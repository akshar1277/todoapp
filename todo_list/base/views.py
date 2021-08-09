
from django.shortcuts import render 
# from django.http import HttpResponse
# Create your views here.
from django.views import generic
from .models import Task
from django.urls import reverse_lazy


from django.contrib.auth.views import LoginView


class CustomLoginView(LoginView):
    template_name='base/login.html'
    fields="__all__"
    redirect_authenticated_user=True

    def get_success_url(self):
        return reverse_lazy('tasks')















class TaskList(generic.ListView):
    model = Task
    context_object_name= 'tasks'

    

class TaskDetail(generic.DetailView):
    model = Task
    context_object_name='task'
    template_name='base/task.html'


class TaskCreate(generic.CreateView):
    model= Task
    fields ='__all__'
    success_url=reverse_lazy('tasks')

class TaskUpdate(generic.UpdateView):
    model= Task
    fields ='__all__'
    success_url=reverse_lazy('tasks')


class deleteView(generic.DeleteView):
    model=Task
    context_object_name='task'
    success_url=reverse_lazy('tasks')




