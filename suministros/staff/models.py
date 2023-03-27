from django.db import models
from django.contrib.auth.models import User

class Staff(User):
    adress = models.CharField(max_length=50)
    cp = models.CharField(max_length=10)
    idcard = models.CharField(max_length=10, default='00000000X')
    department = models.CharField(max_length=50)
    is_staff = True

    def __str__(self):
        return self.name