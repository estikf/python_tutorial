x = int(input('Bir sayi giriniz: '))

def faktoriyel(x):
    if x == 0:
        return 1
    elif x < 0:
        return 'Negatif bir sayi girdiniz.'
    else:
        return x * faktoriyel(x-1)
print(faktoriyel(x))