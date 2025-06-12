from django.shortcuts import render
from .models import Comments
from django.views.generic import ListView,CreateView,DeleteView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

# class AddComment(LoginRequiredMixin,CreateView):
#     model = Comments
#     template_name = 'mainapp/create_blog.html'

# class DeleteComment(LoginRequiredMixin,DeleteView):
#     model=Comments
#     template_name=''

    
# class EditComment(LoginRequiredMixin,UpdateView):
#     model= Comments
#     template_name=''