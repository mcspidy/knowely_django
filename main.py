import init_django_orm  # noqa: E402
from django.db.models import QuerySet, F


from db.models import LoyaltyProgramParticipant


def get_customers_with_no_bonuses() -> QuerySet[dict]:
    """    
    Returns a QuerySet of dictionaries containing all customers' phone numbers
    who currently have zero active bonuses.
    """    
    return LoyaltyProgramParticipant.objects.filter(active_bonuses=0).values("customer__phone_number")
