# ----------------------------------------
# Library System using Inheritance + Composition
# ----------------------------------------

class Book:
    """Base class for all books."""

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: '{self.title}' by {self.author}"


class EBook(Book):
    """EBook inherits from Book and adds file size."""

    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size  # in MB

    def __str__(self):
        return f"EBook: '{self.title}' by {self.author} - {self.file_size}MB"


class PrintBook(Book):
    """PrintBook inherits from Book and adds page count."""

    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: '{self.title}' by {self.author} - {self.page_count} pages"


class Library:
    """Demonstrates composition by holding a collection of books."""

    def __init__(self):
        self.books = []  # list of Book/EBook/PrintBook objects

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)

    def list_books(self):
        if not self.books:
            print("The library has no books.")
        else:
            for book in self.books:
                print(book)
