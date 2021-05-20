from django.db import models

# Create your models here.


class HomeData(models.Model):
    differential_pressure = models.FloatField()
    temprature = models.IntegerField()
    relative_humidity = models.IntegerField()

    def __str__(self):
        return self.differential_pressure


class CopperSilver(models.Model):
    type_material = models.CharField(max_length=20)
    amo = models.IntegerField()
    corrosion_rate = models.CharField(max_length=10)
