from .models import Supplier
from django.contrib.auth.forms import UserCreationForm

class SupplierForm(UserCreationForm):
    class Meta:
        model = Supplier;
        fields = ['first_name', 'password1', 'password2', 'cif', 'email', 'adress', 'cp', 'info']

        
        
        
        