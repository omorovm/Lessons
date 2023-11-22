class Makers:
    student_count = 0
    def __init__(self, name, language, kpi) -> None:
        self.name = name
        self.language = language
        self.kpi = kpi

    @classmethod
    def new_student(cls, name, language, kpi):
        cls.student_count += 1
        return cls(name, language, kpi)

    def get_info(self):
        return f'Student name: {self.name}, Language: {self.language}'

    def set_kpi(self, new_kpi):
        self.kpi = new_kpi
        return self.kpi
    
student1 = Makers.new_student("Vlad", "Python", 0)
student2 = Makers.new_student("Nikita", "JS", 0)
print(student1.set_kpi(89)) 
print(student1.get_info()) 
print(student2.set_kpi(89)) 
print(student2.get_info()) 
print(Makers.student_count)