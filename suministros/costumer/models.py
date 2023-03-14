from django.db import models
from datetime import date

class Costumer(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    username = models.CharField(max_length=50, blank=False)
    lastName = models.CharField(max_length=50, blank=False)
    info = models.TextField(max_length=1200, blank=False)
    dateSingUp = models.DateField(default=date.today)
    email = models.EmailField(max_length=50, blank=False)
    birth = models.DateField(blank=False)
    ident = models.CharField(max_length=50, null=False, blank=False)
    accessLevel = models.IntegerField(default=1)
    password = models.CharField(max_length=20, blank=False)


    def __str__(self):
        return self.name