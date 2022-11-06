#Macie Pelle Thursday 3:30pm
#mpelle@purdue.edu
#This program uses 
#Academic Honesty:
#I attest that this is my original work.
#I have not used unauthorized source code, either modified or unmodified.
#I have not given other fellow student(s) access to my program.


def StepsToMiles(lst1):
    Miles = list()
    
    for i in lst:
        
        Miles.append(i / 2000.0)
    
    return Miles

def main():
    
    print("****************************************************\n**********\t\t\t\t  **********\n**********   Steps to Miles Calculator\t  **********\n**********\t\t\t\t  **********\n****************************************************")
    Steps = list()
    day = 1
    while day <= 7:
        
        steps = 0
        
        try:
            
            steps = int(input("Enter the number of steps for Day " + str(day) + ":"))
            
            if steps < 0:
                raise ValueError
            
            day +=1
            Steps.append(steps)            
                    
        except ValueError:
            print("\nException: Wrong value entered!\nPlease enter an integer value in a correct format!\n")
                
    print("*** The number of miles you walked this week ***")
        
            
               
main()