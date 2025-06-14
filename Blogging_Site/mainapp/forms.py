# from django.forms import ModelForm
# from .models import Post

# class PostForm(ModelForm):
#     class Meta:
#         model = Post 
#         fields = [
#             'title',
#             'subtitle',
#             'content',
#             'image'
#         ]

from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'subtitle', 'content', 'image']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter post title'
            }),
            'subtitle': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter subtitle'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write your blog content here...',
                'rows': 6
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
        }
