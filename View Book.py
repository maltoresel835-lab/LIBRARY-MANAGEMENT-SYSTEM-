# =========================================
# VIEW BOOK CLASS
# =========================================

class ViewBook:

    def __init__(self, book_id, title, author):

        self.book_id = book_id
        self.title = title
        self.author = author

    # =====================================
    # DISPLAY BOOK INFORMATION
    # =====================================

    def display_book_info(self):

        print("\n========== BOOK INFORMATION ==========")
        print("Book ID :", self.book_id)
        print("Title   :", self.title)
        print("