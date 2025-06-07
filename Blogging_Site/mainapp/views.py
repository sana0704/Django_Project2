from django.shortcuts import render
from django.views.generic import ListView, CreateView ,UpdateView, DeleteView
from .models import Post
from .forms import PostForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.


class HomeView(ListView):
    template_name = 'mainapp/home.html'
    model = Post 
    context_object_name = 'posts'



class AddPost(LoginRequiredMixin, CreateView):
    model = Post 
    template_name = 'mainapp/create_blog.html'
    form_class = PostForm
    success_url = '/'


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class EditPost(LoginRequiredMixin,UpdateView):
    model=Post
    template_name = 'mainapp/edit_blog.html'
    form_class = PostForm
    success_url = '/'

class DeletePost(LoginRequiredMixin,DeleteView):
    model = Post
    template_name = 'mainapp/delete_blog.html'
    success_url = '/'
# def addPost(request):
#     if request.method == 'GET':
#         form = PostForm()
#         context = {
#             'form' : form
#         }
#         return render(request, 'mainapp/create_blog.html', context)
#     elif request.method == 'POST':