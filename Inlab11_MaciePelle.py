#Macie Pelle Thursday 3:30pm
#mpelle@purdue.edu
#This program has 
#I attest that this is my original work.
#I have not used unauthorized source code, either modified or unmodified.
#I have not given other fellow student(s) access to my program.

def main():
    
    books = list()
    
    try:
        
        inputFile = open("C:/Users/macar/OneDrive/Desktop/Classes/CNIT 155 Python/Labs/Books.txt", "r")
        outputFile = open("C:/Users/macar/OneDrive/Desktop/Classes/CNIT 155 Python/Labs/book_analysis.txt", "w")
        
        book = inputFile.readlines()
        
        print("Printing the contents of the file...", books)
        

        outputFile.write("======== Analysis Results ========\n")
        outputFile.write("1. The number of books in the file: " + (len(books)) + "\n") 
        
        outputFile.write("2. Titles of Books which have more than 2 words: \n\n")

        for i in books:
            if len(i.split()) > 2:
                outputFile.write(i)       
       
        outputFile.write("3. Organized book titles: \n")
        
        for i in books:
            outputFile.write(i.title())      
       
        
    except FileNotFoundError:
        print("The program failed to open the file. Make sure of the following:\n\tThe file to read is located in the same folder where this program is!\n\tThe file's name is spelled correctly!")