# main_test.py
import pytest

from main import get_chat_dicts
from db.models import User, Chat, Message


@pytest.mark.django_db
def test_get_chat_dicts() -> None:
    users = [
        ("Harry", "Potter", "harry123", "student"),
        ("Hermione", "Granger", "hermione321", "student, 16 y.o."),
        ("Admin", "Admin", "admin1", "admin"),
        ("Admin", "Admin", "admin2", "admin"),
    ]

    for user in users:
        User.objects.create(
            first_name=user[0],
            last_name=user[1],
            username=user[2],
            bio=user[3]
        )

    chats = [
        ("Untitled", None, [1, 2]),
        ("Gryffindor", "Gryffindor house chat", [1, 2]),
        ("Admins", "All admins chat", [3, 4]),
        ("Untitled 2", None, [1, 2]),
    ]

    for chat in chats:
        created_chat = Chat.objects.create(
            title=chat[0],
            description=chat[1],
        )
        chat_users = User.objects.filter(id__in=chat[2])
        created_chat.users.set(chat_users)

    messages = [
        ("Hello, mates!", "2015-02-03T00:00:00", True, 1, 2),
        ("I'm harry123", "2020-02-03T00:00:00", True, 1, 2),
        ("Abla-bla", "2022-03-15T00:00:00", False, 2, 2),
        ("Hi, there!", "2019-12-12T00:00:00", True, 2, 1),
        ("Changes provided", "2019-12-12T00:00:00", False, 3, 3),
        ("Ok", "2020-01-02T00:00:00", True, 4, 3),
        ("Hello", "2022-01-02T00:00:00", False, 4, 3),
    ]

    for message in messages:
        Message.objects.create(
            text=message[0],
            sent=message[1],
            is_delivered=message[2],
            user=User.objects.get(id=message[3]),
            chat=Chat.objects.get(id=message[4])
        )

    assert get_chat_dicts() == [
        {"id": 1, "title": "Untitled", "users": ["harry123", "hermione321"]},
        {"id": 2, "title": "Gryffindor", "users": ["harry123", "hermione321"]},
        {"id": 3, "title": "Admins", "users": ["admin1", "admin2"]},
        {"id": 4, "title": "Untitled 2", "users": ["harry123", "hermione321"]},
    ]
