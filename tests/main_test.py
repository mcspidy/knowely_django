import pytest

from main import get_all_loyalty_program_names
from db.models import LoyaltyProgram


@pytest.mark.django_db
def test_get_all_loyalty_program_names() -> None:
    loyalty_programs = [("Base level", 5), ("Middle level", 10), ("Gold level", 20)]

    for loyalty_program in loyalty_programs:
        LoyaltyProgram.objects.create(
            name=loyalty_program[0], bonus_percentage=loyalty_program[1]
        )
    
    result = get_all_loyalty_program_names()
    expected = [("Base level", 5), ("Middle level", 10), ("Gold level", 20)]
    
    assert sorted(list(result)) == sorted(expected)
