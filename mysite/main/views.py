from django.shortcuts import render, redirect
from django.http import HttpResponse, response
from .models import Task
from django.contrib import messages
import datetime

# Create your views here.

def index(request):
    tasks = Task.objects.all()
    if request.method == 'POST':
        title = request.POST['title']
        desc = request.POST['desc']
        due = request.POST['due']
        if len(title) < 3:
            messages.error(request,'Title must be longer than 3 characters long')
        elif len(desc) < 10: 
            messages.error(request,'Description must be longer than 10 characters long')
            return redirect('index')
        else:
            task = Task(title=title, desc=desc, due=due)
            task.save()
            messages.add_message(request, messages.SUCCESS, 'Task created successfully!')
    return render(request, 'index.html', {"tasks":tasks})

def task(request, id):
    task = Task.objects.get(id=id)
    return render(request, 'task.html', {"task":task})