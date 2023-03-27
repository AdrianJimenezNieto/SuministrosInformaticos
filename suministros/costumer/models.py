from django.db import models
from django.contrib.auth.models import User

class Costumer(User):
    
    birth = models.DateField()
    idcard = models.CharField(max_length=10, default='00000000X')
    adress = models.CharField(max_length=20, default='No adress')
    cp = models.CharField(max_length=5, default='00000')
    isCostumer = models.BooleanField(default=True)
    isSupplier = models.BooleanField(default=False)

    def __str__(self):
        return self.name