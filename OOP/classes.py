"==========OOP=============="
# class - шаблон (схема)
# объект, эземпляр, instance - объект по шаблону класса (перенимает все аттрибуты и методы класса)

# аттрибут класса - переменные внутри класса (которые будут присвоены каждому объекту)
# аттрибут экземпляра класса - переменные внутри класса, которые мы принимаем при создании экземпляра (объекта)
# метод - функция внутри класса
# self - ссылка на сам класс
# __intit__ -  метод конструктор(маг, метод), который создает новые аттрибуты внутри класса

a = 4
a = int(4)
int
b = "gfhsdfjh"
b = str("gfhsdfjh")


class Car:
    shifter = "коробка передачи"
    engine = "двигатель"
    speedometer = "спидометр"

    def __init__(self, color, quantity_of_doors) -> None:

        self.color = color
        self.quantity_of_doors = quantity_of_doors


    def move(self):
        print("whruuum")
    
    def start(self):
        print("turn on")
    
    def end(self):
        print("turn off")

car1 = Car("черный", 4)
print(car1.move)
# car2 = Car("белый", 2)
# print(car1.engine)
# car3 = Car("красный", 3)
# print(car1.engine)


class Human:
    legs = 2
    arms = 2
    eyes = 2
    def __init__(self, nation, language, race, gender, hair_color) -> None:
        self.nation = nation
        self.language = language
        self.race = race
        self.gender = gender
        self.hair_color = hair_color
    
    def voice(self):
        print("dyshat")
    
    def breathe(self):
        print("dyshu")
    
    def sleep(self):
        print("z z z z ")

    def get_info(self):
        return f'моя страна'
    
Human