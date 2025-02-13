# Get customers with i and o

Loyalty programs are created to encourage people to choose your service among many competitors. A shop has several loyalty programs because the more a customer buys, the bigger discount they get. Let's imagine you've already created your loyalty system.

It contains the following model:

    from django.db import models


    class Customer(models.Model):
        first_name = models.CharField(max_length=64)
        last_name = models.CharField(max_length=64)
        phone_number = models.CharField(max_length=20)

Your task is to write a get_clients_with_i_and_o function that returns all the customers whose first name starts with the letter I or last name contains the letter o.
