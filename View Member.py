# =========================================
# VIEW MEMBER CLASS
# =========================================

class ViewMember:

    def __init__(self, member_id, name, course):

        self.member_id = member_id
        self.name = name
        self.course = course

    # =====================================
    # DISPLAY MEMBER INFORMATION
    # =====================================

    def display_member_info(self):

        print("\n========== MEMBER INFORMATION ==========")
        print("Member ID :", self.member_id)
        print("Name      :", self.name)
        print("Course    :", self.course)


# =========================================
# VIEW MEMBER FUNCTION
# =========================================

def view_member():

    print("\n========== VIEW MEMBER ==========")

    # Sample Member List
    member1 = ViewMember("M001", "John Doe", "BSIT")
    member2 = ViewMember("M002", "Maria Santos", "BSCS")
    member3 = ViewMember("M003", "Alex Cruz", "BSEd")

    # Display Members
    member1.display_member_info()
    member2.display_member_info()
    member3.display_member_info()


# =========================================
# MAIN PROGRAM
# =========================================

view_member()