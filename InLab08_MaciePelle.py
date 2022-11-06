#Macie Pelle Thursday 3:30pm
#mpelle@purdue.edu
#This program uses user defined functions and lists to find the vonversion of USD to Euro, the averga eof both, and the prices that are under $50
#Academic Honesty:
#I attest that this is my original work.
#I have not used unauthorized source code, either modified or unmodified.
#I have not given other fellow student(s) access to my program.

def UsdtoEuro(lst):
    #User defined list
    Euro = list()
    #Converts USD to Euro
    for i in lst:
        Euro.append(i * 0.85)

    return Euro

def PrintInfo(lst1, lst2):
    #prints user defined lists in columns
    for n in range(0, len(lst1)):
        print("\t{:.2f}".format(lst1[n]), "\t\t{:.2f}".format(lst2[n]))

def Average(lst):
    #calculates the averages of USD and Euro
    sum = 0
    for p in lst:
        sum += p

    averagePrice = sum / len(lst)

    return averagePrice

def FindPrices(lst1, lst2):
    #Finds prices that are under $50
    for n in range(0, len(lst1)):
        if lst1[n] < 50.00 and lst2[n] < 50.00:
            print("\t${:.2f}".format(lst1[n]), "\t\t€{:.2f}".format(lst2[n]))

def main():
    #User defined list
    USD = list()

    while True:
        #tells the user to enter in a price in USD
        userInput = float(input("Enter a price in USD. Use -1 to stop data entry: "))
        #uf userinput = -1 it breaks the loop and if not the loop will continue asking for user inputs
        if userInput == -1:
            break
        else:
            USD.append(userInput)
   
    #tells the user how many inputs were entered
    print("\nNumber of prices entered:", len(USD))
    
    print("\n\tUSD($)\t\tEuro(€)\n==============================================")
   
    #calls Usd toEuro to convert the USD prices to Euro
    Euro = UsdtoEuro(USD)
    
    #calls and prints the user defined lists in the main function
    PrintInfo(USD, Euro)
    
    #prints the average title in the code
    print("==============================================")
    print("================== Average ===================\n")
    
    #prints the average for USD and Euros
    print("The average of prices in USD is $", "{:.2f}".format(Average(USD)))
    print("The average of prices in Euro is €", "{:.2f}".format(Average(Euro)), "\n") 
    
    #Prints the prices under $50 title
    print("========= Price(s) under $50 is(are) =========")
    print("\tUSD\t\tEuro")
    print("\t----------\t----------")  
    #finds the prices that are under $50
    FindPrices(USD, Euro)

main()