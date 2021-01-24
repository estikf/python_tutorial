# Python'da hatalar sondan başlanarak okunur.
# https://docs.python.org/3/tutorial/errors.html bu linkten hatalar detaylı olarak incelenebilir.
# Kullanıcının bu hatalarla karşılaşmaması için, oluşabilecek hatalara karşı kodlar geliştirmemiz gerekmektedir.


# IndexError, index numarasını aştığı zaman gelir.

"""
List = ['ahmet', 'mehmet']
print(List[2])
"""

# KeyError, olmayan bir keyvalue aratıldığında karşımıza çıkar.

"""
Dict = {'name':'Furkan', 'age' : 'age'}
print(Dict['isim']
"""

# NameError, değişken tanımlanmadığında karşımıza çıkar.

"""
print(Furkan)
"""

# AttributeError, kullandığımız nesneye ait olmayan bir method kullandığımızda karşımıza çıkar.

"""
my_list = ['ahmet', '28']
my_list.append('Süleyman')
print(my_list)
my_list.appen('Mehmet')
"""

# IndentationError, indent olması gereken yerde indent kullanmadıysak karşımıza çıkar.

"""
names = ['Ahmet', 'Furkan', 'Mehmet']
for name in names:
print(name)
"""

# TypeError, string ve integer toplanamayacağından karşımıza çıkar.

"""
print('10' + 10)
"""

# ValueError, stringi ondalıklı sayıya çeviremez ve bu hata karşımıza çıkar.

print(int('100.5'))
