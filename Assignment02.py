#Macie Pelle Thursday 3:30pm
#mpelle@purdue.edu
#This program runs a conversion calculator that uses basic math components to print pounds to kilograms, celcius to fahrenheit, miles to kilometers, and feet to inches.
# Academic Honesty:
#I attestthat this is my original work.
#I have not used unauthorized source code, either modified or unmodified.
#I have not given other fellow student(s) access to my program.

def main():
    
    #Prints the title block at the top of the program that reads "CNIT155 Assignment 02 and Conversion Calulator" surrounded by a box of asterixs
    print("\t********************************************\n\t*\t   CNIT155 Assignment 02\t   *\n\t*\t                        \t   *\n\t*\t   Conversion Calculator\t   *\n\t********************************************\n")
    #Asks the user to enter their full name for it to be printed in a new line that says "My name is..."
    fullName = input("Enter your full name: ")
    print("My name is", fullName)
    
    print("\n** 1st. Pounds to Kilograms conversion **")
    pound = float(input("What is the weight in pounds to convert it to kilograms?: "))
    #Calculates the conversion from pounds to kilograms
    kilogram = pound / 2.2046
    #Floats the input to pound and kilograms to two decimal places
    poundStr = "{:.2f}".format(pound)
    kilogramStr = "{:.2f}".format(kilogram)
    print("The weight entered in pounds is", poundStr, "lb and it is", kilogramStr, "kg")
    
    print("\n** 2nd. Celsius to Fahrenheit conversion **")
    celsius = float(input("Enter the Celsius temperature to convert it to Fahrenheit: "))
    #Calculates the conversion from celsius to fahrenheit
    fahrenheit = (celsius * 9/5) + 32
    #Floats the input to celsius and fahrenheit to two decimal places
    celsiusStr = "{:.2f}".format(celsius)
    fahrenheitStr = "{:.2f}".format(fahrenheit)
    print("The entered temperature in Fahrenheit is", celsiusStr, "C and it is", fahrenheitStr, "F")
    
    print("\n** 3rd. Miles to Kilometers conversion **")
    miles = float(input("Enter miles to convert it to kilometers: "))
    #Calculates the conversion from miles to kilometers
    kilometers = miles * 1.609344
    #Floats the input to mile and kilometer to two decimal places
    milesStr = "{:.2f}".format(miles)
    kilometersStr = "{:.2f}".format(kilometers)
    print("The entered distance in miles is", milesStr, "mi and it is", kilometersStr, "km.")
    
    print("\n** 4th. Feet and Inches to Centimeters? **")
    print("What is your height in feet and inches?")
    feet = input("Feet?: ")
    inches = input("Inches?: ")
    #Calculates the conversion from feet and inches into centimeters
    centimeters = ((float(feet) * 12) + float(inches)) * 2.54
    #Prints in the comman window the feet and inches inputted and the conversion to centimeters to two decimal places
    print("The entered height is", feet, "feet", inches, "inches and it is {:.2f}".format(centimeters), "cm")
    
main()