from files import db

user_options = """
Film Yönetim Sistemi:
- eklemek için 1
- listelemek için 2
- düzenlemek için 3 
- filmi silmek için 4
- çıkış yapmak için 0
"""

def main():
    user_input = input(user_options)
    while user_input != '0':
        if user_input == '1':
            add_movie()
        elif user_input == '2':
            list_movies()
        elif user_input == '3':
            watch_movie()
        elif user_input == '4':
            delete_movie()
        else: 
            print(f' {user_input} Bilinmeyen komut')
        
        user_input = input(user_options)

def add_movie():
    name = input('Lütfen filmin adını giriniz: ')
    director = input('Lütfen yönetmenin adını giriniz: ')

    db.fl_add_movie(name, director)

def list_movies():
    movies = db.fl_get_movies()
    for movie in movies:
        print(f"Film: {movie['name']}, Yönetmen: {movie['director']}, İzlenme: {movie['watched']}")

def watch_movie():
    name = (input('İzlediğiniz filmin ismini giriniz: '))
    db.fl_watched_movies(name)

def delete_movie():
    name = (input('Silmek istediğiniz filmin ismini giriniz: '))
    db.fl_delete_movie(name)

main()