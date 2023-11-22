class Game:
    __level = 0

    def __init__(self, name) -> None:
        self.name = name
        self.validate_name()

    @property
    def level(self):
        return self.__level
    
    def set_level(self, a):
        if self.name == 'Tolik':
            self.__level = a
            return self.level
        print(f"{self.name} ты не Tolik!")
    
    def validate_name(self):
        self.name = self.name.title()
        return self.name
    


game = Game("Raychel")
game.set_level(5)
print(game._Game__level)

game = Game("TOlik")
game.set_level(5)
print(game._Game__level)