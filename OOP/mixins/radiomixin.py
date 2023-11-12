class RadioMixin:
    def play_music(self,title):
        print(f"Песня называется {title}")

class Auto(RadioMixin):
    def ride(self):
        print("Riding on a ground")

class Boat(RadioMixin):
    def swim(self):
        print("Floating on water")

class Amphibian(Auto, Boat, RadioMixin):
    pass

obj = Amphibian()
obj1 = Auto()
obj2 = Boat()
obj.play_music("fasddg")
obj1.play_music("asdgfd")
obj2.play_music("Asdgf")