from django.db import models


class Seller(models.Model):
    pam_number = models.IntegerField()
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_number = models.IntegerField()
    country = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipCode = models.CharField(max_length=200)
