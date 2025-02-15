# main.py
import init_django_orm  # noqa: E402
from db.models import Message


def get_count_messages_sent_by_first_name(first_name: str) -> int:
    """
    return the number of messages sent by all the users with a selected
    first_name
    """
    return Message.objects.filter(user__first_name=first_name).count()
