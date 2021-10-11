from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class Product (models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField(max_length=1000)
    price = models.FloatField()
