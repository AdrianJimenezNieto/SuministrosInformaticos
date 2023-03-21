from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50, blank=False)
    categoria = models.CharField(max_length=50, blank=False)
    shortDescription = models.CharField(max_length=200, blank=False)
    description = models.TextField(max_length=1200, blank=False)
    ean13 = models.CharField(max_length=13, blank=False)
    ref = models.CharField(max_length=13, blank=False)
    stock = models.IntegerField(blank=False)
    corridor = models.IntegerField(blank=False)
    rack = models.IntegerField(blank=False)
    supPrice = models.FloatField(blank=False)
    pvp = models.FloatField(10000, blank=False)
    discount = models.FloatField(blank=False)
    finalPrice = models.FloatField(blank=False)


    def __str__(self):
        return self.name