from django.db import models
from django.contrib.auth.models import User

class Supplier(User):
    info = models.TextField(max_length=1200, null=True)
    adress = models.CharField(max_length=50, null=True)
    cp = models.CharField(max_length=10, null=True)
    cif = models.CharField(max_length=10, default='00000000X', null=True)
    isCostumer = models.BooleanField(default=False, null=True)
    isSupplier = models.BooleanField(default=True, null=True)

    def __str__(self):
        return self.username