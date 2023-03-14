from django.db import models

class Login(models.Model):

    username = models.CharField(max_length=50, blank=False, null=False)
    password = models.CharField(max_length=20, blank=False, null=False)
    accessLevel = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return self.username