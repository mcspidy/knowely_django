from django.db.models import QuerySet

import init_django_orm  # noqa: E402

from db.models import LoyaltyProgram


def get_all_loyalty_program_names() -> QuerySet[tuple]:
    """
    Returns all the names and bonus percentages of existing loyalty programs
    as a QuerySet containing tuples.
    """
    return LoyaltyProgram.objects.values_list("name", "bonus_percentage")
