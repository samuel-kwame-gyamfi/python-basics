# Class Methods for Counting Instances Instruction:

# Create a class Book with a class variable total_books to count the number of book instances created.
# Implement a class method display_total_books() to display the total number of books created.


class Book:
    total_books = 0
    def __init__(self,title,Author):
        self.title = title
        self.Author = Author
        Book.total_books+=1
    @classmethod
    def display_total_books(cls):
        """Class method to display the total number of book instances created."""
        print(f"Total books created: {cls.total_books}")

book1 = Book("The Journey","Samuel Owusu Gyamfi")

book1.display_total_books()