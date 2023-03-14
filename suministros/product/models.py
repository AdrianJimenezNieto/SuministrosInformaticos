from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False, default='Sin nombre')
    categoria = models.CharField(max_length=50, blank=False, null=False, default='Sin nombre')
    shortDescription = models.CharField(max_length=200, blank=False, null=False, default='Sin descripcion')
    description = models.TextField(max_length=1200, blank=False, null=False, default='Sin descripcion')
    ean13 = models.CharField(max_length=13, blank=False, null=False)
    ref = models.CharField(max_length=13, blank=False, null=False)
    stock = models.IntegerField(max_length=2000, blank=False, null=False)
    corridor = models.IntegerField(max_length=50, blank=False, null=False)
    rack = models.IntegerField(max_length=50, blank=False, null=False)
    supPrice = models.FloatField(max_length=10000, blank=False, null=False)
    pvp = models.FloatField(max_length=10000, blank=False, null=False)
    discount = models.FloatField(mac_length=10000, blank=False, null=False)
    finalPrice = models.FloatField(max_length=10000, blank=False, null=False)


    def __str__(self):
        return self.name