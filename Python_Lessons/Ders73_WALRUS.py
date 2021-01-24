# ÖZELLİK 1 : WALRUS OPERATÖRÜ (:=) 

"""     WALRUS operatörü (:=); değeri alır , değişkene atar ve return eder.  """
"""     Kodların uzunluğunu kısaltmak için kullanılabilir.                   """

# ÖRNEK 1:

"""mylist = list()

while True:
    entry = input('Bir şehir giriniz: ')
    print('Exit yazarak çıkabilirsiniz.')
    if entry == 'Exit':
        break
    mylist.append(entry)

print(mylist)
"""

"""while (entry := input('Şehir ismini yazarak listeye ekleyebilirisiniz.Exit yazarak çıkabilirsiniz.')) != 'Exit':
    mylist.append(entry)
print(mylist)"""

# ÖZELLİK 2 : Positional Only Argument

""" Normalde positional argümanlarda sıra önemliydi ancak keywordlerle oluşturursak sıra önemli değildir."""

def fullname(name, surname):
    print(name, surname)

fullname('Furkan', 'Estik')
fullname(surname='Ali', name='Sabahattin')
    
