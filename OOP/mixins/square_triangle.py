class Square:
    def __init__(self, side) -> None:
        self.side = side
    
    def get_area(self):
        return self.side**2

class Triangle:
    def __init__(self, height, base) -> None:
        self.height = height
        self.base = base
    
    def get_area(self):
        return int(self.height * self.base / 2)

class Pyramid(Triangle, Square):
    def __init__(self, height, base):
        super().__init__(height, base)

    def get_volume(self):
        return int(1 / 3 * self.base**2 * self.height)
    
obj = Pyramid(3,4)
print(obj.get_volume())