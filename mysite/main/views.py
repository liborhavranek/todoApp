from django.shortcuts import render
from django.http import HttpResponse, response
from .models import task

# Create your views here.

def index(request):
    tasks = task.objects.all()
    return render(request, 'index.html', {"tasks":tasks})