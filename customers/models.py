from django.db import models


class Customer(models.Model):
    username = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_number = models.IntegerField()
    country = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipCode = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    landmark = models.CharField(max_length=200)
