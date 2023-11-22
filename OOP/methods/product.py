class Product:
    base_price = 20000

    def __init__(self, model, year, color) -> None:
        self.model = model
        self.year = year
        self.color = color
        
    
    def has_garantiya(self, year):
        if year - self.year  > 2:
            return 'Ваша гарантия истекла'
        return 'Гарантия действительна'

    @classmethod
    def change_price(cls, rate):
        cls.base_price += int(cls.base_price * rate / 100)


obj = Product('A218', 2008, 'red') 
obj.change_price(2) 
print(obj.has_garantiya(2010)) 
print(obj.base_price) 