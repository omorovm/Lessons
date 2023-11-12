class Math:
    def __init__(self, num):
        self.num = num

    def get_sqrt(self):
        return self.num**0.5


a = Math(5)
print(a.get_sqrt())