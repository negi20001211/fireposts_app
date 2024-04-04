from django.db import models
from django.conf import  settings

class Post(models.Model):
    
    title = models.CharField('タイトル',max_length = 120)
    text = models.TextField('投稿文',blank = True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name='投稿者',on_delete=models.CASCADE)
    created_at = models.DateTimeField('投稿日',auto_now_add=True)
    update_at = models.DateTimeField('更新日',auto_now=True)
    file = models.FileField('添付ファイル',blank=True)
