#============================================================================
#Macie Pelle Thursday 3:30pm
#mpelle@purdue.edu
#This program 
#Academic Honesty:
#I attestthat this is my original work.
#I have not used unauthorized source code, either modified or unmodified.
#I have not given other fellow student(s) access to my program.
#============================================================================

import math

def main():
    
   #Tells the user to enter values for d1 and d2
    d1 = int(input("Enter a value for depth1 (D1): "))
    d2 = int(input("Enter a value for depth2 (D2): "))
    
    if (d2>d1):
        
        #Asks the user to enter the value of width and length
        width = int(input("Enter a value for width (W): "))
        length = int(input("Enter a value for length (L): "))
        print("Calculating...")
        
        #The calculations for area and volume of the pool
        side = (d1 + d2) * (length / 2)
        side1 = "{:.2f}".format(side)
        
        d3 = d2 - d1
        hyp = (math.sqrt(d3**2+length**2))
        bottom = hyp * width
        bottom1 = "{:.2f}".format(bottom)
        
        volume = side * width
        volume1 = "{:.2f}".format(volume)
        
        #Prints the calculation value of each equation.
        print("The side area of the pool is ", side1)
        print("The bottom area of the pool is ", bottom1)
        print("The volume of the pool is ", volume1)        

   
    else:
        #Prints the statement if the user enters a d2 value greater than d1
        print("Invalid input! D2 must be greater than D1!") 
    
main()

    