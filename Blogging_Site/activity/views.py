from django.shortcuts import render
from .models import Comment, Like
from mainapp.models import Post
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView,CreateView,DeleteView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.http import JsonResponse
# Create your views here.



def addComment(request, post_id):
    if request.method == 'POST':
        this_post = Post.objects.get(id=post_id)
        comment_body = request.POST.get('body')
        this_comment = Comment.objects.create(body=comment_body,author=request.user,post=this_post)
        this_comment.save()
        return redirect(reverse('detail_blog' , kwargs={'pk': this_post.pk}) + "#comments")





def likePost(request, post_id):
    user = request.user 
    this_post = Post.objects.get(id = post_id)

    if like := Like.objects.filter(author = user, post = this_post):
        like.delete()
        liked = False
    else:
        Like.objects.create(author = user, post = this_post)
        liked = True
    
    context = {
        'liked' : liked,
        'likes' : this_post.get_total_likes
    }
    return JsonResponse(context)