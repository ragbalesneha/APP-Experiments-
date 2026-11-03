class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"[{self.book_id}] '{self.title}' by {self.author} - Status: {status}"


class Patron:
    def __init__(self, patron_id, name):
        self.patron_id = patron_id
        self.name = name
        self.borrowed_books = []  # List to store Book objects

    def __str__(self):
        return f"Patron [{self.patron_id}]: {self.name} (Books borrowed: {len(self.borrowed_books)})"


class Library:
    def __init__(self):
        self.books = {}     # Dictionary mapping book_id to Book object
        self.patrons = {}   # Dictionary mapping patron_id to Patron object

    def add_book(self, book_id, title, author):
        if book_id in self.books:
            print(f"Book with ID {book_id} already exists.")
        else:
            self.books[book_id] = Book(book_id, title, author)
            print(f"Successfully added book: '{title}'")

    def register_patron(self, patron_id, name):
        if patron_id in self.patrons:
            print(f"Patron with ID {patron_id} already registered.")
        else:
            self.patrons[patron_id] = Patron(patron_id, name)
            print(f"Successfully registered patron: {name}")

    def borrow_book(self, patron_id, book_id):
        if patron_id not in self.patrons:
            print(f"Error: Patron ID {patron_id} not found.")
            return
        if book_id not in self.books:
            print(f"Error: Book ID {book_id} not found.")
            return

        book = self.books[book_id]
        patron = self.patrons[patron_id]

        if book.is_borrowed:
            print(f"Sorry, '{book.title}' is already borrowed.")
        else:
            book.is_borrowed = True
            patron.borrowed_books.append(book)
            print(f"Success! {patron.name} borrowed '{book.title}'.")

    def return_book(self, patron_id, book_id):
        if patron_id not in self.patrons:
            print(f"Error: Patron ID {patron_id} not found.")
            return
        if book_id not in self.books:
            print(f"Error: Book ID {book_id} not found.")
            return

        book = self.books[book_id]
        patron = self.patrons[patron_id]

        if book in patron.borrowed_books:
            book.is_borrowed = False
            patron.borrowed_books.remove(book)
            print(f"Success! {patron.name} returned '{book.title}'.")
        else:
            print(f"Error: {patron.name} did not borrow '{book.title}'.")

    def display_library_status(self):
        print("\n--- Library Catalog ---")
        for book in self.books.values():
            print(book)
        print("\n--- Registered Patrons ---")
        for patron in self.patrons.values():
            print(patron)
        print("-" * 30 + "\n")


# ==================== Demonstration / Test Run ====================
if __name__ == "__main__":
    # Initialize the library system
    my_library = Library()

    # 1. Add new books
    my_library.add_book("B001", "The Palace of Illusions", "Chitra Banerjee Divakaruni")
    my_library.add_book("B002", "Norwegian Wood", "Haruki Murakami")
    my_library.add_book("B003", "Python Programming", "Guido van Rossum")

    # 2. Register patrons
    my_library.register_patron("P001", "Sneha")
    my_library.register_patron("P002", "Rahul")

    # Display initial state
    my_library.display_library_status()

    # 3. Borrow books
    my_library.borrow_book("P001", "B001")  # Sneha borrows 'The Palace of Illusions'
    my_library.borrow_book("P001", "B002")  # Sneha borrows 'Norwegian Wood'
    
    # Try borrowing an already borrowed book
    my_library.borrow_book("P002", "B001")  # Rahul tries to borrow 'The Palace of Illusions'

    # Display state after borrowing
    my_library.display_library_status()

    # 4. Return books
    my_library.return_book("P001", "B001")  # Sneha returns 'The Palace of Illusions'

    # Display final state
    my_library.display_library_status()