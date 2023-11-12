from abc import ABC, abstractmethod
class Coder(ABC):
    count_code_time = 0
    @abstractmethod
    def get_info(self):
        pass 
    @abstractmethod
    def coding(self, count):
        pass

class Backend(Coder):
    def __init__(self, experience, languages_backend) -> None:
        self.experience = experience
        self.language = languages_backend

    def get_info(self):
        return f"{self.language} разработчик, уровень: {self.experience}, потрачено {self.count_code_time} часов на программирование"

    def coding(self, count):
        self.count_code_time += count


        
class Frontend(Coder):
    def __init__(self, experience, languages_frontend) -> None:
        self.experience = experience
        self.language = languages_frontend

    def get_info(self):
        return f"{self.language} разработчик, уровень: {self.experience}, потрачено {self.count_code_time} часов на программирование"

    def coding(self, count):
        self.count_code_time += count



class Fullstack(Frontend, Backend):
    def __init__(self, experience, languages_frontend) -> None:
        self.experience = experience
        self.language = languages_frontend


a = Backend('Junior', 'Python')
b = Frontend('Middle', 'Javascript')
c = Fullstack("Senior", 'Python and JS')
a.coding(12) 
b.coding(45) 
c.coding(17) 
print(a.get_info()) 
print(b.get_info()) 
print(c.get_info()) 