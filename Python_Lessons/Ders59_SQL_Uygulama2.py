import sqlite3

connection = sqlite3.connect('users.db')
cursor = connection.cursor()

#cursor.execute(f"CREATE TABLE users (user TEXT, pass TEXT)")


username = input('Kullanici adi giriniz: ')
password = input('Sifre giriniz: ')

#cursor.execute(f"INSERT INTO users (user, pass) VALUES ('{username}', '{password}')")

cursor.execute(f"SELECT * FROM users WHERE user='{username}' AND pass='{password}'")

if(cursor.fetchone()):
    print('Giriş Basarili')
else:
    print('Giriş Basarisiz')

connection.commit()
connection.close()

""" Sifre kismina 'OR 4>3-- yazarsak şifreyi doğru kabul eder ve SQL Injection yapmış oluruz."""