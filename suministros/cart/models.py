from django.db import models
from product.models import Product

class Cart(models.Model):
    created_at = models.DateField()

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)