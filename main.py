# main.py
from django.db.models import Count
import init_django_orm  # noqa: E402
from db.models import User


def get_top_users_by_number_of_the_messages() -> list[User]:
    """
    return the top 3 users by number of messages sent, with an additional
    num_messages field containing a value equal to this number.
    """
    return (
        User.objects.annotate(num_messages=Count("message"))
        .order_by("-num_messages")[:3]
    )
