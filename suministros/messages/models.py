from django.db import models

class Messages(models.Model):
    name = models.CharField(default='Stock Insuficiente')
    message = models.CharField(default='El stock del siguiente producto es insuficiente, por favor pida al proveedor')
 
    def __str__(self):
        return self.name
    
