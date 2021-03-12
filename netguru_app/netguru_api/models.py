from django.db import models


# Create your models here.
class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    avg_rating = models.FloatField(default=0.0)
    rates_number = models.IntegerField(default=0)

