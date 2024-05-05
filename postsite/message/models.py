from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Message(models.Model):
    sender = models.ForeignKey(User,on_delete=models.CASCADE,related_name='sent',verbose_name='送信者')
    recipient = models.ForeignKey(User,on_delete=models.CASCADE,related_name='received',verbose_name='受信者')
    title = models.CharField('件名',max_length=50,blank=False)
    text = models.TextField('内容',blank=False)
    viewed = models.BooleanField('閲覧',default=False)
    created_at = models.DateTimeField('送信日時',auto_now_add=True)
    
    