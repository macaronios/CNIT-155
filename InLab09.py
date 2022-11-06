#Macie Pelle Thursday 3:30pm
#mpelle@purdue.edu
#This program uses user defined functions and try/except to convert steps to miles and find the average
#Academic Honesty:
#I attest that this is my original work.
#I have not used unauthorized source code, either modified or unmodified.
#I have not given other fellow student(s) access to my program.


def StepsToMiles(lst):

    miles = list()
    #Converts steps to miles
    for step in lst:
        miles.append(float(step / 2000))

    return miles

def main():
    
    print("****************************************************\n**********\t\t\t\t  **********\n**********   Steps to Miles Calculator\t  **********\n**********\t\t\t\t  **********\n****************************************************")
    #creates lists based on user inputs
    steps = list()
    miles_walked = list()

    day = 1

    while day <= 7:

        stepCount = 0

        try:
            #Asks the user to enter the amount of steps for the day
            stepCount = int(input("Enter the number of steps for Day " + str(day) + ": "))
            #If the user enters a value less than 0 it'll print an error message
            if stepCount < 0:
                raise ValueError

            day += 1
            steps.append(stepCount)
        #Error message
        except ValueError:
            print("\nException: wrong value entered\nPlease Enter an integer in the correct format!\n")
    #Sets miles_walked = to Stepstomiles udt
    miles_walked = StepsToMiles(steps)
    print("\n*** The number of miles you walked this week ***")

    averageMiles = 0
    #displays miles walked each day
    for n in range(0, len(miles_walked)):
        print("Day ", n+1, " : {:.2f}".format(miles_walked[n]), " miles")
        averageMiles += miles_walked[n]
    #Calculates the average of miles walked
    averageMiles = averageMiles / 7
    #prints the average miles walked
    print("\nThe average of miles walked : {:.2f}".format(averageMiles))
    #tells the user it is the end of the program
    print("\nEnd of the program")

main()