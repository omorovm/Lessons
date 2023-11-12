class ExtensionMixin:
    def add_extension(self, add):
        self.extensions += [add]
        return f'Добавлено новое расширение {add} для игры {self.name}.'
    def remove_extension(self, rem):
        if rem not in self.extensions:
            return "Такого расширения нет в списке."
        self.extensions.remove(rem)
        return f'{rem} был отключен от {self.name}'

class Game(ExtensionMixin):

    def __init__(self, type, name, extensions = []) -> None:
        self.type = type
        self.name = name
        self.extensions = extensions

    def get_description(self, disc):
        return self.name + " это " + disc
    def get_extensions(self):
        if len(self.extensions) == 0:
            return 'Нет подключенных расширений'
        return ' '.join(self.extensions)

game = Game('CS_GO', 'Minencraft') 
print(game.remove_extension('Multiverse-Core')) 