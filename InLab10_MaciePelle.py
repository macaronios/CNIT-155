#Macie Pelle Thursday 3:30pm
#mpelle@purdue.edu
#This program has the user import a file that is read by the code and written to an output file that shows the amount of numbers in the list, the average, max, and min.
#Academic Honesty:
#I attest that this is my original work.
#I have not used unauthorized source code, either modified or unmodified.
#I have not given other fellow student(s) access to my program.

from ast import excepthandler

def main():
    #Makes a list for scores
    Scores = list()
    
    try:
        #Calls the input file from the directory
        fileName = "C:/Users/macar/OneDrive/Desktop/Classes/CNIT 155 Python/Labs/Scores.txt"
        #Reads the input file
        inputFile = open(fileName, "r")
        #Sets the numbers in scores as a float
        for line in inputFile:
            Temp = line.split(",")

            Scores.append(float(Temp[0]))
        #Closes inputFile
        inputFile.close()        
        
        #Calls the output file from the directory       
        fileName = "C:/Users/macar/OneDrive/Desktop/Classes/CNIT 155 Python/Labs/Scores_stats.txt"
        #Writes to the output file
        outputFile = open(fileName, "w") 
        
        #Finds number of scores in the list
        outputFile.write("The number of scores in the list is " + str(len(Scores)) + "\n")
        
        #Finds the average
        average = sum(Scores) / len(Scores)
        outputFile.write("The average of scores in the list is " + "{:.2f}".format(average) + "\n")
        
        #Finds max value
        outputFile.write("Maximum Score is : " + "{:.2f}".format(max(Scores)) + "\n")

        #Finds minimum value
        outputFile.write("Minimum Score is : " + "{:.2f}".format(min(Scores)) + "\n")
        
        #Prints the scores
        print("Printing the contents of the file....\n", Scores)  
        
    #Tells the user the file couldn't be open
    except FileNotFoundError:
        print("The program failed to open the file. Make sure of the following:\n\tThe file to read is located in the same folder where this program is!\n\tThe file's name is spelled correctly!")
    
    
main()