from django.db import models

#This function is to distribute the quantities
def applyPercentage(amount: int):
    Pocket.total += amount
    Pocket.basic += amount*Pocket.basicPercentage
    Pocket.nonBasics += amount*Pocket.nonBasicsPercentage
    Pocket.savingsAndInvestment += amount*Pocket.savingsAndInvestmentPercentage

# Create your models here.
class Pocket(models.Model):
    total = models.IntegerField()
    basicPercentage = models.IntegerField(null=False,default=50)
    basic = models.IntegerField()
    nonBasicsPercentage = models.IntegerField(null=False,default=25)
    nonBasics = models.IntegerField()
    savingsAndInvestmentPercentage = models.IntegerField(null=False,default=25)
    savingsAndInvestment = models.IntegerField()