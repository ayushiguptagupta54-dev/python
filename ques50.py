# CREATE A MINI LIBRARY MANAGEMENT SYSTEM USING CLASSES.
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(book, "added succesfully")


    def remove_book(self, book):        
        if book in self.books:
            self.books.remove(book)
            print(book, "removed sucessfully")

        else:
            print("Book not found") 


    def display_books(self):
        print("\nAvailable books:")
        for book in self.books:
            print("-", book) 

lib = Library()

lib.add_book("Python basice")
lib.add_book("DS")
lib.add_book("OS")

lib.display_books()

lib.remove_book("Ds")

lib.display_books()

