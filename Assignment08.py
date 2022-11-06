#Macie Pelle Thursday 3:30pm
#mpelle@purdue.edu
#This program uses user defined functions that are called into the main function to output lists, averages, and items below $100.
#Academic Honesty:
#I attestthat this is my original work.
#I have not used unauthorized source code, either modified or unmodified.
#I have not given other fellow student(s) access to my program.

#applies a 30% discount to the price list and creates a new list called update
def Discount(Prices):
    Update = list()
    for i in Prices:
        Update.append(i * 0.7)
    return Update

#Prints the three lists info
def PrintInfo(Names, IDs, Prices):
    for i, j, k in zip(Names, IDs, Prices):
        print("\t\t", i, "\t\t", j, "\t\t", "{:.2f}".format(k))

#searches for the prices below $100        
def Search(Names, IDs, Prices):
    searchPriceList = list()
    searchIDList = list()
    searchNamesList = list()

    for i in range(0, len(Prices)):
        if Prices[i] < 100:
            searchPriceList.append(Prices[i])
            searchIDList.append(IDs[i])
            searchNamesList.append(Names[i])
    return searchNamesList, searchIDList, searchPriceList
 
 #calculates the average       
def Average(Prices):
    sum = 0
    for i in range(0, 6):
        sum = sum + Prices[i]
    average = sum / len(Prices)
    return average

def main():
    #displays the title block for assignment 08
    print("\t*******************************************************\n\t**********                                   **********\n\t**********           Assignment 08           **********\n\t**********                                   **********\n\t*******************************************************\n")
    #all three lists created
    Names = ["Book", "Tea", "Soda", "Shoes", "Mug", "TV"]
    IDs = [100, 101, 102, 103, 104, 105]
    Prices = [130.00, 153.00, 221.00, 117.00, 55.00, 200.00]
    
    #calls printinfo
    print("\t\tName\t\tID\t\tPrice\n\t=======================================================")
    PrintInfo(Names, IDs, Prices)
    print("\n\t*******************************************************")
    
    #calls average for prices
    print("\t====================   Averages   =====================")
    average = Average(Prices)
    print("\tThe average of prices before the discount is $", "{:.2f}".format(average))#prints the average of Prices
    print("\n\t*******************************************************")
    
    #tells the user the prices were adjusted
    print("\tPrices have been adjusted!")
    
    #calls discount which gives new updated prices
    print("\t\tName\t\tID\t\tPrice\n\t=======================================================")
    Update = Discount(Prices)
    PrintInfo(Names, IDs, Update)    
    print("\n\t*******************************************************")
    
    #calls average to calculate new list average
    average = Average(Update)
    print("\t====================   Averages   =====================")    
    print("\tThe average of prices after the discount is $", "{:.2f}".format(average)) #prints the average of Update
    
    #calls search to print items less than $100
    print("\n\t==============  Products under <= $100  ===============")
    print("\t\tName\t\tID\t\tPrice\n\t=======================================================")
    Update = Search(Names, IDs, Update)
    PrintInfo(Update[0], Update[1], Update[2]) #prints the info of the lists that are below $100
    
main()