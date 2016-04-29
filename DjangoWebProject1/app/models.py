"""
Definition of models.
"""

from django.db import models
import json

# Create your models here.

class DarcekModel(models.Model):
    manufacturer = models.CharField(max_length=100)
    product = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    url = models.URLField()
    picture = models.URLField()
    price_vat = models.IntegerField()
    category_text = models.CharField(max_length = 500)
    