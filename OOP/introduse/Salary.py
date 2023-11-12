class Salary:
    percent = 8
    def __init__(self, salary, experience) -> None:
        self.salary = salary
        self.experience = experience
    
    def count_percent(self):
        return self.salary * self.percent * self.experience / 100

obj = Salary(1425,13)
print(obj.count_percent()) 