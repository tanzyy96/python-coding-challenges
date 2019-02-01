import time

#function for calculating CGPA
def CGPA_calc():
    try:
        #collect prerequisite information
        print("Before we begin, some information is required to calculate your CGPA!")
        time.sleep(1)
        cgpa = float(input("First question. What is your current CGPA?"))
        time.sleep(1)
        totalAU = int(input("What is your total AU for CGPA Computation so far?"))
        time.sleep(1)
        semAU = int(input("How many graded AUs do you have this semester?"))
        time.sleep(1)

        #2 options for user to select
        print("1. My target CGPA this semester is ...")
        print("2. My target GPA this semester is ... ")
        choice = int(input())
        if choice == 1:
            CGPA_calc_target_CGPA(totalAU, semAU, cgpa)
        elif choice == 2:
            CGPA_calc_target_GPA(totalAU, semAU, cgpa)
        else:   #error message ; Run function again
            print("That is an invalid option.\n")
            cgpaCalc()
    except: #catch input errors
        print("Error! Please enter valid values into the calculator!\n")

def CGPA_calc_target_CGPA(totalAU, semAU, cgpa):
    goalCGPA = float(input("What is your CGPA goal for this semester? "))
    goalGPA = (goalCGPA * (totalAU+semAU) - (cgpa*totalAU))/semAU
    print("To achieve your CGPA goal, you will need to score a GPA of {:.2f}\n".format(goalGPA))

def CGPA_calc_target_GPA(totalAU, semAU, cgpa):
    estGPA = float(input("What GPA do you think you can get this semester? "))
    estCGPA = (cgpa*totalAU + estGPA*semAU)/(totalAU+semAU)
    print("With that GPA, your CGPA will be {:.2f}\n".format(estCGPA))

#function for calculating GPA of a single semester
def GPA_calc():
    try:
        noOfModules = int(input("How many modules do you have this semester?"))
        moduleDict = input_grades(noOfModules)
        #calculate GPA
        calculate_gpa(moduleDict)
    except Exception as e:
        print(e)

def calculate_gpa(moduleDict):
    gpa = 0.0
    for moduleName in moduleDict:
        gpa += gradesDict[moduleDict[moduleName]]
    gpa = gpa/noOfModules
    print("Total GPA: {:.2f}" % gpa)

def input_grades():
    mymodules = {}
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
    for modules in range(noOfModules):              #for each module
        moduleName = input("Name of module:")
        moduleGrade = input("Grade:")
        if moduleGrade not in gradesDict.keys():    #if grade input is invalid
            print("Error. Invalid Grade.")
            return
        mymodules[moduleName] = moduleGrade        #insert module-grade pair into dictionary
        noOfAU += int(input("No of AU: "))          #sum up number of total AUs
    print()
    for modName, modGrade in mymodules.items():    #print out module-grade dictionary
        print("{:10s} {:5s}".format(modName, modGrade))
    return mymodules

# PS right now it may not make sense to have so many functions,
# but in larger programs where functions get repeatedly used again and again,
# this will come in handy.
