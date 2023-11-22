class OS: 
    def __init__(self, version): 
        self.version = version 
class Windows(OS): 
    def copy(self, text): 
        return f'скопирован текст "{text}" горячими клавишами CTRL + C' 
class MacOS(OS): 
    def copy(self, text): 
        return f'скопирован текст "{text}" горячими клавишами COMMAND + C' 
class Linux(OS): 
    def copy(self, text): 
        return f'скопирован текст "{text}" горячими клавишами CTRL + SHIFT + C' 

win = Windows('10') 
mac = MacOS('Big Sur') 
lin = Linux('Ubuntu') 
print(win.copy('Полиморфизм — одна из основных парадигм ООП')) 
print(mac.copy('Полиморфизм - разное поведение одного и того же метода в разных классах')) 
print(lin.copy('На самом деле одинаковым является только имя метода, его исходный код зависит от класса'))