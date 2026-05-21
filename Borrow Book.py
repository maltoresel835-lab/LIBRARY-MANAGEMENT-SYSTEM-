# =========================================
# BORROW BOOK CLASS
# =========================================

class BorrowBook:

    def __init__(self, member_name, book_title, borrow_date):

        self.member_name = member_name
        self.book_title = book_title
        self.borrow_date = borrow_date

    # =====================================
    # DISPLAY BORROW INFORMATION
    # =====================================

    def display_borrow_info(self):

        print("\n========== BORROW INFORMATION ==========")
        print("Member Name :", self.member_name)
        print("Book Title  :", self.book_title)
        print("Borrow Date :", self.borrow_date)


# =========================================
# BORROW BOOK FUNCTION
# =========================================

def borrow_book():

    print("\n========== BORROW BOOK ==========")

    member_name = input("Enter Member Name: ")
    book_title = input("Enter Book Title: ")
    borrow_date = input("Enter Borrow Date: ")

    # Create BorrowBook Object
    new_borrow = BorrowBook(
        member_name,
        book_title,
        borrow_date
    )

    print("\nBook Borrowed Successfully!")

    return new_borrow


# =========================================
# MAIN PROGRAM
# =========================================

borrow1 = borrow_book()

# Display Borrow Information
borrow1.display_borrow_info()