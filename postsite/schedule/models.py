from django.db import models
from django.conf import  settings

class Event(models.Model):
    title = models.CharField(max_length=50)
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)
    memo = models.TextField(blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)


# Create your models here.
