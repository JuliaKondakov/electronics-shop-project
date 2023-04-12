"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src import item
from src.item import Item


@pytest.fixture
def item1():
    return Item("Смартфон", 10000, 20)


def test_calculate_total_price(item1):
    # проверяем, что метод calculate_total_price() возвращает правильную общую стоимость
    item1 = Item("Телефон", 10000, 20)
    assert item1.calculate_total_price() == 200000


def test_apply_discount(item1):
    # экземпляр класса item, проверяем скидку и что цена уменьшилась на 20%
    item = Item("Телефон", 10000.0, 2)
    item.apply_discount()
    assert item.price == 8000.0


def test_name(item1):
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'
    item.name = 'СуперСмартфон'
    assert item.name == 'СуперСмартфон'


def test_string_to_number(item1):
    # Проверяем, что метод возвращает корректные значения для строк с числами
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


"""Homwork 3"""


def test_repr(item1):
    assert repr(item1) == "Item('Смартфон',10000, 20)"


def test_str(item1):
    assert str(item1) == 'Смартфон'

"""Homework-4"""

#from src.phone import Phone


#def test__str__():
 #   phone = Phone("iPhone 14", 120000, 5, 2)
  #  assert str(phone) == "iPhone 14"


#def test__repr__():
   # phone = Phone("iPhone 14", 120000, 5, 2)
 #   assert repr(phone) == "Phone('iPhone 14', 120000, 5, 2)"


#def test_add_item():
 #   phone = Phone("iPhone 14", 120000, 5, 2)
  #  item = Item("Смартфон", 10000, 20)
   # assert (phone + item) == 25

