from django.db import models
from django.contrib.auth.models import User
from mainapp.models import Post
# Create your models here.

# Comment
class Comment(models.Model):
    body = models.TextField(max_length=300 , null=True)
    commented_at = models.DateTimeField(auto_now_add=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE, related_name='author_comments')
    post=models.ForeignKey(Post,on_delete=models.CASCADE, related_name='post_comments')

    def __str__(self):
        return f"{self.author.username} commented on a post by {self.post.author.username} at {self.commented_at}."

# Like
class Like(models.Model):

    liked_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='author_likes')
    post=models.ForeignKey(Post,on_delete=models.CASCADE, related_name='post_likes')

    def __str__(self):
        return f"User : {self.author.username} liked post : {self.post.title} written by : {self.post.author.username.capitalize()}."
    