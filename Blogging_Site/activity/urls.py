from django.urls import path
from .views import  addComment

urlpatterns=[
    path('comment/add/<int:post_id>', addComment,name='add_comment' )
]
