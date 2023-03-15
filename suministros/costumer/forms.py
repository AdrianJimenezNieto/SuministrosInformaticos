from django.forms import ModelForm
from .models import Costumer

class CostumerForm(ModelForm):
    class Meta:
        model = Costumer;
        fields = '__all__'