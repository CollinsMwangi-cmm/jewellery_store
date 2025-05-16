from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={

        'placeholder': 'Email',
        'required': True,
        'id': 'email',
    }))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={

                'placeholder': 'Username',
                'required': True,
                'id': 'username',
            }),
            'password1': forms.PasswordInput(attrs={

                'placeholder': 'Password',
                'required': True,
                'id': 'password1',
            }),
            'password2': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Confirm Password',
                'required': True,
                'id': 'password2',
            }),
        }

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={
        'placeholder': 'Username',
        'required': True,
        'id': 'username',
    }))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={

        'placeholder': 'Password',
        'required': True,
        'id': 'password',
    }))
