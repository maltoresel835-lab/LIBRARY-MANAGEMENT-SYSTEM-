# =========================================
# RETURN BOOK CLASS
# =========================================

class ReturnBook:

    def __init__(self, member_name, book_title, return_date):

        self.member_name = member_name
        self.book_title = book_title
        self.return_date = return_date

    # =====================================
    # DISPLAY RETURN INFORMATION
    # =====================================

    def display_return_info(self):

        print("\n========== RETURN INFORMATION ==========")
        print("Member Name :", self.member_name)
        print("Book Title  :", self.book_title)
        print("Return Date :", self.return_date)


# =========================================
# RETURN BOOK FUNCTION
# =========================================

def return_book():

    print("\n========== RETURN BOOK ==========")

    member_name = input("Enter Member Name: ")
    book_title = input("Enter Book Title: ")
    return_date = input("Enter Return Date: ")

    # Create ReturnBook Object
    new_return = ReturnBook(
        member_name,
        book_title,
        return_date
    )

    print("\nBook Returned Successfully!")

    return new_return


# =========================================
# MAIN PROGRAM
# =========================================

return1 = return_book()

# Display Return Information
return1.display_return_info()