from django.shortcuts import render

# Create your views here.
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from .models import UserProfile
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import CreateView,UpdateView

from .forms import *


class CustomLoginView(LoginView):
    template_name = 'authentication/signin.html'
    form_class = CustomLoginForm
    success_url = '/'

class UserRegisterView(CreateView):
    model = User
    template_name = 'authentication/signup.html'
    form_class = CustomRegistrationForm
    success_url = reverse_lazy('signin')


# Profile View
    
def profileView(request):
    if UserProfile.objects.filter(user = request.user).exists():
        template = 'authentication/profile.html'
        context = {
            'userProfile':UserProfile.objects.get(user = request.user)
        }
        return render(request, template, context)
    else:
        return redirect(reverse_lazy('create_profile'))




class CreateProfile(CreateView):
    model = UserProfile
    fields = ['profile_picture','first_name', 'last_name','email','city']
    widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}),
            'profile_picture': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }



    template_name = 'authentication/profile_add.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
