from django.shortcuts import render, redirect
from django.http import HttpResponse, response
from .models import Task
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.utils import timezone
from datetime import datetime
from itertools import chain
import datetime

# Create your views here.



@login_required(login_url='/login')
def index(request):
    current_user = request.user
    tasks = Task.objects.filter(user=current_user)
    # First, sort the tasks by due date
    tasks = tasks.order_by('due')
    # Then, separate the completed tasks from the incomplete tasks
    completed_tasks = tasks.filter(complete=True)
    incomplete_tasks = tasks.filter(complete=False)
    # Concatenate the incomplete tasks and the completed tasks to form the final list
    tasks = list(chain(incomplete_tasks, completed_tasks))
    current_time = datetime.datetime.now().astimezone(timezone.utc)

    for task in tasks:
        task.duration = task.due - current_time
    if request.method == 'POST':
        title = request.POST['title']
        desc = request.POST['desc']
        due = request.POST['due']
        user = request.user
        due = datetime.datetime.strptime(due, '%Y-%m-%dT%H:%M')
        if len(title) < 3:
            messages.error(request,'Title must be longer than 3 characters long')
        elif len(desc) < 10: 
            messages.error(request,'Description must be longer than 10 characters long')
        elif due < datetime.datetime.now():
            messages.error(request,'Due date and time must be in the future')
        else:
            task = Task(title=title, desc=desc, due=due, user=user)
            task.save()
            messages.add_message(request, messages.SUCCESS, 'Task created successfully!')
        return redirect('index')
    return render(request, 'index.html', {"tasks":tasks})








@login_required(login_url='/login')
def task(request, id):
    try:
        task = Task.objects.get(id=id)
        current_time = datetime.datetime.now().astimezone(timezone.utc)
        task.duration = task.due - current_time
        return render(request, 'task.html', {"task":task, "duration":task.duration})
    except Task.DoesNotExist:
        messages.error(request, 'Task with id "{}" does not exist'.format(id))
        return redirect('index')
    
@login_required(login_url='/login')
def delete_task(request, id):
    try:
        task = Task.objects.get(id=id)
        task.delete()
        messages.success(request, 'Task deleted successfully')
    except Task.DoesNotExist:
        messages.error(request, 'Task does not exist')
    return redirect('index')
    
def home(request):
    return render(request, 'home.html', {})


@login_required(login_url='/login')
def update_complete(request, id):
    if request.method == 'POST':
        task = Task.objects.get(pk=id)
        task.complete = not task.complete
        if task.complete:
            task.time_complete = datetime.datetime.now()
        task.save()
        return redirect('index')
    else:
        return render(request, 'index.html')

@login_required(login_url='/login')
def update_complete_task(request, id):
    if request.method == 'POST':
        task = Task.objects.get(pk=id)
        task.complete = not task.complete
        if task.complete:
            task.time_complete = datetime.datetime.now()
        task.save()
        return redirect('task', id=id)
    else:
        return render(request, 'task/<int:id>')
    


            
def register(request):
    if request.method =='POST':
        email = request.POST["email"]
        username = request.POST["username"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]
        if password !=confirm_password:
            messages.error(request, 'Passwords must be the same')
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
            elif User.objects.filter(email=email).exists(): 
                messages.error(request, 'Email already exists')
            else:
                user = User.objects.create_user(email=email, username=username, password=password)
                user.set_password(password)
                user.save()
                messages.success(request, 'You are registered successfully')
                return redirect('index')
    return render(request, "register.html")


def login_view(request):
    next = request.GET.get('next')
    print(next)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')

@login_required(login_url='/login')
def logout_view(request):
    logout(request)
    return render(request, 'login.html')