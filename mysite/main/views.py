from django.shortcuts import render
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
        task = Task(title=title, desc=desc, due=due)
        task.save()
        messages.add_message(request, messages.SUCCESS, 'Task created successfully!')
    return render(request, 'index.html', {"tasks":tasks})