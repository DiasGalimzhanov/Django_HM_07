from turtle import title
from wsgiref.util import request_uri
from django.shortcuts import render,redirect
from .models import Todo

def home(request):
    todos = Todo.objects.all()
    return render(request, 'home.html', {'todos':todos})

def create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        body = request.POST.get('body')
        deadline = request.POST.get('deadline')
        status = request.POST.get('status')
        Todo.objects.create(title=title,body=body,deadline=deadline,status=status)
        return redirect('home')
    return render(request, 'create.html', {'todos': Todo.objects.all(), 'statuses': Todo.Status.choices})

def detail(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    return render(request,'detail.html', {'todo':todo})

def update(request,todo_id):
    todo = Todo.objects.get(id = todo_id)
    if request.method == "POST":
        title = request.POST.get('title')
        body = request.POST.get('body')
        deadline = request.POST.get('deadline')
        status = request.POST.get('status')
        Todo.objects.filter(id=todo_id).update(title=title,body=body,deadline=deadline,status=status)
        return redirect('home')
    return render(request, 'update.html', {'todo':todo, 'statuses': Todo.Status.choices})

def delete(request, todo_id):
    Todo.objects.filter(id=todo_id).delete()
    return redirect('home')

def get_id(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    return render(request, 'id.html', {'id': todo_id, 'title': todo.title})