from django.urls import path
from .views import *

app_name="home"

urlpatterns = [
    #path('', views.index, name='index'),
    path('', IndexView.as_view(), name = 'index'),

    #path('createTodo/', views.createTodo, name="createTodo"),
    path('createTodo/', CreateTodoView.as_view(), name="createTodo"),

    #path('doneTodo/', views.doneTodo, name='doneTodo')
    path('doneTodo/', DoneTodoView.as_view(), name='doneTodo')
]
