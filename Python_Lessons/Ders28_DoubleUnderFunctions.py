class Circle:
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius
    def area(self):
        return self.radius * self.radius * self.pi
    def __repr__(self):
        return f'{__class__.__name__} nesnesi ve yarıçapı {radius}'
    def __len__(self):
        return self.radius * self.radius
circle_2 = Circle(2 )
print(len(circle_2))

