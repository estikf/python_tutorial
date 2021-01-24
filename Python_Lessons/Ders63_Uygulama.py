# 1 - Toplamlarını ve çarpımlarını liste içerisinde gösterin.

list_1 = [14, 12, 26, 32]
list_2 = [4, 5, 2, 1]

print(list(map(lambda x,y: x+y, list_1, list_2)))
print(list(map(lambda x,y: x*y, list_1, list_2)))

# 2 - List comprehension yöntemiyle Fahrenheit fh = [99, 108, 176, 234] derecelerini Celcius derecelerine çevirelim.

fh = [99, 108, 176, 234]
c = [(f-32)*(5/9) for f in fh]
print(c)

# 3 - İsmin uzunluğu 4 harf ve küçük olanlar için yeni bir liste oluşturun.

str_list = ['Mustafa', 'Ahmet', 'Arin', 'Cem', 'Aysegul', 'Hakan']

print(list(filter(lambda x: len(x)<=4, str_list)))

# 4 - List Comprehension vs Map function

list_3 = [5, 7, 10, 12, 13, 15, 17, 21, 22, 53, 52, 53]

print([x+5 for x in list_3])
print(list(map(lambda x: x+5, list_3)))

# 5 - List içindeki en küçük elemanı bulun min ve sort

list_3 = [5, 7, 10, 12, 13, 15, 17, 21, 22, 53, 52, 53]

print(min(list_3))
list_3.sort()
print(list_3[0])

# 6 - En uzun listeyi key kullanarak bulun.

list_1 = [14, 12, 26, 32]
list_2 = [4, 5, 2, 1]
list_3 = [5, 7, 10, 12, 13, 15, 17, 21, 22, 53, 52, 53]


print('En uzun liste: ', max(list_1, list_2, list_3, key=len))

# 7 - 
