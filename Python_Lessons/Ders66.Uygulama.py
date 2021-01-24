
# ÖRNEK 1: Listeleri ile çalışacak for loopu kendimiz oluşturalım.

"""numbers = [1,2,3,4,5]
friends = ['ahmet', 'mehmet', 'ayşe']

def my_for_loop(iterable):
    my_iterator = iter(iterable)
    while True:
        try:
            print(next(my_iterator))
        except StopIteration:
            break

my_for_loop(friends)"""

# ÖRNEK 2: 0 ile 10 arasındaki sayıların küplerini göstermeyi Iterator sınıfıyla yapalım.

"""class Iterator:
    
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start <= self.end:
            result = self.start **3
            self.start +=1
            return result
    
        else:
            raise StopIteration
            
cubed = Iterator(0,10)
print(next(cubed))
print(next(cubed))
print(next(cubed))
print(next(cubed))
print(next(cubed))
print(next(cubed))
print(next(cubed))
print(next(cubed))
print(next(cubed))
print(next(cubed))
print(next(cubed))"""

# ÖRNEK 3: 0 ile 10 arasındaki sayıların küplerini göstermeyi Generator Expression yardımıyla yapalım.

"""cubed2 = (x**3 for x in range(0,11))

print(next(cubed2))
print(next(cubed2))
print(next(cubed2))
print(next(cubed2))
print(next(cubed2))
print(next(cubed2))
print(next(cubed2))
print(next(cubed2))
print(next(cubed2))
print(next(cubed2))
print(next(cubed2))"""

# ÖRNEK 3: Belirli bir sayıya kadar Fibonacci rakamlarını yazınız.

"""def fibonacci(limit):
    x = 0 
    y = 1 
    while x<limit:
        yield x
        x, y = y, x+y

f = fibonacci(100)

for x in f:
    print(x)"""

# ÖRNEK 4: Iteration vs Indexing

""" Bu kod daha uzun sürede çalışır."""

friends=['ahmet','mehmet','süleyman','Rıza']
i=0
while i<len(friends):
    v=friends[i]
    print(i,v)
    i +=1

""" Bu kod daha kısa sürede çalışır."""

for i,v in enumerate(friends):
    print(i,v)