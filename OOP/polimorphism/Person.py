class Person:
    def __init__(self, name, last_name) -> None:
        self.name = name
        self.last_name = last_name

    def get_info(self):
        return f'Привет, меня зовут {self.name} {self.last_name}'

class Employee(Person):
    def __init__(self, work, status, name, last_name) -> None:
        self.work = work
        self.status = status
        self.name = name
        self.last_name = last_name

    def get_info(self):
        return f'{super().get_info()}, я работаю в компании {self.work} на должности {self.status}'

class Student(Person):
    def __init__(self, university, course, name, last_name) -> None:
        self.university = university
        self.course = course
        self.name = name
        self.last_name = last_name

    def get_info(self):
        return f'{super().get_info()}, я учусь в {self.university} на {self.course} курсе'

def get_human_info(obj):
    print(obj.get_info())

person = Person("Иван", "Петоров")
employee = Employee("Рога и копыта","директор","Иван", "Петоров")
student = Student("КГТУ","3","Иван", "Петоров")

get_human_info(person)
get_human_info(employee)
get_human_info(student)