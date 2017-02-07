from django.db import models


class Location(models.Model):
    lat = models.DecimalField(max_digits=15, decimal_places=8)
    long = models.DecimalField(max_digits=15, decimal_places=8)
    pcn = models.CharField(max_length=255)
    timestamp = models.DateTimeField()
