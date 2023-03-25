from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    identification = forms.CharField(required=True)
    adress = forms.CharField(required=True)
    cp = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'identification', 'first_name', 'last_name',
                   'adress', 'cp', 'password1', 'password2']