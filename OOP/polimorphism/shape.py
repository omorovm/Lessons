from abc import ABC, abstractmethod
import math
class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass

class Triangle(Shape):
    def __init__(self, base, height) -> None:
        self.base = base
        self.heigh = height

    def get_area(self):
        return self.base * self.height / 2
    
class Square(Shape):
    def __init__(self, length) -> None:
        self.length = length
        

    def get_area(self):
        return self.length**2
    
class Circle(Shape):
    def __init__(self, radius) -> None:
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius**2

triangle = Triangle(4,5)
square = Square(4)
circle = Circle(5)
print(triangle.get_area()) 
print(square.get_area()) 
print(circle.get_area()) 
    