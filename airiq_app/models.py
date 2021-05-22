from django.db import models

# Create your models here.


class HomeData(models.Model):
    differential_pressure = models.FloatField()
    temprature = models.IntegerField()
    relative_humidity = models.IntegerField()
    metal_loss1 = models.IntegerField()
    metal_loss2 = models.IntegerField()
    cr1 = models.IntegerField()
    cr2 = models.IntegerField()


    def __str__(self):
        return str(self.id)


class CopperSilver(models.Model):
    type_material = models.CharField(max_length=20)
    amo = models.IntegerField()
    corrosion_rate = models.CharField(max_length=10)
