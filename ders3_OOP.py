## Object Oriented Programming

# Creating a Class and __init__ method

class Human:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        self.is_alive = True
        self.is_hungry = False
    
    def __str__(self):
        return f"{self.name} {self.surname}"
    
    def greetings(self):
        return f"Hello! My name is {self.name} {self.surname}"
    
    def eat(self):
        self.is_hungry = True

class Employee:
    def __init__(self, salary):
        self.salary = salary

    def zam(self):
        self.salary = self.salary * 2

"""human_2 = Human("Süleyman","Yılmaz",10)

print(human_2.is_hungry)
human_2.eat()
print(human_2.is_hungry)"""

# Inheritance

class Turk(Human):
    def __init__(self,name,surname,age,ayran):
        super().__init__(name,surname,age)
        self.ayran = ayran



"""turk_1 = Turk("Furkan","Estik",24,"Var")
print(turk_1.is_hungry)
turk_1.eat()
print(turk_1.greetings())"""

# Multiple Inheritance

class Bursalı(Turk, Employee):
    def __init__(self,name,surname,age,ayran,salary):
        Turk.__init__(self,name,surname,age,ayran)
        Employee.__init__(self,salary)

    def greetings(self):
        return f"Selam, naber?"
    
    def tezahurat(self):
        return "Bursaspor!"

    @staticmethod                   # Class'tan nesne oluşturmadan metoda ulaşmaya yarar.
    def static_hello():
        print("Hello statik method")

    @classmethod                    # Classmethod da staticmethod gibi nesne oluşturmadan çağırmaya yarar. Ancak argument olarak cls almalıdır.
    def class_hello(cls):
        print("Hello class method")

"""Bursalı.static_hello()
Bursalı.class_hello()

bursali_1 = Bursalı("Bursa","Bursalı",24,True,10000)

bursali_1.zam()
print(bursali_1.salary)
bursali_1.zam()
print(bursali_1.salary)"""

# Class Property and Encapsulation

class Fighter:
    def __init__(self, name, level, hp):
        self.__name = name
        self.__level = level
        self.__hp = hp
    
    @property
    def get_name(self):
        return self.__name

    def set_name(self, character_name):
        if type(character_name) != str:
            print("String yazınız.")
        else:
            self.__name = character_name

fighter_1 = Fighter("Legolas",10,100)
#print(fighter_1.__name)

print(fighter_1.get_name)

fighter_1.set_name("Furkan")

print(fighter_1.get_name)
