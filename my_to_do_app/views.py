from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from django.views import View
from django.views.generic.list import ListView

from .models import *

"""
def index(request):
    todos = Todo.objects.all()
    content = {'todos': todos}
    return render(request, 'my_to_do_app/index.html', content)
"""
class IndexView(ListView):
    template_name = 'my_to_do_app/index.html'
    model = Todo
    # context_object_name = "todo_list"

"""
def createTodo(request):
    user_input_str = request.POST['todoContent']
    new_todo = Todo(content = user_input_str)
    new_todo.save()
    return HttpResponseRedirect(reverse('index'))
"""
class CreateTodoView(View):
    def post(self, request):
        user_input_str = request.POST['todoContent']
        new_todo = Todo(content=user_input_str)
        new_todo.save()
        return HttpResponseRedirect(reverse('home:index'))

"""
def doneTodo(request):
    done_todo_id = request.GET['todoNum']
    print("완료한 todo의 id", done_todo_id)
    todo = Todo.objects.get(id = done_todo_id)
    todo.isDone = True
    todo.save()
    return HttpResponseRedirect(reverse('index'))
"""
class DoneTodoView(View):
    def get(self, request):
        done_todo_id = request.GET['todoNum']
        todo = Todo.objects.get(id = done_todo_id)
        # todo.isDone = True
        todo.completed = True
        todo.save()
        return HttpResponseRedirect(reverse('home:index'))