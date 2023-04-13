from django.db import models
from product.models import Product
from django.contrib.auth.models import User
from datetime import datetime
from supplier.models import Supplier

class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    amount = models.IntegerField(default=1)
    date = models.DateField(default=datetime.now)

class SupplierSale(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    date = models.DateField(default=datetime.now)
    amount = models.IntegerField(default=1)