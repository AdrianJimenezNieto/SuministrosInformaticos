from django.db import models
from product.models import Product

class StockControl(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=30, default='Stock insuficiente')
