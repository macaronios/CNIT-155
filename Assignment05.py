#Macie Pelle Thursday 3:30pm
#mpelle@purdue.edu
#This program uses while loops so the user is being asked to enter inputs. When an input is entered A-F that desired function will run and then the user will be asked again to enter an input.
# Academic Honesty:
#I attestthat this is my original work.
#I have not used unauthorized source code, either modified or unmodified.
#I have not given other fellow student(s) access to my program.


#Calls the math functions into the program
import math

def main():
  
  #Runs the code in the while loop when the loop is true
  while True:
    
    #Prints out the options the user has to choose from
    print("\t\tWhile Loops Practice\n=======================================================\nA. Sum of odd natural numbers from 1 to N\nB. Sum of squares of odd natural numbers from 1 to N\nC. Sum of cubes of odd natural numbers from 1 to N\nD. Find the factorial of N\nE.Print the multiplication table of N\nF. Exit\n=======================================================\n")
    
    #Tells the user to input one of the options
    letter = input("Choose one of the options to perform: ")
    #If the letter A is entered this condition will run the output of odd numbers between 1 and the user input 
    if letter == "A":
                 
        natural = int(input("Enter a natural number for N: "))
               
        counter = 1
        sum = 0
        
        print("Displaying odd natural numbers from", counter, "to", natural)
        #outputs all the odd numbers between 1 and the number the user input
        while counter <= natural:
            if(counter % 2 != 0):
                print("{0}".format(counter))
                sum = sum + counter
            counter = counter + 1
        #Prints the sum of the odd numbers from 1 to the number the user input
        print("The sum of odd natural numbers from 1 to", natural, "is", sum, "\n")            
    #If the letter B is entered this condition will run the output of squared odd numbers between 1 and the user input  
    elif letter == "B":       
        
        natural = int(input("Enter a natural number for N: "))
               
        counter = 1
        sum = 0
        
        print("Displaying the squares of odd natural numbers from", counter, "to", natural)
        #Prints the square of each odd number from 1 to the number the user input
        while counter <= natural:
            counterSquare = pow(counter, 2)
            if(counterSquare % 2 != 0):
                print("{0}".format(counterSquare))
                sum = sum + counterSquare
            counter = counter + 1
        #Prints the sum of squares of odd numbers between 1    
        print("The sum of squares of odd natural numbers from 1 to", natural, "is", sum, "\n")
    #If the letter B is entered this condition will run the output of cubed even numbers between 1 and the user input  
    elif letter == "C":
        
        natural = int(input("Enter a natural number for N: "))
               
        counter = 1
        sum = 0
        
        print("Displaying the cubes of even natural numbers from", counter, "to", natural)
        #Prints the cube of each numbers from 1 to the number the user input
        while counter<= natural:
          counterCube = pow(counter, 3)
          if(counterCube % 2 !=1):
              print("{0}".format(counterCube))
              sum = sum + counterCube
          counter = counter + 1
        #Prints the sum of cubes of even numbers from 1
        print("The sum of cubes of even natural numbers from 1 to", natural, "is", sum, "\n")
    #If the letter D is entered this condition will run the factorial of the user input 
    elif letter == "D":
        
        natural = int(input("Enter a natural number for N: "))
         
        factorial = 1     
        counter = 1
        #Calculates the factorial of the user input
        while counter <=  natural:
          factorial = factorial * counter
          counter = counter + 1
        #Prints the factorial  
        print("The factorial of", natural, "is", factorial)
    #If the letter E is entered this condition will run the output of multiplication table for the user input     
    elif letter == "E":
      
        natural = int(input("Enter a natural number for N: "))
        
        counter = 0
        
        print("Multiplication table of", natural)
        #Prints the multiplication table from the user input number to 10
        while counter < 10:
          counter = counter + 1
          print(natural, "*", counter, "=", natural * counter)
    #Prints good bye and ends the while loop     
    elif letter == "F":
        print("Good bye!")
        exit()
    #Tells the user to input an option between A and F because the input they entered was invalid      
    else:
      print("Invalid Input!\nChoose an option between A and F")
      
main()