from django.urls import path
from todo_list.views import todo_list

urlpatterns = [
    path('todo/', todo_list, name='todo_list'),
]