#Macie Pelle Thursday 3:30pm
#mpelle@purdue.edu
#This program uses lists and an external file to make new lists that are written to a new file. It finds the max and min as well as updates the scores.
#Academic Honesty:
#I attest that this is my original work.
#I have not used unauthorized source code, either modified or unmodified.
#I have not given other fellow student(s) access to my program.

from ast import excepthandler

def main():
    Names = list()
    Scores = list()

    try:
        #Calls the input file from the directory
        fileName = "C:/Users/macar/OneDrive/Desktop/Classes/CNIT 155 Python/Assignments/input.txt"
        #Reads the input file
        inputFile = open(fileName, "r")

        for line in inputFile:
            Temp = line.split(",")

            Names.append(Temp[0])
            Scores.append(float(Temp[1]))

        inputFile.close()
        #Calls the output file from the directory       
        fileName = "C:/Users/macar/OneDrive/Desktop/Classes/CNIT 155 Python/Assignments/output.txt"
        #Writes to the output file
        outputFile = open(fileName, "w")
        
        
        #Finds the maximum value
        outputFile.write("Maximum Score is : " + str(max(Scores)) + "\n")
        for i in range(0, len(Names)):
           
            if Scores[i] == max(Scores):
                data = Names[i] + " " + str(Scores[i]) + "\n"
                outputFile.write(data)

        outputFile.write("\n")
        #Finds minimum value
        outputFile.write("Minimum Score is : " + str(min(Scores)) + "\n")
        for i in range(0, len(Names)):
            if Scores[i] == min(Scores):
                data = Names[i] + " " + str(Scores[i]) + "\n"
                outputFile.write(data)

        outputFile.write("\n")  
        
        updatedScores = list()
        outputFile.write("Updated Score(s):" + "\n")
        for i in range(0, len(Names)):
            if Scores[i] == min(Scores):
                data = Names[i] + " " + str(Scores[i] + 0.5) + "\n"
                outputFile.write(data)

        outputFile.close()
        
        
        print("Printing every content in the file....\n", Names, "\n", Scores)
        print("Scores have been updated. Check the output file!")

    except FileNotFoundError:
        print("The program failed to open the file. Make sure of the following:\n\tThe file to read is located in the same folder where this program is!\n\tThe file's name is spelled correctly!")

main()