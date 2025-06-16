from django.contrib import admin
from .models import Like
from .models import Comment
# Register your models here.
admin.site.register(Comment)
admin.site.register(Like)