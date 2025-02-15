# main.py
import init_django_orm  # noqa: E402
from db.models import Message


def get_last_5_messages_dicts() -> list[dict]:
    """
    return a list containing the last five messages. Each message should be
    represented as a dict with the following fields:

        "from" - sender's username
        "text" - message text
    """
    messages = Message.objects.order_by("-sent")[:5]
    return [
        {"from": message.user.username, "text": message.text}
        for message in messages
    ]
