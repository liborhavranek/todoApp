from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('task/<int:id>', views.task, name='task'),
    path('delete/<int:id>', views.delete_task, name='delete_task'),
    path('home', views.home, name='home'),
    path('update-complete/<int:id>', views.update_complete, name='update-complete'),
    path('update-complete-task/<int:id>', views.update_complete_task, name='update-complete-task'),
    path('register', views.register, name='register'),
]
