# Миксины - классы расширители, от которых мы наследеумся, от миксинов мы не создаем объект

class FlyMIxin:
    def fly(self):
        print("я могу летать")
    
class WalkMixin:
    def walk(self):
        print("я могу ходить")

class SwimMixin:
    def swim(self):
        print("я могу плавать")

class Human(FlyMIxin, WalkMixin):
    name = "человек"

    def talk():
        print("я умею говорить")



human = Human()
human.walk()

