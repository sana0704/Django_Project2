from django.db import models
from django.contrib.auth.models import User
from mainapp.models import Post
# Create your models here.

class Comment(models.Model):
    body =models.TextField(max_length=300 , null=True)
    commented_at = models.DateTimeField(auto_now_add=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    