# Полиморфизм - принцип ООП, в котором в разных классах методы называются одинакого, но реализация(функционал) разная (один интерфейс - разный функционал)
# Полиморфизм - множество форм
# a = 1
# a.__add__(4) # тоже самое, что и а + 4


# class Cat:
#     def voice(self):
#         print("meow")
# class Dog:
#     def voice(self):
#         print("gav-gav")

# obj = [Cat(), Dog()]
# for i in obj:
#     i.voise()

# class A:
#     def func():
#         pass

# class B(A):
#     def func():
#         pass

class Square:
    def __init__(self, side) -> None:
        self.side = side
    def area(self):
        return self.side**2
class Circle:
    def __init__(self,radius) -> None:
        self.radius = radius
    def area(self):
        return 3,14*self.radius**2

square = Square()
circle = Circle()