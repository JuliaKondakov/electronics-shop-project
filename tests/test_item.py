"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src import item
from src.item import Item


@pytest.fixture
def item1():
    return Item("Смартфон", 10000, 20)


def test_calculate_total_price():
    # проверяем, что метод calculate_total_price() возвращает правильную общую стоимость
    item1 = Item("Телефон", 10000, 20)
    assert item1.calculate_total_price() == 200000


def test_apply_discount():
    # экземпляр класса item, проверяем скидку и что цена уменьшилась на 20%
    item = Item("Телефон", 10000.0, 2)
    item.apply_discount()
    assert item.price == 8000.0


def test_name():
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'
    item.name = 'СуперСмартфон'
    assert item.name == 'СуперСмартфон'


def test_string_to_number():
    # Проверяем, что метод возвращает корректные значения для строк с числами
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5


def test_repr():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == 'Item(name=Смартфон, price=10000, quantity=20)'


def test_str():
    item1 = Item("Смартфон", 10000, 20)
    assert str(item1) == 'Смартфон'