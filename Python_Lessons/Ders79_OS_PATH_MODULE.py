import os.path

adres = r'C:\Users\Furkan\Desktop\Python Dersleri\python_lessons'
adres2 = r'C:\Users\Furkan\Desktop\Python Dersleri'
#basename : Dosya isminin adını yazdırır.

"""print(os.path.basename(adres))"""

#dirname: İstediğimiz dosyanın dosya yolunu gösterir.

""""print(os.path.dirname(adres))"""

#exists : Dosya yolunun olup olmadığını döner.

"""print(os.path.exists(adres))"""

#isdir : Klasörse True dosyasya False döner. 

"""print(os.path.isdir(adres))
print(os.path.isdir(adres2))"""

#isfile : Dosyaysa True klasörse False döner.  

"""print(os.path.isfile(adres))
print(os.path.isfile(adres2))"""

#join: Birden fazla dosya yolunu birleştirebiliriz.

"""print(os.path.join(adres, adres2))"""

#split: Dosya yolunu, dosya ismi ve klasörün bulunduğu bir tuple'a çevirir.

dirname, filename = os.path.split(adres)
print(dirname)
print(filename)
