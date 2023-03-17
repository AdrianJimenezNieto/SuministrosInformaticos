from django.db import models
from costumer.models import Costumer
from product.models import Product

class ShoppingCart(models.Model):

    user = models.ForeignKey(Costumer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)