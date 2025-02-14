# main.py
import init_django_orm  # noqa: E402
from db.models import Message


def get_users_who_sent_messages_in_2015() -> list[str]:
    """
    return a list of tuples with the first_name and last_name of the users who sent messages in 2015. Use values_list.
    """
    return list(
        Message.objects.filter(sent__year=2015).values_list(
            "user__first_name", "user__last_name"
        )
    )
