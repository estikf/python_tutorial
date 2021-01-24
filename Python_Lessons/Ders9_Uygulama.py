""" 
my_list = ['a' , 'b' , 'c' , 'd' , 'e' , 'f']
my_list.remove('a')
print(my_list)
del my_list[2]
print(my_list)
"""


"""
numbers = [1 , 123 , 3434 ,34 , 23 , 54 , 56 , 8 , 12 , 45 , 65 , 36]
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
"""


"""
dersler = [['matematik' , 'fizik'] , ['kimya' , 'biyoloji'] , ['ahmet' , 'mehmet']]
dersler2 = []
for ders in dersler:
    dersler2.append(ders[-1])
print(dersler2)
"""


"""
squares = []
for num in range(1,11):
    squares.append(num**2)
print(squares)
"""


numbers = [num**2 for num in range(1,12)]
print(numbers)
