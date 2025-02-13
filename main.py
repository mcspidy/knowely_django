import init_django_orm  # noqa: E402
from django.db.models import QuerySet
from db.models import LoyaltyProgramParticipant


def get_not_active_customers_names() -> QuerySet[dict]:
    """
    Returns a list of customer first names of loyalty participants who were
    active in 2021, as a QuerySet of dictionaries with no duplicates.
    """
    return LoyaltyProgramParticipant.objects.filter(
        last_activity__year=2021
    ).values("customer__first_name").distinct()
