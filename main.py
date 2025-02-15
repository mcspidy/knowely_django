# main.py
import init_django_orm  # noqa: E402
from db.models import Chat


def get_actual_chats() -> list[Chat]:
    """
    Returns a list of up-to-date chats. A chat is active when it contains a
    message sent later than 2020.
    """
    return Chat.objects.filter(message__sent__gt="2020-12-31")
