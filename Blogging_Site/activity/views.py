from django.shortcuts import render
from .models import Comment, Like 
from mainapp.models import Post
from authentication.models import UserProfile
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


class DeleteComment(DeleteView):
    model = Comment
    template_name = 'authentication/delete_comment.html'
    success_url = '/'
    
    

# like

from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Post, Like
from django.urls import reverse_lazy

@login_required
def like_post(request, post_id):
    post = Post.objects.get(id=post_id)
    user = request.user

    liked = Like.objects.filter(post=post, author=user)

    if liked.exists():
        liked.delete()
        is_liked = False
    else:
        Like.objects.create(post=post, author=user)
        is_liked = True

    return redirect(reverse_lazy('homepage')+"#post_"+str(post_id))