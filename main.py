"""
Your task is to write a get_most_active_customers function that returns first
and last names along with the sum of money spent by 5 most active customers
(people who spent the highest amount of money) as a QuerySet of tuples. The
result should be ordered by the sum_of_spent_money field.
"""

# import init_django_orm
from django.db.models import QuerySet, Sum
from db.models import LoyaltyProgramParticipant


def get_most_active_customers() -> QuerySet[tuple]:
    return LoyaltyProgramParticipant.objects.values(
        "first_name", "last_name").annotate(
        sum_of_spent_money=Sum("spent_money")
    ).order_by("-sum_of_spent_money")[:5]
