
from django.contrib import admin
from django.urls import path, include
from .views import home,create,detail,update,delete

urlpatterns = [
    path('', home, name='home'),
    path('create/',create,name='create'),
    path('update/<int:todo_id>',update,name='update'),
    path('detail/<int:todo_id>',detail,name='detail'),
    path('delete/<int:todo_id>',delete,name='delete'),
] 
