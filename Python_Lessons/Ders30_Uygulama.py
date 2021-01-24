class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
    
    def __str__(self):
        return self.name + ' ' + self.surname + ' ' + str(self.age)

person_1 = Person('furkan', 'estik', 23)

print(person_1.__str__())

class Employee(Person):
    def __init__(self, name, surname, age, salary):
        super().__init__(name, surname, age)
        self.salary = salary
    def __str__(self):
        return super().__str__() + ' ' + str(self.salary)

employee_1 = Employee('furkan', 'estik', 32, 1000)
print(employee_1.salary)