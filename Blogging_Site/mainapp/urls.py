from django.urls import path
from .views import HomeView, AddPost ,EditPost,DeletePost


urlpatterns = [
    path('', HomeView.as_view(), name = 'homepage'),

    path('blog/add', AddPost.as_view(), name = 'create_blog'),
    path('blog/edit/<int:pk>', EditPost.as_view(),name= 'edit_blog'),
    path('blog/delete/<int:pk>',DeletePost.as_view(),name='delete_blog'),
    
    
]