# main.py
import init_django_orm  # noqa: E402
from db.models import Chat


def get_chat_dicts() -> list[dict]:
    """
    return a list of chats represented by dicts. Each dict should contain the
    following fields:

    "id" - chat id
    "title" - chat title
    "users" - a list of the participants' usernames

        chats = get_chat_dicts()
        print(chats[0])
        # {
        #    "id": 1,
        #    "title": "My family",
        #    "users": ["mom", "dad", "me"]
    """
    return [
        {
            "id": chat.id,
            "title": chat.title,
            "users": [user.username for user in chat.users.all()],
        }
        for chat in Chat.objects.all()
    ]
