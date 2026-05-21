# =========================================
# BOOK CLASS
# =========================================

class Book:

    def __init__(self, book_id, title, author, isbn, publication_year):

        self.book_id = book_id
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_year = publication_year

    # =====================================
    # DISPLAY BOOK INFORMATION
    # =====================================

    def display_book_info(self):

        print("\n========== BOOK INFORMATION ==========")
        print("Book ID          :", self.book_id)
        print("Title            :", self.title)
        print("Author           :", self.author)
        print("ISBN             :", self.isbn)
        print("Publication Year :", self.publication_year)


# =========================================
# ADD BOOK FUNCTION
# =========================================

def add_book():

    print("\n========== ADD BOOK ==========")

    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    isbn = input("Enter ISBN: ")
    publication_year = input("Enter Publication Year: ")

    # Create Book Object
    new_book = Book(
        book_id,
        title,
        author,
        isbn,
        publication_year
    )

    print("\nBook Added Successfully!")

    return new_book


# =========================================
# MAIN PROGRAM
# =========================================

book1 = add_book()

# Display Book Information
book1.display_book_info()