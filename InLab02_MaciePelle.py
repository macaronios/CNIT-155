#======================================================================
#Macie Pelle, Thursday 3:30pm
#mpelle@purdue.edu
#This program uses inputs and prints to display user input values in the command window.
# Academic Honesty:
#I attestthat this is my original work.
#I have not used unauthorized source code, either modified or unmodified.
#I have not given other fellow student(s) access to my program.

def main():
    
    #Prints out "This is InLab02 for CNIT155 by Macie Pelle" in the command window
    print("This is Inlab02 for CNIT155 by Macie Pelle")
    #Using int with the input makes student a class int
    student = int(input("\nEnter the number of students in CNIT 155:"))
    #This prints out the number of students in CNIT155 that the user inputted
    print("The number of students in CNIT155 is", student)
    #This shows the data type of the variable student
    print("The data type of the number of students is",type(student))
    
    textbook = float(input("\nEnter the price of the textbook: "))
    #This line formats the print to round off at 2 decimal places
    textbook2 = "{:.2f}".format(textbook)
    print("The price of the textbook is $", textbook2)
     #This shows the data type of the variable textbook
    print("The data type of the price is",type(textbook))
    
    fahrenheit = float(input("\nEnter today's temperature in Fahrenheit (F): "))
    #This calculation converts the temperature from fahrenheit to celsius
    celsius = (fahrenheit - 32) * 5/9
    celsius2 = "{:.2f}".format(celsius)
    print("Today's temperature in Celsius is", celsius2, "C")
     #This shows the data type of the variable fahrenheit
    print("The data type of the temperature is", type(fahrenheit))

main()
