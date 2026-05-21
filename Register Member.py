# =========================================
# MEMBER CLASS
# =========================================

class Member:

    def __init__(self, member_id, name, course, year_level):

        self.member_id = member_id
        self.name = name
        self.course = course
        self.year_level = year_level

    # =====================================
    # DISPLAY MEMBER INFORMATION
    # =====================================

    def display_member_info(self):

        print("\n========== MEMBER INFORMATION ==========")
        print("Member ID   :", self.member_id)
        print("Name        :", self.name)
        print("Course      :", self.course)
        print("Year Level  :", self.year_level)


# =========================================
# REGISTER MEMBER FUNCTION
# =========================================

def register_member():

    print("\n========== REGISTER MEMBER ==========")

    member_id = input("Enter Member ID: ")
    name = input("Enter Member Name: ")
    course = input("Enter Course: ")
    year_level = input("Enter Year Level: ")

    # Create Member Object
    new_member = Member(
        member_id,
        name,
        course,
        year_level
    )

    print("\nMember Registered Successfully!")

    return new_member


# =========================================
# MAIN PROGRAM
# =========================================

member1 = register_member()

# Display Member Information
member1.display_member_info()