from django.shortcuts import render, redirect
from django.http import HttpResponse, response
from .models import Task
from django.contrib import messages
from datetime import datetime
import datetime

# Create your views here.

def index(request):
    tasks = Task.objects.all().order_by('due')
    for task in tasks:
        task.duration = task.due - task.created
    if request.method == 'POST':
        title = request.POST['title']
        desc = request.POST['desc']
        due = request.POST['due']
        due = datetime.datetime.strptime(due, '%Y-%m-%dT%H:%M')
        if len(title) < 3:
            messages.error(request,'Title must be longer than 3 characters long')
        elif len(desc) < 10: 
            messages.error(request,'Description must be longer than 10 characters long')
        elif due < datetime.datetime.now():
            messages.error(request,'Due date and time must be in the future')
        else:
            task = Task(title=title, desc=desc, due=due)
            task.save()
        messages.add_message(request, messages.SUCCESS, 'Task created successfully!')
        return redirect('index')
    return render(request, 'index.html', {"tasks":tasks})






def task(request, id):
    try:
        task = Task.objects.get(id=id)
        return render(request, 'task.html', {"task":task})
    except Task.DoesNotExist:
        messages.error(request, 'Task with id "{}" does not exist'.format(id))
        return redirect('index')
    
    
    
    