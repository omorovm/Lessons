class Person:
    def __init__(self, name = None, last_name = None, age = None, email = None) -> None:
        self.__name = name
        self.__last_name = last_name
        self.__age = age
        self.__email = email
    
    @property
    def name(self):
        return self.__name
    
    @property
    def last_name(self):
        return self.__last_name
    
    @property
    def age(self):
        return self.__age
    
    @property
    def email(self):
        return self.__email
    
    @name.setter
    def name(self, a):
        self.__name = a

    @last_name.setter
    def last_name(self, a):
        self.__last_name = a

    @age.setter
    def age(self, a):
        self.__age =  a

    @email.setter
    def email(self, a):
        self.__email = a

john = Person()
print(john.name) # None
print(john.last_name) # None
print(john.age) # None
print(john.email) # None
john.name = 'John'
john.last_name = 'Snow'
john.age = 30
john.email = 'johnsnow@gmail.com'
print(john.name) # John
print(john.last_name) # Snow
print(john.age) # 30
print(john.email) # johnsnow@gmail.com