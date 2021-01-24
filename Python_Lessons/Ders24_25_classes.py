class Student:
    school_name = 'X Lisesi'
    number_of_students = 0
    
    def __init__(self,name,age,grades):
        self.name = name
        self.age = age
        self.grades = grades
        Student.number_of_students += 1
    
    def average(self):
        return sum(self.grades) / len(self.grades)

print(Student.number_of_students)

student1 = Student('Furkan', 21, [45,50, 65, 70])

print(Student.number_of_students)