class MyString(str):
    def __init__(self, stroka) -> None:
        self.stroka = stroka
    def __str__(self) -> str:
        return self.stroka
    def append(self, str_):
        self.stroka = self.stroka + str_
        return self.stroka
    def pop(self):
        a = self.stroka[-1:]
        self.stroka = self.stroka[:-1]
        return a
    
example = MyString('String') 
example.append('hello')
print(example) 