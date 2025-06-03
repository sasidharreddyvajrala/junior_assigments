class book:
    def __init__(self, author, title):
        self.author  = author
        self. title = title
        self.is_available = True

    def __str__(self):
        status = 'Available' if self.is_available else "Not Available"
        return f'{self.title} by {self.author} is {status}'

class Library:
    def __init__(self,name):
        self.name = name
        self.books = []

    def add_books(self, book):
        self.books.append(book)
    def show_books(self):
        for book in self.books:
            print(book)
    def borrow(self,title):
        for book in self.books:
            if book.title.lower() == title.lower() and book.is_available:
                book.is_available = False
                print(f" your borrowed {book.title}")
                return
        print("Book not found or not available")
    def return_book(self,title):
        for book in self.books:
            if book.title.lower() == title.lower() and not book.is_available:
                book.is_available = True 
                print(f'{book.title} returned')
                return 
        print("book already returned")

def main():
    Library1 = Library("school library")
    Library1.add_books(book("Rick Riordan","Percy Jackson"))
    Library1.add_books(book("J. K. Rowling","Harry Potter"))

    Library1.show_books()

    Library1.borrow("Percy Jackson")
    Library1.show_books()

if __name__ == '__main__':
    main()