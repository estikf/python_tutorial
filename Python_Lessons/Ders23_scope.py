class car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    def brandmodel(self):
        return f'Araç markanız : {self.brand} ve aracınızın modeli : {self.year}'

car1 = car('BMW', 'i5', 2012)
car2 = car('Mitsubishi', 'L300', 1994)

print(car1.brandmodel())
