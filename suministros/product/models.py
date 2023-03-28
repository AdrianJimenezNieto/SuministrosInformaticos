from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50, blank=False, null=True)
    categoria = models.CharField(max_length=50, blank=False, null=True)
    shortDescription = models.CharField(max_length=200, blank=False, null=True)
    description = models.TextField(max_length=800, blank=False, null=True)
    ean13 = models.CharField(max_length=13, blank=False, null=True)
    ref = models.CharField(max_length=13, blank=False, null=True)
    stock = models.IntegerField(blank=False)
    rack = models.IntegerField(blank=False, null=True)
    supPrice = models.FloatField(blank=False, null=True)
    pvp = models.FloatField(blank=False, null=True)
    discount = models.FloatField(blank=False, null=True)
    finalPrice = models.FloatField(blank=False, null=True)


    def __str__(self):
        return self.name