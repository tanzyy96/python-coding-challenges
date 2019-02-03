import cgpafunctions
import cgpafunctionsTemplate


def main():
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


while __name__ == "__main__":
    # intro
    main()
