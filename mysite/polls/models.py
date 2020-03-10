from django.db import models

# Create your models here.
class TrendType(models.Model):
    name = models.CharField(max_length=100)
    kw_find = models.CharField(max_length=100)
