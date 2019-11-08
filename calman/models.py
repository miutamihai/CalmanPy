from django.db import models


class FoodStuff(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=200)
    cal100 = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    cal50 = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    cal10 = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return self.name
# Create your models here.
