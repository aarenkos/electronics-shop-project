"""Здесь надо написать тесты с использованием pytest для модуля item."""
import os

from src.item import Item, InstantiateCSVError
import pytest

from src.phone import Phone

path = os.path.join("../src/", "items.csv")

def test_calculate_total_price():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    assert Item.calculate_total_price(item1) == 200000
    assert Item.calculate_total_price(item2) == 100000


def test_apply_discount():
    item1 = Item("Смартфон", 10000, 20)
    Item.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 8000.0
    item2 = Item("Ноутбук", 20000, 5)
    assert item2.price == 20000


def test_name():
    item = Item('Смартфон', 10000, 5)
    item.name = "Кабель"
    assert item.name == "Кабель"
    with pytest.raises(Exception):
        item.name = "Супер_Телефон"



def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_repr():
    item3 = Item("PS5", 30000, 6)
    assert repr(item3) == "Item('PS5', 30000, 6)"


def test_str():
    item3 = Item("PS5", 30000, 6)
    assert str(item3) == "PS5"


def test__add__():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    item1 = Item("Смартфон", 10000, 20)
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10
    assert phone1 + 10 == ValueError

def test_instantiate_from_csv():
    # Item.instantiate_from_csv()
    # assert len(Item.all) == 5
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv(path="нет такого файла")

    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv(path=r"../src/items.csv")


