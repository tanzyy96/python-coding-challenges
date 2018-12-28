#CGPA Calculator
import time
#variables

ptOne = False
ptTwo = False
ptThree = False

def calcGPA():
    moduleNo = int(input("How many modules do you have this semester?"))
    moduleDict = {}
    noOfAU = 0
    gradesDict = {'A+':5.0,
                  'A' :5.0,
                  'A-':4.5,
                  'B+':4.0,
                  'B' :3.5,
                  'B-':3.0,
                  'C+':2.5,
                  'C' :2.0,
                  'D+':1.5,
                  'D' :1.0,
                  'F' :0.0}
    for modules in range(moduleNo):
        moduleName = input("Name of module:")
        moduleGrade = input("Grade:")
        if moduleGrade not in gradesDict.keys():
            print("Error. Invalid Grade.")
            return
        moduleDict[moduleName] = moduleGrade
        noOfAU += int(input("No of AU: "))
    for modName, modGrade in moduleDict.items():
        print("%20s %5s" %(modName, modGrade))

    #calculate GPA
    gpa = 0.0
    for moduleName in moduleDict:
        gpa += gradesDict[moduleDict[moduleName]]
    gpa = gpa/moduleNo
    print("Total GPA: %.2f" % gpa)

while True:
    #intro
    print("""------Welcome to CGPA calculator!------\n
    1. Input your current CGPA
    2. Input your total AU for CGPA Computation
    3. Input your number of graded AUs this semester
    4. I want ____ CGPA!
    5. I can only do ____ GPA this semester...
    6. Open GPA calculator
    7. Exit
    """)
    choice = int(input())


    if choice == 1:
        cgpa = float(input("What is your current CGPA? "))
        ptOne = True
    elif choice == 2:
        totalAU = int(input("What is your total AU for CGPA Computation so far? "))
        ptTwo = True
    elif choice == 3:
        semAU= int(input("How many graded AUs do you have this semester? "))
        ptThree = True
    elif choice == 4:
        if ptOne and ptTwo and ptThree == True:
            goalCGPA = float(input("What is your CGPA goal for this semester? "))
            goalGPA = (goalCGPA * (totalAU+semAU) - (cgpa*totalAU))/semAU
            print("To achieve your CGPA goal, you will need to score a GPA of %.2f" % goalGPA)
        else:
            print("Please complete Parts 1-3 first.")
    elif choice == 5:
        if ptOne and ptTwo and ptThree == True:
            estGPA = float(input("What GPA do you think you can get this semester? "))
            estCGPA = (cgpa*totalAU + estGPA*semAU)/(totalAU+semAU)
            print("With that GPA, your CGPA will be %.2f" % estCGPA)
        else:
            print("Please complete Parts 1-3 first.")
    elif choice == 6:
        calcGPA()
    elif choice == 7:
        print("Thank you!")
        break
    else:
        print("Please enter a valid choice between 1 and 6")

    time.sleep(1)
