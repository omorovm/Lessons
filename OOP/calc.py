class calc:
    def __init__(self, num1: int, num2: int):
        if (type(num2) or type(num2)) is str:
            raise TypeError("нужны числа, а не строки")
        self.num1 = num1
        self.num2 = num2
        
    def sum(self):
        return self.num1 + self.num2
    
    def subtract(self):
        return self.num1 - self.num2
    
    def div(self):
        try:
            return self.num1 / self.num2
        except:
            print("На ноль делить нельзя")
    def mult(self):
        return self.num1 * self.num2
    
a = calc(5, 0)
print(a.div())
    
