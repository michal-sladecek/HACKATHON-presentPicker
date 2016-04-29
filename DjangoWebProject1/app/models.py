"""
Definition of models.
"""

from django.db import models
import json

# Create your models here.

class DarcekModel(models.Model):
    item_id = models.CharField(max_lenght = 100)
    manufacturer = models.CharField(max_length=100)
    product = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    url = models.URLField()
    picture = models.URLField()
    price_vat = models.CharField(max_length = 25)    