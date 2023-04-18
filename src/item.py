import csv


class Item:

    pay_rate = 0.8
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """

        self.quantity = quantity
        self.price = price
        self.total = self.calculate_total_price()
        self.__name = name
        Item.all.append(self)  # сохоняем экземпляры класса в списке

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        :return: Общая стоимость товара.
        """
        self.total = self.price * self.quantity
        return self.total

    def apply_discount(self) -> None:
        """Применяет установленную скидку для конкретного товара."""
        self.price = self.price * self.pay_rate

    @property
    def name(self):
        """геттер название товара"""
        return self.__name

    @name.setter
    def name(self, name):
        """сеттер на название, длинну имени"""
        if len(name) > 10:
            raise ValueError('Имя не должно превышать 10 символов')
        self.__name = name

    @classmethod
    def instantiate_from_csv(cls):
        cls.all = []
        """добовляем класс-метод"""
        with open('../src/items.csv', 'r', encoding='cp1251') as f:
            reader = csv.DictReader(f)
            for row in reader:
                name = row['name']
                price = cls.string_to_number(row['price'])
                quantity = int(row['quantity'])
                item = cls(name, price, quantity)
                print(item)

    @classmethod
    def string_to_number(cls, param):
        """Преобразование из чтроки в число"""
        if isinstance(param, str):
            return int(float(param))

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        elif isinstance(other, Phone):
            return self.quantity + other.quantity
        else:
            return NotImplemented

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}',{self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.__name}"

