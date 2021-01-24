# İşlemleri uygularken durdurabileceğimiz veya tekrar çalıştırabileceğimiz fonksiyonlara denir.

"""def odds(limit):
    for odd in range(1, limit+1, 2):
        yield odd

my_odds = odds(15)
print(next(my_odds))
print(next(my_odds))
print(next(my_odds))
"""
import random

while True:
    rastgele_rakam = (x for x in range(0, 10))
    for n in range(10):
        print(next(rastgele_rakam))