from django.db import models
from django.contrib.auth.models import User

class Costumer(User):
    
    birth = models.DateField()
    idcard = models.CharField(max_length=10, default='00000000X')
    accessLevel = models.IntegerField(default=1)

    def __str__(self):
        return self.name