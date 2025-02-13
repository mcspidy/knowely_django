# Get customers with no bonuses

Loyalty programs are created to encourage people to choose your service among many competitors. A shop has several loyalty programs because the more a customer buys, the bigger discount they get. Let's imagine you've already created your loyalty system.

It contains the following models:

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
        last_activity = models.DateField()
        active_bonuses = models.IntegerField(default=0, null=True, blank=True)
        sum_of_spent_money = models.IntegerField(default=0)

Your task is to write a get_customers_with_no_bonuses function that returns the phone numbers of all customers who currently have zero active bonuses. The function should return a QuerySet of dictionaries containing the customers' phone numbers.

