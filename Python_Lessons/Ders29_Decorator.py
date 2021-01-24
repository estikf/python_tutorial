class Student:
    test = 'Student'
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades
    
    def average(self):
        return sum(self.grades) / len(self.grades)
    @property
    def fullname(self):
        return f'{self.name} {self.age}'

class UniversityStudent(Student):
        test = 'University Student'
        def __init__(self, name, age, grades, university):
            super().__init__(name, age, grades)
            self.university = university

u_student1 = UniversityStudent('Mahmut', 22, [32, 39, 98, 60], 'ITU')
print(u_student1.name)
print(UniversityStudent.test)
print(u_student1.fullname)