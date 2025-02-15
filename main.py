# main.py
from django.db.models import Q
import init_django_orm  # noqa: E402
from db.models import Message


def get_delivered_or_admin_messages() -> list[Message]:
    """
    return a list of messages that was delivered or sent by a user whose first
    name starts with "admin" prefix
    """
    return Message.objects.filter(
        Q(is_delivered=True) | Q(user__first_name__istartswith="admin")
    ).all()
