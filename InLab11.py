#Macie Pelle Thursday 3:30pm
#mpelle@purdue.edu
#This program has 
#I attest that this is my original work.
#I have not used unauthorized source code, either modified or unmodified.
#I have not given other fellow student(s) access to my program.

def main():

    try:
        #Calls input file from directory
        inputFile = open("C:/Users/macar/OneDrive/Desktop/Classes/CNIT 155 Python/Labs/Books.txt", "r")
        
        #Calls output file from directory
        outputFile = open("C:/Users/macar/OneDrive/Desktop/Classes/CNIT 155 Python/Labs/book_analysis.txt", "w")

        books = inputFile.readlines()
        
        #prints the books list in the command window
        print("Printing the contents of the file... \n \n", books)
        
        outputFile.write("======= Analysis Results =======\n\n")
        bookCount = len(books)
        outputFile.write("1. The number of books in the file: ")
        outputFile.write(str(bookCount))
        outputFile.write("\n\n")

        outputFile.write("2. Titles of Books which have more than 2 words: \n\n")
        
        #finds book titles that have more then 2 words
        for i in books:
            if len(i.split()) > 2:
                outputFile.write(i)

        outputFile.write("\n\n")
        outputFile.write("3. Organized Book Titles: \n\n")
        
        #Capitalizes the first letter for each title
        for i in books:
            outputFile.write(i.title())

    except FileNotFoundError:
        print("The program failed to open the file. Make sure of followings:\n  The file to read is located in the same folder where the program is!\n  The file's name is spelled correctly!")

main()