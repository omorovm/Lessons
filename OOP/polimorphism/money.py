class Money:
    def __init__(self, country, symbol) -> None:
        self.country = country
        self.symbol = symbol

class Dollar(Money):
    rate = 84.80
    def exchange(self, amount):
        return f'{self.symbol} {amount} равен {self.rate * amount} сомам'
    
class Euro(Money):
    rate = 98.40
    def exchange(self, amount):
        return f'{self.symbol} {amount} равен {self.rate * amount} сомам'

