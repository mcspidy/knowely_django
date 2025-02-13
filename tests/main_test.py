import pytest

from main import get_clients_with_i_and_o
from db.models import Customer

@pytest.mark.django_db
def test_get_clients_with_i_and_o():
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

    for customer in customers:
        Customer.objects.create(
            first_name=customer[0], last_name=customer[1],
            phone_number=customer[2]
        )

    expected_result = get_clients_with_i_and_o()
    assert expected_result.count() == 9
