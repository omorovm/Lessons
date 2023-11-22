class Dad:
    name = "John"
    _last_name = "Snow"
    __age = 40

class Me(Dad):
    name = "Sam"
    __age = 10
    def about_me(self):
        print(f'My name is {self.name} {self._last_name} and I am {self.__age} years old')
    
    def about_my_father(self):
        print(f"My father is {super().name} {super()._last_name}")

me = Me()
me.about_me()
me.about_my_father()