class Library:
    def __init__(self):
        self.nobooks = 0
        self.book = []

    def addBook(self, book):
        self.book.append(book)
        self.nobooks = len(self.book)

    def showInfo(self):
        print(f"The library has {self.nobooks} books. The books are")
        for book in self.book:
            print(book)

l1 = Library()
l1.addBook("Harry Potter1")
l1.addBook("Harry Potter2")
l1.addBook("Harry Potter3")
l1.showInfo()
    
  