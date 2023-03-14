from django.db import models
from datetime import date

class Costumer(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    lastName = models.CharField(max_length=50, blank=False, null=False)
    info = models.TextField(max_length=1200, blank=False, null=False)
    dateSingUp = models.DateField(default=date.today)
    email = models.EmailField(blank=False, null=False)
    birth = models.DateField(blank=False, null=False)
    ident = models.CharField(max_length=50, null=False, blank=False)
    accessLevel = models.IntegerField(default=3)


    def __str__(self):
        return self.name