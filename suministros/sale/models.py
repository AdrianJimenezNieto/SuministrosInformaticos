from django.db import models
from product.models import Product
from django.contrib.auth.models import User
from datetime import date

class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    amount = models.IntegerField(default=1)
    date = models.DateField(default=date.today())