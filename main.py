import init_django_orm  # noqa: E402
from django.db.models import QuerySet


from db.models import LoyaltyProgramParticipant


def get_most_active_customers() -> QuerySet[tuple]:
    pass
