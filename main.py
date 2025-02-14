# main.py
import init_django_orm  # noqa: E402
from db.models import Chat


def get_untitled_chats() -> list[Chat]:
    """
    Returns chats whose titles start with the Untitled string.

    For example, the following should be considered as untitled
        chats Untitled,
        Untitled(1),
        Untitled(2)

    """
    return Chat.objects.filter(title__startswith="Untitled")
