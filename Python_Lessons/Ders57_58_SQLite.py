# https://docs.python.org/3.7/library/sqlite3.html 

import sqlite3

# Veritabanımızı oluşturuyoruz.

connection = sqlite3.connect('friends.db')
cursor = connection.cursor()

# Veritabanımızda bulunacak tabloları oluşturuyoruz.

"""

cursor.execute("CREATE TABLE friends(first_name TEXT, last_name TEXT, age INTEGER)")


"""

# Veritabanımıza veri ekliyoruz.

"""

cursor.execute("INSERT INTO friends VALUES('Fatma', 'Caliskan', 26)")

"""

# Veri tabanımızdan veri görüntülüyoruz.

"""

cursor.execute("SELECT * FROM friends WHERE first_name = 'Fatma' ")

"""

# Veri tabanımız için kullanıcıdan veri alıyoruz.

"""

first_name = input('Lütfen isminizi giriniz: ')
last_name = input('Lütfen soyisminizi giriniz: ')
age = input('Lütfen yaşınızı giriniz: ')

"""

# Verileri tek seferde de alabiliriz: 

""" 

1. YOL: TUPLE YÖNTEMİ

first_name, last_name, age = input('Lütfen verilerinizi araya virgül koyarak giriniz: ').split(',')

cursor.execute(f"INSERT INTO friends VALUES(?, ?, ?)", (first_name, last_name, age))

"""
"""

2. YOL: DICTIONARY YONTEMI

first_name, last_name, age = input('Lütfen verilerinizi araya virgül koyarak giriniz: ').split(',')

cursor.execute(f"INSERT INTO friends VALUES(:first, :last, :ag)", {'first':first_name,'last':last_name,'ag':age})

"""

# Verileri göstermek için SELECT * FROM komutu kullanılır ve sıralamak için ORDER BY kullanabiliriz.

"""

cursor.execute("SELECT * FROM friends ORDER BY first_name DESC")

"""

# İlk kaç veriyi görüntülemek istiyorsan .fetchmany("sayi") metodunu kullanıyoruz.

"""

print(cursor.fetchmany(3))

"""

# Veri silmek için DELETE komutunu kullanıyoruz.

"""

cursor.execute("DELETE FROM friends WHERE first_name=?", ('Fatma',))

"""

# Veri update etmek için UPDATE komutunu kullanıyoruz.

cursor.execute("UPDATE friends SET first_name=? WHERE first_name=?", ('furkan', 'Durkan'))
cursor.execute("SELECT * FROM friends")
print(cursor.fetchall())

# Veri tabanımıza işlemleri gönderiyoruz.

connection.commit()

# Veri tabanımızı kapatıyoruz.

connection.close()  