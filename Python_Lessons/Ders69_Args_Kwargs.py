# *args

""" ÖRNEK 1 """

def print_names(name1, name2, *names):
    print(name1, name2, names)

isimler = ['Ahmet', 'Mehmet', 'Ayşe', 'Fatma', 'Rıza']

print_names(*isimler)

"""ÖRNEK 2"""

def sum_numbers(*numbers):
    total = 0 
    for num in numbers:
        total += num
    return total


print(sum_numbers(1,3))

# **kwargs

def fav_pro(**kwargs):
    for name, program in kwargs.items():
        print(f'İsim: {name} Sayı: {program}')

fav_pro(ahmet='1',rıza='2')
