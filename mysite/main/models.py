from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=500)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    time_complete = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True)
    due = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True)


    def __str__(self):
        return self.title
    
    def __str__(self):
	    return self.desc
 
