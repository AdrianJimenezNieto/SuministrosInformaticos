from django.db import models
from datetime import date

class Supplier(models.Model):
    name = models.CharField(max_length=50, blank=False)
    username = models.CharField(max_length=50, blank=False)
    info = models.TextField(max_length=1200, blank=False)
    adress = models.CharField(max_length=50, blank=False)
    cp = models.CharField(max_length=50, blank=False)
    dateSingUp = models.DateField(default=date.today)
    email = models.EmailField(max_length=50, blank=False)
    cif = models.CharField(max_length=50, blank=False)
    accessLevel = models.IntegerField(default=2)
    password = models.CharField(max_length=20, blank=False)


    def __str__(self):
        return self.name