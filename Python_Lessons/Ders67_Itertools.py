# count ve islice fonksiyonu:
# count fonksiyonu girilen ilk değeri her adımda ikinci değer kadar artırır.
# islice fonksiyonunda girilen adım ise bu adımları maksimum kaç kere yapacağımızı belirler.

"""
from itertools import count,islice
counter = islice(count(10,2),5)
for i in counter:
    print(i)
"""

# cycle fonksiyonu: Durmadan çalıştırmaya yarar.

"""
from itertools import count,islice
from itertools import cycle
cities = ['Istanbul', 'Ankara', 'Izmir', 'Bursa', 'Çanakkale']
for city in cycle(cities):
    print(city)
"""

# repeat fonksiyonu : Sürekli tekrar eder.

"""
from itertools import islice
from itertools import repeat
print(list(map(pow,range(10),repeat(3))))
"""

# chain fonksiyonu : ('ABC', 'DEF') --> ('A', 'B', 'C', 'D', 'E', 'F')

"""
from itertools import chain
list1 = [5,3,9,8,4,9,2,9,7,0]
list2 = [x**2 for x in range(10)]
list3 = ['Bursa', 'Çanakkale', 'İzmir', 'Edirne']
list4 = list(chain(list1,list2,list3))
print(list4)
"""

# compress fonksiyonu : 

from itertools import compress

"""
list1 = ['X', 'Y','X', 'Y','X', 'Y','X', 'Y','X', 'Y',]
list2 = [1,0,1,0,1,0,1,0,1,0,]
data = compress(list1,list2)
print(list(data))
"""