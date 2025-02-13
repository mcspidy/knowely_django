import pytest

from main import get_customers_with_no_bonuses
from db.models import LoyaltyProgram, Customer, LoyaltyProgramParticipant

@pytest.mark.django_db
def test_get_customers_with_no_bonuses():
    loyalty_programs = [
        ("Base level", 5),
        ("Middle level", 10),
        ("Gold level", 20)
    ]

    for name, bonus_percentage in loyalty_programs:
        LoyaltyProgram.objects.create(
            name=name,
            bonus_percentage=bonus_percentage
        )

    customers = [
        ("Ivan", "Ivanov", "380666666666"),
        ("Alina", "Koval", "380999999999"),
        ("Mariia", "Marichna", "380666752638"),
        ("Alona", "Burga", "380666728490"),
        ("Dariia", "Kalinina", "380667287392"),
        ("Sasha", "Alekseev", "380634393939"),
        ("Lena", "Bondar", "380636535353"),
        ("Ivan", "Hryshko", "380505555555"),
        ("Oleksii", "Ivanov", "380668966666"),
        ("Ivan", "Litvin", "380666602966"),
        ("Vadim", "Kuhar", "380766666666"),
        ("Eduard", "Kanaryan", "380666690906"),
        ("Maksim", "Kravchenko", "380669866666"),
        ("Eleonora", "Ivanova", "380666686666"),
        ("Ivanna", "Kukushkina", "38066666666"),
    ]

    for first_name, last_name, phone_number in customers:
        Customer.objects.create(
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number
        )

    loyalty_program_participants = [
        (1, 1, "1970-01-02", 3, 12000),
        (2, 1, "2012-09-09", 100, 100),
        (3, 1, "2022-01-01", 1000, 1001),
        (4, 1, "2021-09-01", 2000, 2000),
        (5, 1, "2021-12-28", 0, 0),      # Customer with zero active bonuses
        (6, 1, "2022-04-28", 12, 12),
        (7, 1, "2022-02-02", 0, 100),    # Customer with zero active bonuses
        (8, 1, "2022-02-09", 2000, 2000),
        (9, 1, "2019-02-09", 90, 90),
        (10, 2, "2019-02-09", 90, 90),
        (11, 2, "2019-05-09", 1000, 1090),
        (12, 2, "2022-05-09", 100, 100),
        (13, 2, "2022-06-09", 1005, 1006),
        (14, 2, "2022-06-09", 10059, 10059),
        (15, 2, "2021-11-09", 100, 200),
    ]

    for participant in loyalty_program_participants:
        LoyaltyProgramParticipant.objects.create(
            customer_id=participant[0],
            loyalty_program_id=participant[1],
            last_activity=participant[2],
            active_bonuses=participant[3],
            sum_of_spent_money=participant[4],
        )

    # Expected phone numbers of customers with zero active bonuses
    expected = [
        {"customer__phone_number": "380667287392"},  # Customer ID 5
        {"customer__phone_number": "380636535353"},  # Customer ID 7
    ]

    result = get_customers_with_no_bonuses()

    assert sorted(list(result), key=lambda x: x["customer__phone_number"]) == \
           sorted(expected, key=lambda x: x["customer__phone_number"])
