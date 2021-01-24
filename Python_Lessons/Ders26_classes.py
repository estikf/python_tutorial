class Student:
    school_name = 'X Lisesi'
    number_of_students = 0
    
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades
        Student.number_of_students += 1
    
    def average(self):
        return sum(self.grades) / len(self.grades)
    
    @classmethod
    def display_school_name(cls, name_of_school):
        cls.school.name = name_of_school
    
    @staticmethod
    def statik():
        return f'Sadece bu mesajı gönderiyorum.'

student1 = Student('Furkan', 21, [45,50, 65, 70])
student2 = Student('Mahmut', 21, [98, 41, 95, 80])

print(Student.statik())
print(student1.statik())
print(student2.statik())