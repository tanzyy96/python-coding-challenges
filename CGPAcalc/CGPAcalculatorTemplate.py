
def CGPA_calc():
    """
    To calculate CGPA, we need
    (1) current CGPA,
    (2) total AU for GPA computation so far,
    (3) Number of graded AUs this semester,
    By requesting for an estimated semester GPA, we can calculate the final CGPA at the end of the month.
    """
    pass

def GPA_calc():
    """
    To calculate GPA, we need to find out for each module taken this sem:
    (1) module name (optional)
    (2) module AU
    (3) expected grade
    """
    pass

while __name__ == "__main__":
    #intro
    print("""
-----Welcome to CGPA calculator!------\n
1. CGPA Calculator
2. GPA calculator
3. Exit
    """)
    choice = int(input())

    if choice == 1:
        CGPA_calc()
    elif choice == 2:
        GPA_calc()
    elif choice == 3:
        print("Thanks for using this calculator!")
        exit()
    else:
        print("Please enter a valid option.")
