import time

#function for calculating CGPA
def cgpaCalc():
    try:
        #collect prerequisite information
        print("Before we begin, some information is required to calculate your CGPA!")
        time.sleep(1)
        cgpa = float(input("First question. What is your current CGPA?"))
        time.sleep(1)
        totalAU = int(input("What is your total AU for CGPA Computation so far?"))
        time.sleep(1)
        semAU = int(input("How many graded AUs do you have this semeester?"))
        time.sleep(1)

        #2 options for user to select
        print("1. My target CGPA this semester is ...")
        print("2. My target GPA this semester is ... ")
        choice = int(input())
        if choice == 1:
            goalCGPA = float(input("What is your CGPA goal for this semester? "))
            goalGPA = (goalCGPA * (totalAU+semAU) - (cgpa*totalAU))/semAU
            print("To achieve your CGPA goal, you will need to score a GPA of %.2f\n" % goalGPA)
        elif choice == 2:
            estGPA = float(input("What GPA do you think you can get this semester? "))
            estCGPA = (cgpa*totalAU + estGPA*semAU)/(totalAU+semAU)
            print("With that GPA, your CGPA will be %.2f\n" % estCGPA)
        else:   #error message ; Run function again
            print("That is an invalid option.\n")
            cgpaCalc()
    except: #catch input errors
        print("Error! Please enter valid values into the calculator!\n")

#function for calculating GPA of a single semester
def calcGPA():
    noOfmodules = int(input("How many modules do you have this semester?"))
    moduleDict = {}     #dictionary to store user modules and respective grade
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
    for modules in range(noOfmodules):              #for each module
        moduleName = input("Name of module:")
        moduleGrade = input("Grade:")
        if moduleGrade not in gradesDict.keys():    #if grade input is invalid
            print("Error. Invalid Grade.")
            return
        moduleDict[moduleName] = moduleGrade        #insert module-grade pair into dictionary
        noOfAU += int(input("No of AU: "))          #sum up number of total AUs
    for modName, modGrade in moduleDict.items():    #print out module-grade dictionary
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
      1. CGPA Calculator
      2. GPA calculator
      3. Exit
    """)
    choice = int(input())

    if choice == 1:
        cgpaCalc()
    elif choice == 2:
        calcGPA()
    elif choice == 3:
        print("Thanks for using this calculator!")
        exit()
    else:
        print("Please enter a valid option.")

    time.sleep(1)
