class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    
    def display(self):
        return f'name:{self.name}, age:{self.age}'

class Student(Person):
    def __init__(self, name, age, faculty) -> None:
        super().__init__(name, age)
        self.faculty = faculty
    
    def display(self):
        print(super().display())
    
    def display_student(self):
        print(super().display()+f', faculty:{self.faculty}')
    
obj_student = Student('Rick', '21', '4123r24')
obj_student.display() 
obj_student.display_student() 