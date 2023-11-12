class Phone:
    def __init__(self, name, last_name, phone) -> None:
        self.name = name
        self.last_name = last_name
        self.phone = phone
    
    def get_info(self):
        print(f'Контакт: {self.name} {self.last_name}, телефон: {self.phone}')

contact = Phone("John", "Snow", "+996707707707")
contact.get_info()