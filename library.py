class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True 

class Patron:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []  

class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self, book):
        self.books.append(book)  

    def register_patron(self, patron):
        self.patrons.append(patron)  

    def borrow_book(self, patron, book):
        if book.available:
            book.available = False
            patron.borrowed_books.append(book)  
            print(f"{patron.name} successfully borrowed '{book.title}'.")
        else:
            print(f"Sorry, '{book.title}' is currently unavailable.")

    def return_book(self, patron, book):
        if book in patron.borrowed_books:
            book.available = True
            patron.borrowed_books.remove(book)  
            print(f"{patron.name} successfully returned '{book.title}'.")


my_library = Library()


book1 = Book("The Hobbit", "J.R.R. Tolkien")
alice = Patron("Alice")


my_library.add_book(book1)
my_library.register_patron(alice)


my_library.borrow_book(alice, book1)
my_library.return_book(alice, book1)