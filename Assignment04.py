#Macie Pelle Thursday 3:30pm
#mpelle@purdue.edu
#This program uses the math function to allow the user to make multiple calclations depending on what they select. It uses multi-state if statements to give the uer multiple different inputs to select. After the user inputs a certain letter, it will output the information from that selection.
# Academic Honesty:
#I attestthat this is my original work.
#I have not used unauthorized source code, either modified or unmodified.
#I have not given other fellow student(s) access to my program.

#calls the math function to allow calculations to be completed with different math functions. Used in this program is math.pi and math.sqrt
import math

def main():
    
    #Prints the inputs and wht they will show for the user
    print("\tArea and Volume Calculators \n========================================== \nA. Area Of A Rectangle \nB. Area Of A Trapezoid \nC. Volume Of A Sphere \nD. Volume Of A Hexagonal Pyramid \nE. Volume Of An Octagonal Prism \n==========================================")
    
    #defines letter to be used in the multi-state if statement and tells the user to input an option
    letter = input("\nChoose one of the following options to calculate:\n")
    
    #multistate if statement that will run the input the user entered
    if letter == "A":
        print("\nOption A. Area Of A Rectangle")
        
        width  = float(input("\nEnter the width of the rectangle: "))
        length = float(input("Enter the length of the rectangle: "))
        
        #Calculates the area of a rectangle
        areaRectangle = width * length
        areaRectangle1 = "{:.2f}".format(areaRectangle)
        
        print("\nThe area of the rectangle is ",areaRectangle1)
    
    elif letter == "B":
        print("\nOption B. Area Of A Trapezoid")
        
        short = int(input("\nEnter the short base of the trapezoid: "))
        long = int(input("Enter the long base of the trapezoid: "))
        height = int(input("Enter the height of the trapezoid: "))
        
        #Calculates the area of a trapezoid
        areaTrapezoid = ((short + long)/2) * height
        areaTrapezoid1 = "{:.2f}".format(areaTrapezoid)
        
        print("\nThe area of the trapezoid is: ",areaTrapezoid1)
        
    elif letter == "C":
        print("\nOption C. Volume Of A Sphere")
        
        radius = float(input("\nEnter the radius of the sphere: "))
        
        #Calculates the volume of a sphere
        volumeCircle = (4/3) * math.pi * radius**3
        volumeCircle1 = "{:.2f}".format(volumeCircle)
        
        print("\nThe volume of the sphere is: ",volumeCircle1)
        
        
    elif letter == "D":
        print("Option D. Volume Of A Hexagonal Pyramid")
        
        basePyramid = float(input("\nEnter the base edge of the hexagonal pyramid: "))
        heightPyramid = float(input("Enter the height of the hexagonal pyramid: "))
        
        #Calculates the volume of a hexagonal pyramid
        volumePyramid = (math.sqrt(3)/2) * basePyramid**2 * heightPyramid
        volumePyramid1 = "{:.2f}".format(volumePyramid)
        
        print("\nThe volume of the hexagonal pyramid is: ",volumePyramid1)                     
        
    elif letter == "E":
        print("\nOption E. Volume Of An Octagonal Prism")
        
        basePrism = float(input("\nEnter the base edge of the octagonal prism: "))
        heightPrism = float(input("Enter the height of the octagonal prism: "))
        
        #Calculates the volume of an octagonal prism
        volumePrism = 2 * (1 + math.sqrt(2)) * basePrism**2 * heightPrism
        volumePrism1 = "{:.2f}".format(volumePrism)
        
        print("\nThe volume of the octagonal prism is: ",volumePrism1)
        
    else:
        #Informs the user the input they entered is invalid and they must select and option between A and E
        print("Invalid Input!\nPlease enter your choice between A and E.")
    
main()