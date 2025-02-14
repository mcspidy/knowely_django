import init_django_orm  # noqa: E402
from db.models import Message
import pytest


def get_messages_that_contain_word(word: str) -> list[Message]:
    """
    Receives a word as an argument and returns a list of messages that contain
    the word in their text. Use a case-insensitive containment test.
    """
    return list(Message.objects.filter(text__icontains=word))


messages = get_messages_that_contain_word("hello")
assert sorted([message.text for message in messages]) == sorted(
    ["Hello, mates!", "Hello"]
)
assert get_messages_that_contain_word("olleh") == []
