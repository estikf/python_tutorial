class Book:

    def __init__(self, name, author, read):
        self.name = name
        self.author = author
        self.read = read
        
    def __repr__(self):
        return f'Book: {self.name} | Author: {self.author}'

class Member:

    def __init__(self, name):
        self.name = name
        self.books = []

    def __repr__(self):
        return f'Member: {self.name}'
    
    def read_book(self):
        read_book_list = []
        for book in self.books:
            if book.read:
                read_book_list.append(book)
        return read_book_list

    def add_book(self, name, author):
        book = Book(name, author, False)
        self.books.append(book)
    
    def delete_book(self, name):
        for book in self.books:
            if book.name == name:
                self.books.remove(book)
    
    def save_to_file(self):
        with open(f' {self.name}.txt', 'w', encoding='utf-8') as f:
            f.write(self.name + '\n')
            for book in self.books:
                f.write(f'{book.name}, {book.author}, {str(book.read)}\n')



book1 = Book('1Q84', 'Haruki Murakami', False)
book2 = Book('İnce Memed', 'Yaşar Kemal', True)
book3 = Book('Bir Gün Tek Başına', 'Vedat Türkali', True)

member1 = Member('Furkan')
member1.add_book('Don Kisot', 'Cervantes')
member1.add_book("Osmanlı'yı Anlamak", 'İlber Ortaylı')

member1.save_to_file()




