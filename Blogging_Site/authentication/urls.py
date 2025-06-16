
from django.urls import path

from . import views

urlpatterns=[
    path('login/',views.CustomLoginView.as_view(), name='signin'),
    path('register/',views.UserRegisterView.as_view(), name='signup'),

    path('profile/', views.profileView, name= 'profile'),
    path('profile/create', views.CreateProfile.as_view(), name = 'create_profile')
]
