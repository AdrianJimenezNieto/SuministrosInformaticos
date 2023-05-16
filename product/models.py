from django.db import models
from supplier.models import Supplier

class Product(models.Model):

    name = models.CharField(max_length=50, blank=False, null=True)
    categoria = models.CharField(max_length=50, blank=False, null=True)
    shortDescription = models.CharField(max_length=200, blank=False, null=True)
    description = models.TextField(max_length=800, blank=False, null=True)
    ean13 = models.CharField(max_length=13, blank=False, null=True)
    minStock = models.IntegerField(default=30, blank=False)
    stock = models.IntegerField(default=30, blank=False)
    rack = models.IntegerField(blank=False, null=True)
    pvp = models.FloatField(blank=False, null=True)
    discount = models.FloatField(blank=False, null=True)
    finalPrice = models.FloatField(blank=False, null=True)

    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name