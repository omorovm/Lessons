class Taxi:
    def __init__(self, name, cost, cost_km):
        self.name = name
        self.cost = cost
        self.cost_km = cost_km
    
    def get_total_cost(self, km):
        return f'Такси {self.name}, стоимость поездки: {self.cost + self.cost_km * km} сом'
    
taxi1 = Taxi('Namba', 45, 15)
taxi2 = Taxi('Yandex', 35, 15)
taxi3 = Taxi('Jorgo', 40, 15)
print(taxi1.get_total_cost(10)) 
print(taxi2.get_total_cost(6)) 
print(taxi3.get_total_cost(14))  