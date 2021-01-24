# First Class Functions: Fonksiyonu başka bir değişkene atayabiliriz.

""" Örnek """

def summation(x,y):
    return x+y

result = summation
print(result(1,2))

# Higher Order Functions: Fonksiyonu değişken olarak aldırabiliriz.

""" Örnek """

def summation2(array1, func):
    total = 0
    for x in array1:
        total += func(x)
    return total

def cube(x):
    return x**2

def square(x):
    return x**3

array = [1,2,3,4,5]
print(summation2(array, cube))

# Return Function

""" Örnek """

def say_my_name(name):
    def say_my_salary(salary):
        print(f'İsminiz: {name}, Maaşınız: {salary} TL')
    return say_my_salary

Furkan_emp = say_my_name('Furkan')
Furkan_emp(500)

""" Örnek """

from random import choice

def takimlar(team):
    def msg():
        message = choice(range(19))
        return message
    
    result = f'{msg()}. {team}'
    print(result)

takim = input('Takiminizin ismini giriniz.: ')
takimlar(str(takim))

# Closure kavramı : bir fonksiyonun kendi kapsamında başka bir değişkeni kullanmasıdır.
# İçteki fonksiyonda herhangi bir değişken olmamasına rağmen parent fonksiyondan almaktadır.

def parent(isim):
    the_name = isim
    def isim_göster():
        print(f'İsminiz: {the_name}')
    return isim_göster

Furkan_name = parent('Furkan')
Furkan_name()