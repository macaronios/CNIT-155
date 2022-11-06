#Macie Pelle Thursday 3:30pm
#mpelle@purdue.edu
#This program uses nested for loops to run different commands when the while loop is true. The user has 5 options to choose from which each display different outputs.
# Academic Honesty:
#I attestthat this is my original work.
#I have not used unauthorized source code, either modified or unmodified.
#I have not given other fellow student(s) access to my program.

def main():
    #used to control while loop. if false, while loop is exited
    loopCtrl = True
    #when true, the commands in the loop will run
    while loopCtrl:
        #displays the input options
        print("\tNested For Loops Lab\n======================================\n1. A Multiplication table\n2. N for N times with commas\n3. The Table of Stars\n4. The inverted Triangle\n5. Exit\n======================================")
        #tells the user to input an option from the table displayed
        option = int(input("Choose one of the options to perform: "))
        #If option 1 is selected, this command will run
        if option == 1:
            #tells the user to enter a number
            number = int(input("Enter a number for N: "))
            print("Displaying", number, "x", number, "of A Multiplication Table")
            #Prints the multiplication table
            for x in range(1, number+1):
                print(" ")
                for y in range(1, number+1):
                    print(x*y, end=" ")
            print("\n")
            
        elif option == 2:
            #asks the user how many lines they want printed
            lines = int(input("How many lines do you want to print?: "))
            #Prints N to N with commas
            for i in range(1, lines+1):
                for n in range(1, i+1):
                    if n == 1:
                        print(i, end=" ")
                    else:
                        print("," + str(i), end=" ")
                print()
            
        elif option == 3:  
            #asks the user how many ros they want printed
            num_rows = int(input("How many rows do you want to print the stars: "))
            #prints stars in an inversed right triangle
            for row in range(1, num_rows+1):
                for i in range(1, (num_rows - row)+1):
                    print(" ", end=" ")
                for j in range(1, row + 1):
                    print("*", end=" ")
                print()
                
        elif option == 4:
            #asks the user to input the size of the triangle
            triangle = int(input("Enter the size of the triangle of the stars to print: "))
            print("Displaying", triangle, "row(s) of stars of the Triangle")
            #Displays reversed triangle made of stars
            for line in reversed(range(1, triangle+1)):
                for i in range(1, (triangle-line)+1):
                    print(" ", end="")
                for j in range(1, line+1):
                    print("* ", end="")
                print()
        #exits the while loop        
        elif option == 5:
            print("Good bye")
            loopCtrl = False
        #Tells the user their input was invalid and to input an option between 1 and 5
        else:
            print("Invalid input!\nPlease choose an option between 1 and 5")
            
main()