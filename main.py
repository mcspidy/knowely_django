# main.py
from django.db.models import F
import init_django_orm  # noqa: E402
from db.models import Message


def get_messages_contain_authors_first_name() -> list[Message]:
    """    
    return a list of messages with text containing their author's first_name.
    """
    return Message.objects.filter(text__icontains=F("user__first_name"))
