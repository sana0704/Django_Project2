from django.urls import path
from .views import  addComment, like_post ,DeleteComment

urlpatterns=[
    path('comment/add/<int:post_id>', addComment,name='add_comment' ),
    path('like/<int:post_id>', like_post, name = 'like_post'),
    path('comment/delete/<int:pk>', DeleteComment.as_view(), name='delete_comment')
]
