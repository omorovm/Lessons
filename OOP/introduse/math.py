class Math:
    def __init__(self, number) -> None:
        self.number = number
    
    def get_sum(self):
        sum_ = 0
        for i in str(self.number):
            sum_ += int(i)
        return sum_
    def get_factorial(self):
        fact = 1
        for i in range(1,self.number + 1):
            fact *= i
        return fact
    def get_mul_table(self):
        table = "".join([f'{self.number} x {i} = {self.number*i}\n' for i in range(1, 11)])
        return table

a = Math(11)
print(a.get_sum())
print(a.get_factorial())
print(a.get_mul_table())