from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=500)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    due = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True)

    def __str__(self):
        return self.title
    
    def __str__(self):
	    return self.desc