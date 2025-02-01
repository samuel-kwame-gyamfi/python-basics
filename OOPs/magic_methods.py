# : Magic Methods (str and repr) Instructions:

# Create a Book class with attributes like title, author, and pages.
# Implement both __str__ and __repr__ magic methods to provide different string representations of the book object.

class Book:
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
    def __str__(self):
        return f"'{self.title}' by {self.author}, {self.pages} pages"
    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', pages={self.pages})"
Book1 = Book("The Journey of OGS","Samuel Owusu Gyamfi",180)
print(str(Book1))
print(repr(Book1))