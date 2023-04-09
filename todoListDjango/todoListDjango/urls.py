from django.contrib import admin
from django.urls import path
from todo_list import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', views.todo_list, name='todo_list'),
]