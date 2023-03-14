from django.forms import ModelForm
from .models import Staff

class StaffForm(ModelForm):
    class Meta:
        model = Staff;
        fields = '__all__'