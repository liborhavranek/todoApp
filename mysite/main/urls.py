from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('task/<int:id>', views.task, name='task'),
    path('delete/<int:id>', views.delete_task, name='delete_task'),
    path('home', views.home, name='home'),
]
