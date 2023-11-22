# абстракция - принцип ООП, в котором создается класс пустышка, где задаются названия аттрибутов и методов, необходим для того чтобы в дочерних классах не забыть их переопределить
from abc import ABC, abstractmethod, abstractproperty
# class A(ABC):
#     @abstractmethod
#     def func(self):
#         pass
#     @abstractproperty
#     def a(self):
#         pass

# class B(A):
#     a = 8

#     def func(self):
#         pass

# b = B()


# class AbstractAnimal(ABC):
#     @abstractmethod
#     def voice(self):
#         pass

#     @abstractproperty
#     def legs(self):
#         pass

#     @abstractmethod
#     def move(self):
#         pass

# class Dog(AbstractAnimal):
#     legs = 4

#     def voice(self):
#         print('Гав')
    
#     def move(self):
#         print("walk")

# # dog = Dog()


# class Bird(AbstractAnimal):
#     legs = 2

#     def voice(self):
#         print('aaaaaaaaaaaaaa')
    
#     def move(self):
#         print("fly")

# bird = Bird()

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractproperty
    def angles(self):
        pass

class Square(Shape):
    angles = 4
    def __init__(self, side) -> None:
        self.side = side

    def calculate_area(self):
        return self.side**2
    
    def calculate_perimeter(self):
        return self.side*4
    
class Triangle(Shape):
    angles = 3
    def __init__(self,side1, side2, side3) -> None:
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def calculate_area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return (s*(s-self.side1)*(s-self.side2)*(s-self.side3))**0.5
    
    def calculate_perimeter(self):
        return self.side1 +self.side2 + self.side3

square = Square(3)
triangle = Triangle(3,3,3)