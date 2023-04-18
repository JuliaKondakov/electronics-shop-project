from src.item import Item


class Phone(Item):
    """Класс Phone наследуется от родительского класса Item"""

    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)
        self._number_of_sim = None
        self.number_of_sim = number_of_sim

    @property
    def number_of_sim(self):
        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value):
        if not isinstance(value, int) or value < 1:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
        self._number_of_sim = value

    def __add__(self, other):
        if isinstance(other, Phone):
            return Phone(
                self.name + other.name,
                self.price + other.price,
                self.quantity + other.quantity,
                self.number_of_sim + other.number_of_sim,
            )
        elif isinstance(other, Item):
            return Item(
                self.name + other.name,
                self.price + other.price,
                self.quantity + other.quantity,
            )
        else:
            raise TypeError("Unsupported operand types")

    def __repr__(self):
        return f"Phone('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

