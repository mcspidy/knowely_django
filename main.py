# main.py
from django.db.models import Q
import init_django_orm  # noqa: E402
from db.models import User


def get_users_who_sent_messages_starts_with_m_or_a() -> list[User]:
    """
    return a list of users who sent at least one message starting with th
    letter a or m. Use case-insensitive test.
    """
    return User.objects.filter(
        message__text__iregex=r"^(a|m)"
    ).distinct()
