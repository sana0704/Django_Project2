from django.urls import path
from .views import  addComment, likePost ,DeleteComment

urlpatterns=[
    path('comment/add/<int:post_id>', addComment,name='add_comment' ),
    path('like/<int:post_id>', likePost, name = 'like_post'),
    path('comment/delete/<int:pk>', DeleteComment.as_view(), name='delete_comment')
]
