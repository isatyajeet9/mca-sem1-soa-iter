# A9Q5
# Question: Create a class to manage library books. The attributes of the class are book name,
#           author(s) name, ISBN number, number of pages and price. The operations are input
#           details, display details, add books and remove books.
# Name: Satyajeet Nayak
# Appl No: 25C200429

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, name, author, isbn, pages, price):
        self.books.append([name, author, isbn, pages, price])

    def remove_book(self, name):
        for b in self.books:
            if b[0] == name:
                self.books.remove(b)

    def display(self):
        for b in self.books:
            print(b)

obj = Library()
obj.add_book("Python", "Guido", 1111, 300, 450)
obj.add_book("Java", "James Gosling", 2222, 500, 600)

# obj.remove_book("Java")

obj.display()
