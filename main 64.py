#  Exercise 6
#  Write a library class with no of books and books as two instance variable .write a program to create a library from this 
# library class and show how you can print all books add s book
#  and get the number  of books using diffrent methods.
# show that your program doestn't persist the books after the program is stooped!
#  Solution:
# class Library:
#     def __init__(self):
#         self.no_of_books = 0
#         self.books=[]
#     def add_book(self, book):
#         self.books.append(book)
#         self.no_of_books += 1
#     def print_boooks(self):
#         print("Books in library:")
#         for book in self.books:
#             print(book)
#     def get_no_of_books(self):
#         return self.no_of_books
    
class Library:
    def __init__(self):
        self.no_of_books = 0
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        self.no_of_books += 1

    def print_books(self):
        print("Books in library:")
        for book in self.books:
            print(book)

    def get_no_of_books(self):
        return self.no_of