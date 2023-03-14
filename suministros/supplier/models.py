from django.db import models
from datetime import date

class Supplier(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    info = models.TextField(max_length=1200, blank=False, null=False)
    adress = models.CharField(max_length=50, blank=False, null=False)
    cp = models.CharField(max_length=50, blank=False, null=False)
    dateSingUp = models.DateField(default=date.today)
    email = models.EmailField(blank=False, null=False)
    cif = models.CharField(max_length=50, null=False, blank=False)
    accessLevel = models.IntegerField(default=2)
    

    def __str__(self):
        return self.name