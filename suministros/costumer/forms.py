from .models import Costumer
from django.contrib.auth.forms import UserCreationForm
from django import forms

class CostumerForm(UserCreationForm):
    class Meta:
        model = Costumer;
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2', 'idcard','email'
                  , 'adress', 'cp', 'birth']
        
        widgets = {
            'birth': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}
            )
        }
        