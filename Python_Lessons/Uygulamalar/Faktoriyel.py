n = int(input('Bir sayi giriniz: '))

if type(n) == str:
    raise TypeError('Lütfen bir sayi giriniz.')
else:
    def faktoriyel(n):
        if n == 1 or n == 0:
            return 1
        else:
            return n * faktoriyel(n-1)


print(faktoriyel(n))