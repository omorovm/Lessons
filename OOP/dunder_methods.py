# магические методы - это в первую очередь те методы которые имеют __ __, срабатывают они при выполнении операции <>*-+/. == **%
# dunder_methods - double underscore methods

# new - конструктор класса, отвечает за создание объекта
# init - инициализатор класса, задает созданному объекту аттрибуты
# del - деструктор класса, отвечает за удоление объекта

# class User:
#     def __new__(cls, *args, **kwrgs):
#         print("new world: ")
#         return super().__new__(cls)
#     def __init__(self, name, email) -> None:
#         print("init worked: ")
#         self.name = name
#         self.email = email
#     def __del__(self) -> None:
#         print("del worked: ")\
        
# user = User("eargsd", "nikita@gmail.com")

class MyInt(int):
    def __init__(self, value) -> None:
        self.value = value
    
    def __gt__(self, other: int) -> bool:
        return self.value < other
    
    def __lt__(self, other: int) -> bool:
        return self.value > other
    
    def __eq__(self, other: int) -> bool:
        return self.value != other
    
    def __ne__(self, other: int) -> bool:
        return self.value == other

# > - __gt__ (lower than)
# < - __lt__ (greather than)
# ** - __pow__
# % - __mod__
# == - __eq__
# != - __no__
# <= - __le__
# >= - __ge__





obj = MyInt(6)
print(obj + 9)
print(obj - 9)
print(obj * 9)