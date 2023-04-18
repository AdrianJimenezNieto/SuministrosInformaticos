from .models import Supplier
from django.contrib.auth.forms import UserCreationForm
from django import forms

class SupplierForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].label = 'CONTRASEÑA'
        self.fields['password2'].label = 'CONFIRMACION CONTRASEÑA'
        self.fields['username'].label = 'NOMBRE DE USUARIO'

        self.fields['username'].help_text = 'Requerido. Aceptados caracteres alfanumericos y @/./+/-/_ solo.'
        self.fields['password1'].help_text = '''
        Tu contraseña no puede ser similar al resto de informacion.<br>
        Tu contraseña debe tener al menos 8 caracteres.<br>
        Tu contraseña no debe ser usada comunmente.<br>
        Tu contraseña no puede ser solo numérica.'''
        self.fields['password2'].help_text = 'Introduzca la misma contraseña para verificar.'


    class Meta:
        model = Supplier;
        fields = ['first_name', 'username', 'password1', 'password2', 'cif', 'email', 'adress', 'cp', 'info']
        
        widgets = {
            'info': forms.TextInput(
                attrs= {'type': 'text', 'class':'info'}
            )
        }
        
        labels = {
            'first_name': 'NOMBRE',
            'last_name': 'APELLIDOS',
            'cif': 'CIF',
            'email': 'DIRECCION DE EMAIL',
            'adress': 'DIRECCION',
            'cp': 'CÓDIGO POSTAL',
            'info': 'INFORMACIÓN EXTRA',
        }

        
        
        
        