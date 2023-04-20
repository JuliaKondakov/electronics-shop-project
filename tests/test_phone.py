import pytest

from src.item import Item
from src.phone import Phone

@pytest.fixture
def phone1():
    return Phone("iPhone 14", 120000, 5, 2)

@pytest.fixture
def item1():
    return Item("Смартфон", 10000, 20)


def test_phone_init(phone1):
    assert str(phone1) == 'iPhone 14'
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"
    assert phone1.number_of_sim == 2


def test_addition(phone1, item1):
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10


def test_invalid_number_of_sim(phone1):
    with pytest.raises(ValueError):
        phone1.number_of_sim = 0


def test_addition_with_invalid_operand(phone1):
    with pytest.raises(TypeError):
        phone1 + "Invalid operand"
