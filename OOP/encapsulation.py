# # Инкапсуляция
# # Ограничение доступа к методам и аттрибутам (сокрытие данных)
# # Сбор всех методов и аттрибутов в одну капсулу (класс)

# # 3 модификации доступа
# # public - публичный
# # protected - защищенный  
# # private - приватный

# class A:
#     public = "публичный"
#     _protected = "защищенный"
#     __private = "приватный"

#     def public_func(self):
#         pass

#     def _protected_func(self):
#         pass

#     def __private_func(self):
#         pass

# a = A()
# a.public
# print(a._protected) # мы не должны обращатся к защищенному аттрибуту или методу через объект (на уровне соглашения)
# # print(a.__private)  к приватному аттрибуду я немогу обратится через объект и дочерних классов
# # _<насзвание класса>__<название аттрибута(метода)> (так нельзя на уровне соглашения)


# class B(A):
#     def func(self):
#         self.public
#         # self.__private_func()

# b = B()
# b.func()
# print(b._A__private) # так нельзя на уровне соглашения

# class Person:
#     name = "Nikita"
#     __last_name = "Grebnev"

#     def get_last_name(self):
#         return self.__last_name
    
#     def set_last_name(self, new_last_name):
#         self.__last_name = new_last_name

# human = Person()
# human.set_last_name("Zhoroev")
# print(human.get_last_name())


# class Game:
#     __level = 0

#     def get_level(self):
#         return self.__level
    
#     def set_level(self, num):
#         self.__level = num
    
#     @property # превращает метод в аттрибут
#     def level(self):
#         return self.__level
    
#     @level.getter

#     @level.setter # позволяет изменить аттрибут
#     def level(self,n):
#         self.__level = n

# game = Game()

# print(game.get_level())
# game.set_level(5)
# print(game.get_level())
# game._Game__level += 5
# print(game._Game__level)

# print(game.level)
# game.level = 7
# print(game.level)

# class Human:
#     def __init__(self, name, age, last_name) -> None:
#         self._name = name
#         self.__age = age
#         self.last_name = last_name

#     @property
#     def age(self):
#         return self.__age
    
#     @age.setter # позволяет изменить аттрибут
#     def age(self,new_age):
#         self.__age = new_age

# game = Human('watrestr', 1234, 'fagfdsf')
# print(game.age)
# game.age = 7
# print(game.age)

# getter - переопределяет маг. метод __getattribute__
# setter - переопределяет маг. метод __setattr__
# deleter - переопределяет маг. метод __delattr__

# class Human:
#     def __init__(self, name) -> None:
#         self.__name = name

#     @property
#     def name(self):
#         return self.__name
    
#     @name.deleter # срабатывает когда пишем оператор "del"
#     def name(self):
#         del self.__name

# human = Human("name")
# del human.name
# print(human.name)

class Temperature:
    __default_temp = 20
    def __init__(self, target_temp) -> None:
        self.__target_temp = target_temp
        self.get_count()
    def add_temp(self):
        self.__target_temp += 1
        if self.__target_temp == self.__default_temp:
            print("вы достигли необходимой температуры")
    def minus_temp(self):
        self.__target_temp -= 1
        if self.__target_temp == self.__default_temp:
            print("вы достигли необходимой температуры")
    def get_temp(self):
        return self.__default_temp
    
    def get_count(self):
        self.count = abs(self.__default_temp - self.__target_temp)
        while self.__default_temp == self.__target_temp:
            if self.__default_temp > self.__target_temp:
                self.minus_temp()
            else:
                self.add_temp()