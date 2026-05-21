# =========================================
# VIEW LOAN CLASS
# =========================================

class ViewLoan:

    def __init__(self, loan_id, member_name, book_title):

        self.loan_id = loan_id
        self.member_name = member_name
        self.book_title = book_title

    # =====================================
    # DISPLAY LOAN INFORMATION
    # =====================================

    def display_loan_info(self):

        print("\n========== LOAN INFORMATION ==========")
        print("Loan ID     :", self.loan_id)
        print("Member Name :", self.member_name)
        print("Book Title  :", self.book_title)


# =========================================
# VIEW LOAN FUNCTION
# =========================================

def view_loan():

    print("\n========== VIEW LOAN ==========")

    # Sample Loan List
    loan1 = ViewLoan("L001", "John Doe", "Python Programming")
    loan2 = ViewLoan("L002", "Maria Santos", "Data Structures")
    loan3 = ViewLoan("L003", "Alex Cruz", "Database System")

    # Display Loans
    loan1.display_loan_info()
    loan2.display_loan_info()
    loan3.display_loan_info()


# =========================================
# MAIN PROGRAM
# =========================================

view_loan()