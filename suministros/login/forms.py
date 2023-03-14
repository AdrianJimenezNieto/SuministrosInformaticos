from django.forms import ModelForm
from .models import Login

class LoginForm(ModelForm):
    class Meta:
        model = Login
        exclude = ('accessLevel', '')