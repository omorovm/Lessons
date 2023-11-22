class Person:
    def __init__(self, name, phone_number, card_number) -> None:
        self.name = name
        self._phone_number = phone_number
        self.__card_number = card_number
        self.__validate_name()
        self.__validate_card_number()
        self._validate_phone_number()

    def __validate_name(self):
        if len(self.name) < 2:
            self.name = "John"
            return self.name
        self.name = self.name.title()
        return self.name

    def _validate_phone_number(self):
        if type(self._phone_number) is int:
            if str(self._phone_number).startswith("996"):
                return self._phone_number
        self._phone_number = None
        return self._phone_number

    def __validate_card_number(self):
        if type(self.__card_number) is int:
            if len(str(self.__card_number)) ==  16:
                return self.__card_number
        self.__card_number = None
        return self.__card_number

    @property
    def card_number(self):
        return self.__card_number 

tolik = Person("Tolik", 996557551757, 9999999999999999)
print(tolik.name)
print(tolik._phone_number)
print(tolik.card_number)