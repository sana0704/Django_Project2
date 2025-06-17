from django.db import models
from django.contrib.auth.models import User 


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    profile_picture =  models.ImageField(upload_to='profile_pics/')
    created_at = models.DateTimeField(auto_now_add = True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email=models.CharField(max_length=300, null=True)
    city=models.CharField(max_length=200, null=True)





