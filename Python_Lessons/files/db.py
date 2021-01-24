movies_file = 'Movies.csv'

# Ayriyeten fl_add_movie şeklinde fonksiyon tanımlamamızın sebebi verileri dosyaya kaydetmemizdir.
# Ders56 uygulamasındaki add_movie kodu sadece kullanıcıdan gelen verileri almaya yaramaktadır.

def fl_add_movie(name, director):
    with open(movies_file, 'a') as f:
        f.write(f' {name}, {director}, {False}\n')


def fl_get_movies():
    with open(movies_file, 'r') as f2:
        lines = [line.strip().split(',') for line in f2.readlines()]

# list comprehension yöntemiyle kodu kısalttık 
    
    return [{'name': line[0], 'director': line[1], 'watched': line[2]} for line in lines]

def fl_watched_movies(name):
    movies = fl_get_movies()
    for movie in movies:
        if movie['name'] == name:
            movie['watched'] = True
        
    _fl_save_movies(movies)

def _fl_save_movies(movies):
    with open(movies_file, 'w') as f3:
        for movie in movies:
            f3.write(f" {movie['name']}, {movie['director']}, {movie['watched']}\n") 

def fl_delete_movie(name):
    movies = fl_get_movies()
    movies = [movie for movie in movies if movie['name'] != name]
    _fl_save_movies(movies)
