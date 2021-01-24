# Örnek 1 

"""
class Human:
    def __init__(self):
        self.friends = []
    
    def add_friends(self, friend):
        
        # Burada hatalı bir kod yazdığımızda karşımıza hatanın ne olduğunu belirtmek için not bırakabiliriz.
        
        raise NotImplementedError('Arkadas Eklenemedi')

Human1 = Human()
Human1.add_friends('Ahmet')
print(Human1.friends)
Human1.add_friends('Ayşe')
print(Human1.friends)
"""

# Örnek 2

# Development kısmında developerların anlaması için kendimiz hata kodları geliştirebiliriz.

class MyCustomError(TypeError):
    
    def __init__(self, message, code):
        self.message = message
        self.code = code
        super().__init__(f'{message}, Hata kodu: {code}')

friends = ['Ahmet', 'Ayşe']

def select_best_friends(friend):
    if type(friend) is not str:
        raise MyCustomError('Arkadas ismi str olmalidir.', 100)
    if friend not in friends:
        raise ValueError(f'{friend} arkadas listesinde değildir')
    print(f'En iyi arkadasiniz: {friend}')

select_best_friends(123)
