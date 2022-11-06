#============================================================================
#Macie Pelle Thursday 3:30pm
#mpelle@purdue.edu
#This program using a while loop to run the conditons inside it if the while loop is true. The user inputs a number from the selection and that condition will run. If the user inputs a number outside of 1-6 the program will tell them the input is invalid and to enter a proper number.
#Academic Honesty:
#I attestthat this is my original work.
#I have not used unauthorized source code, either modified or unmodified.
#I have not given other fellow student(s) access to my program.
#============================================================================

def main():
    choice = 0
    
    while (choice != 6):
        #Tells the user the options they have to choose from and what they do
        print("\t\tWhile loops lab\n==================================================================\n1. Print all natural numbers between 1 and N\n2.Add up all natural numbers between 1 and N\n3. Add up all even numbers between 1 and N\n4.Compute the sum of the square numbers between 1 and N\n5. Compute the sum and average of the cube numbers between 1 and N\n6. Exit\n==================================================================")
        
        choice = int(input("Choose one of the following options to perform: "))
        #if the user inputs 1, this will ask them to enter a value and then will output the numbers from 1 to that number
        if choice == 1:
            natural = int(input("Enter a natural number for N: "))
            
            counter = 1
            
            print("Displaying natural numbers from", counter, "to", natural)
            
            while counter <= natural:
                print(counter)
                counter += 1
        #If the user inputs 2, this will ask them to enter a value and then will output the numbers from to the that number as well as the sum        
        elif choice == 2:
            natural = int(input("Enter a natural number for N: "))
            
            counter = 1
            sum = 0
            
            print("Displaying natural numbers from", counter, "to", natural)
            #Calculates the sum and prints the numbers from 1 to the user input
            while counter <= natural:
                    print(counter)
                    sum = sum + counter
                    counter += 1 

            print("The sum of the numbers from 1 to", natural, "is", sum)
        #If the user inputs 3, this will ask them to enter a value and then will output the even number from 1 to the number as well as the sum    
        elif choice == 3:
            natural = int(input("Enter a natural number for N: "))
            
            counter = 1
            sum = 0
            
            print("Displaying even natural numbers from", counter, "to", natural) 
            #Calculates the even numbers and the sum
            while counter <= natural:
                if(counter % 2 != 1):
                    print("{0}".format(counter))
                    #Calculates the sum
                    sum = sum + counter
                counter = counter + 1

            print("The sum of even numbers from 1 to", natural, "is", sum, "\n") 
        #This will output the squares of all numbers between 1 and the number the user input as well as the sum of those numbers    
        elif choice == 4:
            natural = int(input("Enter a natural number for N: "))
            
            counter = 1
            sum = 0
            
            print("Displaying the squares of numbers from", counter, "to", natural)
            #Calculates the square of each number
            while counter <= natural:
                counterSquare = pow(counter, 2)
                print("{0}".format(counterSquare))
                #Calculates the sum
                sum = sum + counterSquare
                counter = counter + 1          
            print("The sum of the squares of numbers from 1 to", natural, "is", sum, "\n")
        #This will output the cubes of all numbers between 1 and the number the user input as well as the sum and average of those numbers    
        elif choice == 5:
            natural = int(input("Enter a natural number for N: "))
            
            counter = 1
            sum = 0
            
            print("Displaying the cubes of numbers from", counter, "to", natural)            
            #Calculates the cubes for each number as well as the sum and average
            while counter<= natural:
                counterCube = pow(counter, 3)
                print("{0}".format(counterCube))
                sum = sum + counterCube
                counter = counter + 1
                #Calculates the average and formats it
                average = sum / natural
                average1 = "{:.2f}".format(average)


            print("The sum of cubes of numbers from 1 to", natural, "is", sum) 
            print("The average of cubes of numbers from 1 to", natural, "is", average1)
        #This ends the while loop    
        elif choice == 6:
            print("Good bye!")
            exit()
        #This tells the user their input is invalid and to enter a number between 1 and 6   
        else:
            print("Invalid Input!\nEnter a number between 1 and 6")
main()
    