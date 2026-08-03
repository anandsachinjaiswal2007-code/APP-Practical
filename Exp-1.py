# ================================
# Library Management System using OOP
# ================================

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = False

    def display(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        print(f"{self.book_id:<10}{self.title:<25}{self.author:<20}{status}")


class Patron:
    def __init__(self, patron_id, name):
        self.patron_id = patron_id
        self.name = name
        self.borrowed_books = []

    def display(self):
        print(f"Patron ID : {self.patron_id}")
        print(f"Name      : {self.name}")

        if self.borrowed_books:
            print("Borrowed Books :", ", ".join(self.borrowed_books))
        else:
            print("Borrowed Books : None")


class Library:
    def __init__(self):
        self.books = {}
        self.patrons = {}

    # Add a new book
    def add_book(self, book):
        if book.book_id in self.books:
            print("Book ID already exists!")
        else:
            self.books[book.book_id] = book
            print(f"Book '{book.title}' added successfully.")

    # Register a new patron
    def register_patron(self, patron):
        if patron.patron_id in self.patrons:
            print("Patron ID already exists!")
        else:
            self.patrons[patron.patron_id] = patron
            print(f"Patron '{patron.name}' registered successfully.")

    # Borrow a book
    def borrow_book(self, patron_id, book_id):

        if patron_id not in self.patrons:
            print("Patron not found.")
            return

        if book_id not in self.books:
            print("Book not found.")
            return

        patron = self.patrons[patron_id]
        book = self.books[book_id]

        if book.is_borrowed:
            print(f"'{book.title}' is already borrowed.")
            return

        if len(patron.borrowed_books) >= 3:
            print("Borrow limit reached (Maximum 3 books).")
            return

        book.is_borrowed = True
        patron.borrowed_books.append(book.title)

        print(f"{patron.name} borrowed '{book.title}' successfully.")

    # Return a book
    def return_book(self, patron_id, book_id):

        if patron_id not in self.patrons:
            print("Patron not found.")
            return

        if book_id not in self.books:
            print("Book not found.")
            return

        patron = self.patrons[patron_id]
        book = self.books[book_id]

        if book.title not in patron.borrowed_books:
            print("This book was not borrowed by the patron.")
            return

        book.is_borrowed = False
        patron.borrowed_books.remove(book.title)

        print(f"{patron.name} returned '{book.title}' successfully.")

    # Display all books
    def display_books(self):

        if not self.books:
            print("\nNo books available in the library.")
            return

        print("\n================ Library Books ================")
        print(f"{'Book ID':<10}{'Title':<25}{'Author':<20}{'Status'}")
        print("-" * 65)

        for book in self.books.values():
            book.display()

    # Display all patrons
    def display_patrons(self):

        if not self.patrons:
            print("\nNo patrons registered.")
            return

        print("\n============== Registered Patrons ==============")

        for patron in self.patrons.values():
            patron.display()
            print("-" * 40)


# ================================
# Main Program
# ================================

library = Library()

while True:

    print("\n========== Library Management System ==========")
    print("1. Add Book")
    print("2. Register Patron")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Display Books")
    print("6. Display Patrons")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")

        library.add_book(Book(book_id, title, author))

    elif choice == "2":

        patron_id = input("Enter Patron ID: ")
        name = input("Enter Patron Name: ")

        library.register_patron(Patron(patron_id, name))

    elif choice == "3":

        patron_id = input("Enter Patron ID: ")
        book_id = input("Enter Book ID: ")

        library.borrow_book(patron_id, book_id)

    elif choice == "4":

        patron_id = input("Enter Patron ID: ")
        book_id = input("Enter Book ID: ")

        library.return_book(patron_id, book_id)

    elif choice == "5":

        library.display_books()

    elif choice == "6":

        library.display_patrons()

    elif choice == "7":

        print("\nThank you for using the Library Management System.")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 7.")