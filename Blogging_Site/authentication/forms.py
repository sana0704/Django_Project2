
from django.contrib.auth.models import User
from django import forms

from django.contrib.auth.forms import UserCreationForm , AuthenticationForm


class CustomRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields

        username = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Enter your username'
                }
            )
        )

        password1 = forms.CharField(
            label='password',
            widget=forms.PasswordInput(
                attrs=
                {
                    'class':'form-control',
                    'placeholder':'Enter your password'
            
            }
            )
        )

        Confirm_Password = forms.CharField(
        label = 'Confirm Password',
        widget = forms.PasswordInput(
            attrs={
                'class':'form-control', 'placeholder' : 'Confirm your password.'
            }
        )
    )
class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
    widget = forms.TextInput(
    attrs={
                'class':'form-control', 'placeholder' : 'Enter your username'
            }
        )
    )
    password = forms.CharField(
        widget = forms.PasswordInput(
            attrs={
                'class':'form-control', 'placeholder' : 'Enter your password.'
            }
        )
    )



