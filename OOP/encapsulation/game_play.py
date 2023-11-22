class Game:
    __level = 0

    def __init__(self, name) -> None:
        self.name = name


    def play(self, hours):
        if hours > 2:
            self.__level += 1

    
    def get_level(self):
        return self.__level
    


game = Game("Raychel")
print(game.get_level())
game.play(5)
game.play(5)
print(game.get_level())

