#Macie Pelle Thursday 3:30pm
#mpelle@purdue.edu
#This program uses nested for loops to display different options depending on what the user inputs
# Academic Honesty:
#I attestthat this is my original work.
#I have not used unauthorized source code, either modified or unmodified.
#I have not given other fellow student(s) access to my program.

def main():
    #If true the while loop runs and if false the program will exit
    loopCtrl = True
    
    while loopCtrl:
        #Displays the options the user has to choose from
        print("\t\tFor Loops Lab\n==================================================\n1. Display and Add natural numbers from N to 1\n2. The multiplication table of N\n3. The pyramid of stars\n4. The pyramid of numbers\n5. Exit\n==================================================")
        #tells the user to choose an option from the display menu
        option = int(input("Choose one of the options to perform: "))
        
        if option == 1:
            
            natural = int(input("Enter a natural number for N: "))
            print("Displaying natural numbers from", natural, "to 1")
            
            sum = 0
            #prints user input number in descending order to 1          
            for i in range(natural, 0, -1):
                print (i)
                sum = sum + i
            #prints out the sum of the numbers in the for loop     
            print("The sum of natural numbers from", natural, "to 1: ", sum)
            
        elif option == 2:
            
            natural = int(input("Enter a natural number for N: "))
            print("The multiplication table of", natural)
            #displays a multiplication table with the users input
            for i in range(1, 11):
                print(natural, "*", i, "=", natural * i)
            
        elif option == 3:
            
            row = int(input("Enter a number to define the number of rows of *: "))
            #displays a triangle made of stars
            for line in (range(1, row+1)):
                for i in range(1, row+1):
                    print("", end="")
                for j in range(1, line+1):
                    print("*", end=" ")
                print()
                
        elif option == 4:
            
            row = int(input("Enter a number to define the number of rows of numbers: "))
            #displays numbers in a reversed triangle from 1 to the number the user inputs
            for i in reversed(range(row)):
                for j in range(i + 1):
                    print(j + 1, end=" ")
                print()
        #tells the user good bye and ends the while loop        
        elif option == 5:
            print("Good bye!")
            loopCtrl = False
        #tells the user their input was invalid    
        else:
            print("Invalid option!\nPlease choose an option between 1 and 5")
main()