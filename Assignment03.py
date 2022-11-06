#Macie Pelle Thursday 3:30pm
#mpelle@purdue.edu
#This program uses the math function to allow the user to use the quadratic formula. The program will have the user enter 3 values to find the discrimanent, roots, and smallest coefficient.
# Academic Honesty:
#I attestthat this is my original work.
#I have not used unauthorized source code, either modified or unmodified.
#I have not given other fellow student(s) access to my program.


#Imports the math function into the program
import math

def main():
   
   #Prompts the user to input the coefficients for a,b, and c
   coefficientA = float(input("Enter the coefficient a: "))
   coefficientB = float(input("Enter the coefficient b: "))
   coefficientC = float(input("Enter the coefficient c: "))
   
   #Prints the quadratic formula with the user inputs
   print("\nQuadratic Equation is: ", coefficientA, "*X^2 + ", coefficientB, "*X +",  coefficientC, "= 0")
   
   #Calculating the discimenant
   discriminant = (coefficientB**2)-(4*coefficientA*coefficientC)
   sqrt_val = math.sqrt(abs(discriminant))
   
   #Prints out the value of the discrimenant
   discriminant1 = "{:.2f}".format(discriminant)
   print("\nThe discrimenant is: ", discriminant1)
   
   #Checks the condition for the discriminant
   if discriminant > 0:
      root_1 = ((-coefficientB + sqrt_val)/(2 * coefficientA))
      root_2 = ((-coefficientB - sqrt_val)/(2 * coefficientA))
      root1 = "{:.2f}".format(root_1)
      root2 = "{:.2f}".format(root_2)
      print("\nThe equation has two real roots:", root1,"and",root2)
      
   elif discriminant == 0:
      real = (-coefficientB /(2 * coefficientA))
      real1 = "{:.2f}".format(real)
      print("\nThe equation has only one root:", real1)
      
   else:
      print("\nThe equation has no real roots")
      
   #Prints the smallest coefficient
   coefficient = [coefficientA, coefficientB, coefficientC]
   coefficient1 = min(coefficient)
   print("\nThe smallest coefficient is: {:.2f}".format(coefficient1))
   
main()