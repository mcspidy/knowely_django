import init_django_orm
from django.db.models import QuerySet, Sum
from db.models import LoyaltyProgramParticipant


def get_most_active_customers() -> QuerySet:
    """
    Returns the first and last names along with the sum of money spent by 5
    most active customers as a QuerySet of tuples. The result is ordered by
    the sum_of_spent_money field.
    """

    return LoyaltyProgramParticipant.objects.values(
        "customer__first_name", "customer__last_name"
    ).annotate(
        sum_of_spent_money=Sum("sum_of_spent_money")
    ).order_by(
        "-sum_of_spent_money"
    ).values_list(
        "customer__first_name", "customer__last_name", "sum_of_spent_money"
    )[:5]
