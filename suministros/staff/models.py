from django.db import models
from datetime import date

class Staff(models.Model):
    name = models.CharField(max_length=50, blank=False)
    username = models.CharField(max_length=50, blank=False)
    lastName = models.CharField(max_length=50, blank=False)
    adress = models.CharField(max_length=50, blank=False)
    cp = models.CharField(max_length=50, blank=False)
    dateSingUp = models.DateField(default=date.today)
    email = models.EmailField(max_length=50, blank=False)
    ident = models.CharField(max_length=50, blank=False)
    department = models.CharField(max_length=50, blank=False)
    accessLevel = models.IntegerField(default=3)
    password = models.CharField(max_length=20, blank=False)


    def __str__(self):
        return self.name