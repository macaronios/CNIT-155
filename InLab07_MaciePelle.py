#Macie Pelle Thursday 3:30pm
#mpelle@purdue.edu
#This program uses user input to create lists that shows students names and their gpas.
#Academic Honesty:
#I attestthat this is my original work.
#I have not used unauthorized source code, either modified or unmodified.
#I have not given other fellow student(s) access to my program.

def main():
    #tells the user to input how many students are in their class
    students = input("How many students are there in your class?: ")
    #lists created from user input
    studentNames = list()
    studentGPAs = list()

    for n in range(1, int(students)+1):
        #user inputs a name
        printString = "Input student #" + str(n) + " Name: "
        Name = input(printString)

        while True:
            #user inputs a valid gpa
            printString = "Input student #" + str(n) + " GPA: "
            GPA = float(input(printString))
            #tells the user their input is invalid if it is < 0 or < 4.0
            if 0.0 < float(GPA) <= 4.0:
                break
            else:                
                print("A GPA must be between 0 and 4.0 (both inclusive)!\n")

        studentNames.append(Name)
        studentGPAs.append(GPA)
        #prints the list titles
    print("=================== List ====================")
    print("\t  Name\t\t  GPA      ")
    print("\t--------\t-------")
    #prints the lists
    for i in range(0, int(students)):
        #prints the user created lists
        print("\t", studentNames[i], "\t\t", "{:.1f}".format(studentGPAs[i]))

    print("============================================")

    sum = 0
    #calculates the average gpas
    for x in studentGPAs:

        sum += float(x)
        
    average = sum / int(students)
    #prints the average, min and max gpas
    print("Average GPA is {:.2f}".format(average))
    print("Max GPA is {:.2f}".format(float(max(studentGPAs))))
    print("Min GPA is {:.2f}".format(float(min(studentGPAs))))
    print("============================================")

main()