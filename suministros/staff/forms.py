from .models import Staff
from django.contrib.auth.forms import UserCreationForm

class StaffForm(UserCreationForm):
    class Meta:
        model = Staff;
        fields = ['first_name', 'last_name', 'username', 
                  'password1', 'password2', 'idcard','email'
                  , 'adress', 'cp', 'department']