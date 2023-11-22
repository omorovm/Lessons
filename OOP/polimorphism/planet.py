class Planet:
    def __init__(self, orbit) -> None:
        self.orbit = orbit
class Mercury(Planet):
    def get_age(self, earth_age):
        return f'на Меркурии ваш возраст составляет {int(earth_age*365//self.orbit)} лет'

class Venus(Planet):
    def get_age(self, earth_age):
        return f'на Венере ваш возраст составляет {int(earth_age*365/self.orbit*365)} дней'
class Jupiter(Planet):
    def get_age(self, earth_age):
        return f'на Юритере ваш возраст составляет {int(earth_age*365//self.orbit*365*24)} часов'

v = Venus(12)
print(v.get_age(17))

j = Jupiter(88)
print(j.get_age(23))

m = Mercury(225)
print(m.get_age(32))