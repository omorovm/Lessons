# существует 3 вида методов
# instance method - обычные методы, которые первым аргументом принимают self(ссылка на объект), нужны они для работы с аттрибутами объекта
# class method -  это методы класса, которые принимают первым аргументом cls(ссылку на класс), нужны для изменения аттрибутов и создания объектов
# static method - просто функции внутри класса, которые нивзаимодействуют ни с классом, ни с объектом, они находятся внутри класса лишь для использования внутри класса, чтобы создать ствтичный метод его нужно задекорировать staticmethod

# class A:
#     def instance_method(self):
#         print('метод объекта')
#         print('первый аргумент {self}')
    
# obj = A()
# obj.instance_method() # если вызываем у объекта, то self передается автоматически
# A.instance_method(obj) # если вызываем у класса, то self нужно передать объект этого класса

# class B:
#     @classmethod
#     def class_method(cls):
#         print('метод класса')
#         print(f'первый аргумент {cls}')

# obj = B()
# obj.class_method()
# B.class_method()
# неважно откуда вызываем класс метод, первым аргументом всегда прилетает ссылка на класс


class Iphone15:
    def __init__(self, name, cost) -> None:
        self.name = name
        self.cost = cost

    @classmethod
    def change_cost(cls,new_cost):
        cls.cost = new_cost
        print(cls.cost)
    
    @staticmethod
    def som_to_dollars(money):
        dollars = money/89.140
        print(dollars)
        return dollars

iphon = Iphone15("pro max", 110000)
print(iphon.cost)
iphon.change_cost(456)
print(iphon.cost)
iphon.som_to_dollars(110000)