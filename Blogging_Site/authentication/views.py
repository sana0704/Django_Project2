from django.shortcuts import render

# Create your views here.

from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView

from django.urls import reverse_lazy
from django.views.generic import CreateView

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

    