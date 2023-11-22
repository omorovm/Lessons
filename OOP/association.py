# ================Ассоциация
# Это принцип ООП, в которов два класса связаны друг с другом
# Агрегация - слабая связь
# Композиция - сильная связь

# class Battery:
#     _power =100

#     def charge(self):
#         self._power = 100

# class Iphone():
#     def __init__(self, color: str  = "black") -> None:
#         self.color = color
#         self.batttery =Battery()
#         #  это у нас композиция

# class Nokia:
#     def __init__(self, battery:Battery, color: str = "white") -> None:
#         self.color = color
#         self.batttery =battery

#         #  это агрегация

# iphone = Iphone()
# del iphone

# battery = Battery()
# nokia = Nokia(battery)
# del nokia

class Printer:
    def print_content(self):
        print()

class Document:
    def __init__(self, content) -> None:
        self.printer = Printer(content)