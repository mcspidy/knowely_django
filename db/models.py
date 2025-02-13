from django.db import models


class LoyaltyProgram(models.Model):
    name = models.CharField(max_length=63)
    bonus_percentage = models.IntegerField()
