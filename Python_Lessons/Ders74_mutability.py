# string, integer, float ve tuple tipi veriler değiştirilemez.

"""name = 'Furkan'

print(name)
print(id(name))

name = 'Mehmet'

print(name)
print(id(name))

name = 'Süleyman'

print(name)
print(id(name))"""

# ALIAS
# Side effect: Programlama olarak hata olmasa da hafızada aynı yeri tutan elementler 
# ileride yan etki olarak hata çıkarabilir.

"""num = [5,9]

print(num)
print(id(num))

num2 = num

num.append(7)

print(num2)
print(id(num))
print(id(num2))"""

# ÖRNEKLER

# ÖRNEK 1:
# Listeye immutable bir veri tipi (string) nesne id numarası değişmez.

my_list = []

for i in range(3):
    my_list.append('Furki')
    print(my_list)
    print(id(my_list))

# ÖRNEK 1:
# Listeye mmutable bir veri tipi (string) nesne id numarası değişir.

my_list = []

for i in range(3):
    my_list.append(['Furki', 'Yağmur'])
    print(my_list)
    print(id(my_list))