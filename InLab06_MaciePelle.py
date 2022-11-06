#Macie Pelle Thursday 3:30pm
#mpelle@purdue.edu
#This program 
#Academic Honesty:
#I attestthat this is my original work.
#I have not used unauthorized source code, either modified or unmodified.
#I have not given other fellow student(s) access to my program.

#imports themath function
import math
#prints users info
def printInfo():
    print("******************************\n* Macie Pelle                *\n* mpelle@purdue.edu          *\n* CNIT155 InLab06            *\n******************************\n")
    
#if user inputs valid, prints the input is a triangle if false not a triangle
def validate(a, b, c):
    
    
    if a + b > c and b + c > a and a+c > b:
        return True
    
    else:
        return False

#computes area of triangle                
def computeArea(a, b, c):
    
    s = (a + b + c) / 2
    
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    
    area1 = "{:.2f}".format(area)

    
    print("The area of the triangle is ", area1)
#finds minimum value    
def findMin(a, b, c):
    
    if a <= c and a <= b:
        return a
    
    elif b <= a and b <= c:
        return b
    
    else:
        return c
#finds max value   
def findMax(a, b, c):
    
    if c >= a and c >= b:
        return c
    
    elif b >= a and b >= c:
        return b
    
    else:
        return a 
    
def main():
    #calls printInfo function
    printInfo()
    #controls first while loop
    
    
    while True:
    
        a = int(input("Enter the length of side A of a triangle: "))
        b = int(input("Enter the length of side B of a triangle: "))
        c = int(input("Enter the length of side C of a triangle: "))
        
        print("\nValidating a triangle...")
        #calls validate function    
        if validate(a, b, c) == True:
            print("\nThis is a valid triangle")
            #Calls computeArea function
            computeArea(a, b, c)
            #prints the smallest and largest side of the traingle
            print("The smallest side is", float(findMin(a, b, c)), "and the largest side is", float(findMax(a, b, c)))            
        elif validate(a, b, c) == False:
            print("Inputs cannot form a triangle! Please enter different numbers!")
            continue
            
        
    
        
        #asks the user if they want to continue 
        while True:
            compute = input("Do you want to compute again? (Y/N): ")  
            #runs first while loop again
            if compute == "y" or compute=="Y":
            
                
                break
            #ends the program
            elif compute == "N" or compute == "n":
                print("End of the program")
                return False
                
                
            #tells the user their input was invalid
            else:
                print("Invalid input!\nPress Y or N, case sensitive:")
    
main()