# zip gömülü fonksiyonu ile listeleri birbirine zip edebiliriz.
# sırasıyla hangi iterable baştaysa onu ilk değişken olarak atar.
# ziplemeyi az sayıdaki elemana göre yapar. 

list1 = [1,2,3,4,5]
list2 = ['a','b','c']

zip1 = list(zip(list1,list2))
zip2 = dict(zip(list1,list2))

print(zip1)
print(zip2)

# zip_longest fonksiyonu ise eleman sayısı fazla olan iterable'a göre ziplemeyi gerçekleştirir.

from itertools import zip_longest

zip3 = list(zip_longest(list1,list2, fillvalue='CITY'))
print(zip3)

# filterfalse fonksiyonu doğru değerleri filtreler yanlışları gösterir.

from itertools import filterfalse

print(list(filterfalse(lambda x: x<=3, list1)))

# dropwhile false olduğu kısımdan itibaren devamını gösterir.

from itertools import dropwhile

list3 = [13, 10, 5, 3, 32, 45, 3, 2, 0]

print(list(dropwhile(lambda x: x>3, list3)))

# accumulate

from itertools import accumulate

print(list(accumulate(list3, max)))