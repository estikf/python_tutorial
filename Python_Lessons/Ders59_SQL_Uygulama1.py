import sqlite3
connection = sqlite3.connect('friends.db')
cursor = connection.cursor()

# Öncelikle txt dosyamızı read modda açıyoruz ve türkçe karakterleri görmek için encoding='utf-8' yazıyoruz.

with open('friends.txt', 'r', encoding='utf-8') as f:

# for döngüsüyle her bir veri satırını okutuyoruz.    

    for friend in f.readlines():

# list comprehension yöntemiyle verileri ayırtıyoruz.

        friends = [x.strip() for x in friend.split(',')]

# Verileri, veri tabanımıza aktarıyoruz.

        cursor.execute("INSERT INTO friends (first_name, last_name, age) VALUES (?,?,?)", (friends[0], friends[1], friends[2]))


connection.commit()
connection.close()