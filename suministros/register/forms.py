from django import forms

class RegisterAccessLevelForm(forms.Form):
    choices = ((1, 'Cliente'),
               (2, 'Proveedor'),
               (3, 'Administrador'),)

    accessLevel = forms.ChoiceField(choices=choices)
