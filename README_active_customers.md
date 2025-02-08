# Get most active customers

Loyalty programs are created to encourage people to choose your service among many competitors. A shop has several loyalty programs because the more a customer buys, the bigger discount they get. Let's imagine you've already created your loyalty system.

It contains the following models (main.py):

    from django.db import models


    class Customer(models.Model):
        first_name = models.CharField(max_length=64)
        last_name = models.CharField(max_length=64)
        phone_number = models.CharField(max_length=20)


    class LoyaltyProgram(models.Model):
        name = models.CharField(max_length=64)
        bonus_percentage = models.IntegerField()


    class LoyaltyProgramParticipant(models.Model):
        customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
        loyalty_program = models.ForeignKey(LoyaltyProgram, on_delete=models.PROTECT)
        last_activity = models.DateField(auto_now=True)
        active_bonuses = models.IntegerField(default=0, null=True, blank=True)
        sum_of_spent_money = models.IntegerField(default=0)

Your task is to write a get_most_active_customers function that returns first and last names along with the sum of money spent by 5 most active customers (people who spent the highest amount of money) as a QuerySet of tuples. The result should be ordered by the sum_of_spent_money field.
