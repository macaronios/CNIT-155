#Macie Pelle Thursday 3:30pm
#mpelle@purdue.edu
#This program uses user defined functions that are called from the main function when the if statement is true for them
# Academic Honesty:
#I attestthat this is my original work.
#I have not used unauthorized source code, either modified or unmodified.
#I have not given other fellow student(s) access to my program.

def factorial(n):
    
    factorial = 1
    num = n
    #finds the factorial of the number entered by the user
    for i in range(1, n +1):
        factorial = factorial * i
    print(num, "!=", factorial, "\n")
    
def sumOdds(x, y):
    
    print("Displaying odd numbers from n1 to n2 (n1<=n2)")
    
    sum = 0
    #Prints off numbers from a range the user input and finds the sum
    for i in range(x, y + 1):
        if (i % 2 != 0):
            print(" ")
            print(i, end= " ")
            sum = sum + i
    print("\n")
    print("The sum of odd numbers is ", sum)
    
def sumInverse(n1, n2):
    print("Displaying the inverse of the numbers from n1 to n2 (n1<=n2)")
    
    sum = 0.0
    #finds the inverse of numbers entered by the user and finds the sum
    for i in range(n1, n2+1):

        print("1 /", str(i))

        sum = sum + (1 / i)
    #Prints the the sum of the numbers and formats them to two decimal places
    print("The sum of numbers between ", str(n1), "and", str(n2), "is: ", "{:.2f}".format(sum))
    
def findChar(sentence, letter):
    
    sum = 0
    #finds the number of times a letter appears in a string
    for i in sentence:
        if i.upper() == letter.upper():
            sum = sum + 1
    #outputs the number of characters based on the user input
    print("The character", letter, "appeared " + str(sum))
    

def main():
    #controls the while loop
    loopCtrl = True
    #when true, the commands in the loop will run
    while loopCtrl:
        #outputs the users choices
        print("==================User Defined Functions Menu==================\n1. Compute n Factorial\n2. Sum of all odd numbers from n1 to n2 (n1<=n2)\n3. Sum of the inverse of the numbers between n1 and n2 (n1<=n2)\n4. Find the number of characters\n5. Exit\n===============================================================\n")
        
        choice = int(input("Choose one of options to perform: "))
        
        if choice == 1:
            print("1. Compute n Factorial")
            
            n = int(input("Please enter a natural number for n: "))
            #called into the main loop when choice 1 is inputted            
            factorial(n)
        
        elif choice == 2:
            print("\n2.  Sum of all odd numbers from n1 to n2 (n1<=n2)")
            #tells the user to input a value
            x = int(input("Please enter a natural number for n1: "))
            y = int(input("Please enter a natural number for n2: "))
            #called into the main loop when choice 2 is inputted 
            sumOdds(x,y)
        
        elif choice == 3:
            print("\n3. Sum of the inverse of the numbers between n1 and n2 (n1<=n2)")
            
            n1 = int(input("Please enter a natural number for n1: "))
            n2 = int(input("Please enter a natural number for n2: "))
            #called into the main loop when choice 3 is inputted 
            sumInverse(n1, n2)
            
        elif choice == 4:
            print("4. Find the number of characters")
            
            sentence = input("Please enter the string to work on: ")
            letter = input("Please enter a character that you want to count in the string entered above: ")
            #called into the main loop when choice 4 is inputted 
            findChar(sentence, letter)
        #Exits the for loop    
        elif choice == 5:
            print("Bye")
            loopCtrl = False
        #tells the user their input is invalid    
        else:
            print("Invalid option! Enter a number between 1 and 5")
                
main()