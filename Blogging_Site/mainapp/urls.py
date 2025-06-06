from django.urls import path
from .views import HomeView, AddPost


urlpatterns = [
    path('', HomeView.as_view(), name = 'homepage'),

    path('blog/add', AddPost.as_view(), name = 'create_blog'),
    # path('blog/add', addPost, name = 'create_blog')
    
]