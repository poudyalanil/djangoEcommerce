from django.db import models
import datetime


class Products(models.Model):
    sku = models.CharField(max_length=200)
    #date_added = datetime.datetime.now()
    p_tittle = models.CharField(max_length=200)
    img_url = models.CharField(max_length=208)
    p_description = models.TextField()
    p_price = models.FloatField()
