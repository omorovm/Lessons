class SmartPhones:
    def __init__(self, name, color, memory, battery = 0):
        self.name = name
        self.color = color
        self.memory = memory
        self.battery = int(battery)

    def __str__(self) -> str:
        return f"{self.name} {self.memory}"
    
    def charge(self, num):
        pass
        self.battery += num
    

class Iphone(SmartPhones):
    def __init__(self, name, color, memory, ios):
        super().__init__(name, color, memory)
        self.ios = ios
    def send_imessage(self, message):
        pass
        return f"sending {message} from {self.name} {self.memory}"

class Samsung(SmartPhones):
    def __init__(self, name, color, memory, android):
        super().__init__(name, color, memory)
        self.android = android
    def show_time(self):
        import datetime
        return datetime.datetime.now().time()

phone = SmartPhones('generic', 'blue', '128GB', "0") 
print(phone)
print(phone.battery)
phone.charge(20) 
print(phone.battery) 
iphone7 = Iphone('Iphone 7', 'gold', '128gb', '12.1.3') 
print(iphone7)
print(iphone7.send_imessage('hello'))
samsung21 = Samsung('Samsung A21', 'black', '256gb', 'Oreo') 
print(samsung21.show_time()) 