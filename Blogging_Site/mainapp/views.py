from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView ,UpdateView, DeleteView
from .models import Post
from .forms import PostForm
from activity.forms import CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader
from activity.models import Comment, Like
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
    ordering = ['-id']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        posts = context['posts']

        if user.is_authenticated:
            liked_posts = Like.objects.filter(author=user).values_list('post_id', flat=True)
            for post in posts:
                post.is_liked_by_user = post.id in liked_posts
        else:
            for post in posts:
                post.is_liked_by_user = False
        context['search_bar'] = True
        return context


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


def searchView(request):
    query = request.GET.get('search_text')

    result_posts = Post.objects.filter(title__icontains = query)
    context =  {
        'posts' : result_posts,
        'query' : query,
        'search_bar' : True
    }

    template = loader.get_template('mainapp/search_results.html')
    return HttpResponse(template.render(context, request))