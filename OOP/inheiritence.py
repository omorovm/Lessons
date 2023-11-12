# Наследование - принцип ООПб в котором мы можем унаследовать, переопределить и использовать в дочернемклассе все методы и аттрибуты родительского класса
# object - класс прородитель, в котором хранятся все маг методы
class A:
    h = 5
    def method(self):
        print("method A")

class B(A):
    h = 6
    def Method(self):
        super().method    #ссылается на родительский класс
        print("method B")

# b = B()
# b.method()
# b.h
# print(dir(B))


class Human:
    def __init__(self, name, age,sex):
        self.name = name
        self.age = age
        self.sex = sex
    def get_info(self):
        return f"My name is {self.name}, i'm {self.age} years old."

class Student(Human):
    def __init__(self, name, age, sex, facultet, kurs):
        super().__init__(name, age, sex)
        self.facultet = facultet
        self. kurs = kurs
    
    def get_info(self):
        return super().get_info() + "I'm studying at {self.facultet} on {self.kurs} kurs"

student1 = Student("Nikita", 20, "male", "IT", 3)
# print(student1.get_info())
print(super(student1))

# одиночное наследование
# множественное наследование
# многоуровневое наследование
# иерархическое наследование
# гибридное наследование

list

# __str__ and __repr__ - различия