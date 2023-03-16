from django import forms

class LoginForm(forms.Form):

    username = forms.CharField(max_length=50, required=True)
    password = forms.CharField(max_length=50,required=True)
    accessLevel = forms.IntegerField(min_value=1,max_value=3, required=True)