from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView ,UpdateView, DeleteView
from .models import Post
from .forms import PostForm
from activity.forms import CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from activity.models import Comment
# Create your views here.


# Create


class AddPost(LoginRequiredMixin, CreateView):
    model = Post 
    template_name = 'mainapp/create_blog.html'
    form_class = PostForm
    success_url = '/'


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# Read
class HomeView(ListView):
    template_name = 'mainapp/home.html'
    model = Post 
    context_object_name = 'posts'

class PostDetails(DetailView):
    template_name = 'mainapp/post.html'
    model = Post 
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['post_comments'] = Comment.objects.filter(post = context['post'])
        return context

# Update
class EditPost(LoginRequiredMixin,UpdateView):
    model=Post
    template_name = 'mainapp/edit_blog.html'
    form_class = PostForm
    success_url = '/'

# Delete
class DeletePost(LoginRequiredMixin,DeleteView):
    model = Post
    template_name = 'mainapp/delete_blog.html'
    success_url = '/'
