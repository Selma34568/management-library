from classes.book import Book
from classes.patron import Patron
from classes.librarian import Librarian
from classes.library import Library

library = Library("City Library")

book1 = Book("1984", "George Orwell", "1234567890")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "1234567891")

librarian = Librarian("John Doe", "L001")

patron1 = Patron("Alice Smith", "P001")
patron2 = Patron("Bob Johnson", "P002")

librarian.add_book(library, book1)
librarian.add_book(library, book2)

librarian.add_patron(library, patron1)
librarian.add_patron(library, patron2)

patron1.borrow_book(book1)
book1.available = False

print("Books in the library:")
print(library.list_books())

print("\nPatrons in the library:")
print(library.list_patrons())

patron1.return_book(book1)
book1.available = True

print("\nBooks in the library after returning a book:")
print(library.list_books())

