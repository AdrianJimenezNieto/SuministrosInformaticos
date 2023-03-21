from django import forms

class LoginForm(forms.Form):
    choices = ((1, 'Administrador'),
               (2, 'Proveedor'),
               (3, 'Cliente'),)

    username = forms.CharField(max_length=50, required=True)
    password = forms.CharField(max_length=50,required=True)
    accessLevel = forms.ChoiceField(choices=choices)