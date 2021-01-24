"""
#Sayı Bulma oyunu
______________________________________
import random
xnum = random.randint(1, 100)
x = int(input('bir sayi giriniz.'))
while xnum != x:
    if x < xnum:
        print('Büyük bir sayi giriniz.')
        x = int(input())
    else:
        x = int(input())
        print('Küçük bir sayi giriniz.')
print('Tebrikler! Sayiyi buldunuz.')
"""
"""
# dereceyi fahrenheit ve kelvine çevir
______________________________________
celcius = [20, 25, 30, 35]
kelvin = []
fahrenheit = []
# F = C * 9 / 5 + 32
for c in celcius:
    k = c + 273
    kelvin.append(k)
    f = c * 9 // 5 + 32
    fahrenheit.append(f)
    
print(kelvin)
print(fahrenheit)
"""

x = int(input('sayi gir'))
sum = 0
if x < 0:
    print('Negatif bir sayı girdiniz.')
else:
    while x > 0:
        sum += x 
        x = x - 1
    print(sum)

