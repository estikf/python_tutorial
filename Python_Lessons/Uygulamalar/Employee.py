import datetime
my_date = datetime.date(2020, 1, 17)

class Employee:
    number_of_employees = 0
    raise_amount = 1.04

    def __init__(self, name, lastname, pay):
        self.name = name
        self.lastname = lastname
        self.pay = pay
        Employee.number_of_employees += 1

# email'i init olarak girseydik isimler update edildiğinde email update olmayacaktı.
# ancak property decorator altında girince isimler update olunca email de update olacaktır.
# ayrıca property decorator altındaki fonksiyonlar bir attribute olarak davranacaktır.
# yani bu fonksiyonları çalıştırmak için () yapmamıza gerek kalmayacaktır.

    @property
    def email(self):
        return '{} {}@email.com'.format(self.name,self.lastname)    

    @property
    def fullname(self):
        return '{} {}'.format(self.name, self.lastname)

    def apply_raise(self):
        self.pay = int(self.pay * Employee.apply_amount)

    def __repr__(self):
        return "Employee ('{}', '{}', '{}')".format(self.name,self.lastname,self.pay)
    
    def __str__(self):
        return '{} - {}'.format(self.fullname(),self.email)
    
    def __add__(self,other):
        return self.pay + other.pay
# classmethodlar ile class'ın içindeki değişkenleri değiştirebilir. Bir nevi decorator            
    
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(name, lastname, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False 
        return True

# Üst sınıftan name, lastname ve pay özelliklerini miras almak için super().__init__ kullanılır. 
# Bu şekilde kodları tekrardan yazmak zorunda kalmayız.       

class Developer(Employee):
    def __init__(self, name, lastname, pay, prog_lang):
        super().__init__(name, lastname, pay)
        self.prog_lang = prog_lang 

class Manager(Employee):
    def __init__(self, name, lastname, pay, employees=None):
        super().__init__(name, lastname, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())

dev_1 = Developer('Rıza', 'Kamiloğlu', 6000, 'Java')
dev_2 = Developer('Süleyman', 'Osmanoğlu', 6000, 'Python')
emp_1 = Employee('Test1', 'User1' , 3000)
emp_2 = Employee('Test2', 'User2' , 3500)

mgr1 = Manager('Furkan', 'Estik', 9000, [dev_1])
print(repr(mgr1))
print(emp_1 + emp_2)

# İlk değerin ikinci değerin subclass'ı veya instance'ı olup olmadığını sorgular.
print(issubclass(Developer, Employee))
print(isinstance(emp_1, Developer))
emp_2.name = 'Rıza'
print(emp_2.fullname)