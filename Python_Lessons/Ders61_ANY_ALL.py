list1 = [1, 2, 3, 4]
list2 = [7, 8, 9]
list3 = [0, 0, 2, 3]
list4 = [True, False]
list5 = [True, 0]
list6 = []

# all fonksiyonu, verilerde 0 varsa False, 0 haricinde sayı mevcutsa True olarak geri döner.
# Verinin içindeki elemanların tamamının True olması gerekmektedir.

"""print(all(list1))
print(all(list2))
print(all(list3))
print(all(list4))
print(all(list5))
print(all(list6))"""

# Dictionary veri tipinde sadece key değerlerine bakılır.

"""dict1 = {}
dict2 = {1: True, 2: False}
dict3 = {0: True, 1: True}

print(all(dict1))
print(all(dict2))
print(all(dict3))"""

# any fonksiyonunda tek bir True eleman olması yeterlidir.

"""print(any(list1))
print(any(list2))
print(any(list3))
print(any(list4))
print(any(list5))
print(any(list6))

print(any(dict1))
print(any(dict2))
print(any(dict3))"""

# ÖRNEK:

friends = ['ayşe', 'ahmet', 'ali' ,'atiye']

print(all(friend[0] == 'a' for friend in friends))
    
