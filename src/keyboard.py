class LanguageMixin:
    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, value):
        if value not in ('EN', 'RU', 'FR'):
            raise ValueError(f"Unsupported language: {value}")
        self._language = value


class KeyBoard(LanguageMixin):
    def __init__(self, name, price, quantity, language='EN'):
        self.name = name
        self.price = price
        self.quantity = quantity
        self._language = language

    def __str__(self):
        return self.name

    def change_lang(self):
        if self._language == 'EN':
            self._language = 'RU'
        else:
            self._language = 'EN'
        return self
