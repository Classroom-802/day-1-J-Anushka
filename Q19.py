class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

class Borrower:
    def __init__(self, name, borrower_id):
        self.name = name
        self.borrower_id = borrower_id

class Library(Book, Borrower):
    def borrow_book(self):
        print(f'Borrower {self.name} (ID: {self.borrower_id}) has borrowed "{self.title}" by {self.author} (ISBN: {self.isbn}).')

    def return_book(self):
        print(f'Borrower {self.name} (ID: {self.borrower_id}) has returned "{self.title}" by {self.author} (ISBN: {self.isbn}).')

# Input Book and Borrower details
book_title = input("Enter Book Title: ")
book_author = input("Enter Book Author: ")
book_isbn = int(input("Enter Book ISBN: "))
borrower_name = input("Enter Borrower Name: ")
borrower_id = int(input("Enter Borrower ID: "))

# Create Library object
lib = Library(book_title, book_author, book_isbn)
lib.name = borrower_name
lib.borrower_id = borrower_id

# Input action
action = int(input("Enter Action (1 for Borrow, 2 for Return): "))
if action == 1:
    lib.borrow_book()
elif action == 2:
    lib.return_book()
else:
    print("Invalid action!")
