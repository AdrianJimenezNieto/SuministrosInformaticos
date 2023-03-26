from django.db import models
from django.contrib.auth.models import User

class Supplier(User):
    info = models.TextField(max_length=1200)
    adress = models.CharField(max_length=50)
    cp = models.CharField(max_length=10)
    cif = models.CharField(max_length=10, default='00000000X')

    def __str__(self):
        return self.name