# Get all loyalty program names

Loyalty programs are created to encourage people to choose your service among many competitors. A shop has several loyalty programs because the more a customer buys, the bigger discount they get. Let's imagine you've already created your loyalty system.

It contains the following model:

    from django.db import models

    class LoyaltyProgram(models.Model):
        name = models.CharField(max_length=64)
        bonus_percentage = models.IntegerField()

Your task is to write a get_all_loyalty_program_names() function that returns all the names and bonus percentages of existing loyalty programs as a QuerySet containing tuples.
