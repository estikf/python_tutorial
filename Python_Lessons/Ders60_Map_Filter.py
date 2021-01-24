# Map ve Filter fonksiyonları gömülü fonksiyonlardır.

# ÖRNEK 1:

def func(x):
    return x**2

list1 = [1, 2, 3, 4, 5]
print(list(map(func, list1)))

# ÖRNEK 2:

list2 = ['ahmet', 'mehmet', 'süleyman', 'furkan', 'kamil']

def buyuk_harf(x):
    return x.upper()
list3 = map(buyuk_harf, list2)
print(list(list3))

""" İkinci sefer print ettirdiğimizde [] çıktısını alırız. """

print(list(list3))

# ÖRNEK 3:

list4 = [1, 2, 3, 4, 5, 6, 7, 8]

print(list(filter(lambda x: x<3, list4)))
