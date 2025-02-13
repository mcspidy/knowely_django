import init_django_orm  # noqa: E402
from django.db.models import QuerySet, Q
from db.models import Customer


def get_clients_with_i_and_o() -> QuerySet:
    """
    returns all the customers whose first name starts with the letter I or
    last name contains the letter o
    """
    return (Customer.objects.filter(Q(first_name__startswith="I")
                                    | Q(last_name__icontains="o")))
