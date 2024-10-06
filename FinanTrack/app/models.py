from django.db import models

# Create your models here.
class Pocket(models.Model):
    name = models.CharField(max_length=200)

class Distribution(models.Model):
    pocket = models.ForeignKey(Pocket, on_delete=models.CASCADE)
    percentage = models.IntegerField(default=100)
    cuantity = models.IntegerField(default=0)