import csv

class Item:

    """
    Класс для представления товара в магазине.
    """
    pay_rate = 0.8      # атрибут кл.
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
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate

        """
        геттер и сеттер для name, используя @property
        """
    @property
    def name(self):
        return self.__name

    """
    в сеттере name проверять, что длина наименования товара не больше 10 симвовов
    """
    @name.setter
    def name(self, name):
        if len(name) > 10:
            raise ValueError('Имя не должно превышать 10 символов')
        self.__name = name

    """добовляем класс-метод, 
    инициализирующий экземпляры класса Item данными из файла src/items.csv
    """
    @classmethod
    def instantiate_from_csv(cls):
        with open('../src/items.csv', 'r', encoding='cp1251') as f:
            reader = csv.DictReader(f)
            for row in reader:
                name = row['name']
                price = cls.string_to_number(row['price'])
                quantity = int(row['quantity'])
                item = cls(name, price, quantity)
                print(item)
    """
    string_to_number() - статический метод,
    возвращающий число из числа-строки
    """
    @classmethod
    def string_to_number(cls, param):
        if isinstance(param, str):
            return int(param)

    def __repr__(self):
        return f'Item(name={self.__name}, price={self.price}, quantity={self.quantity})'

    def __str__(self):
        return self.__name

    def __add__(self, other):
        return self.quantity + other.quantity


item1 = Item("Смартфон", 10000, 20)

