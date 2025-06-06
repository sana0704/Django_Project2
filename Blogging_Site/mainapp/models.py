from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=255, null = True)
    content = models.TextField(max_length=500 ,null = True)
    image = models.ImageField(upload_to='post_images/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    posted_at = models.DateTimeField(auto_now_add= True)


    def __str__(self):
        return f"{self.title.capitalize()} by {self.author.username.capitalize()}."
