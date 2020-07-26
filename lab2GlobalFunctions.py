##########################################################
#   CS217:      DVD Class
#   Assignment: Lab 2
#   Author:     James Burch
#   Date:       10/27/2016
#   Filename:   lab2GlobalFunctions.py
#   Purpose:    Functions that manipulate DVD objects
#               passed to them
##########################################################

# imports (if any)

from dvd import DVD

# Function to display the values of the DVDs passed to it
def Display_DVD_Information(DVD1, DVD2, DVD3):
    LINE_LENGTH = 60
    NUM_COLUMNS = 4
    COL_WIDTH = LINE_LENGTH // NUM_COLUMNS
    print('{0:<{1}s}'.format("Title:", COL_WIDTH), end='')
    print('${0:<{1}s}'.format("Cost:", COL_WIDTH), end='')
    print('{0:<{1}s}'.format("Type:", COL_WIDTH),"\n")

    for i in range(1,4):
        DVD = eval("DVD" + str(i))
        print('{0:<{1}s}'.format(DVD.getTitle(), COL_WIDTH), end='')
        print('${0:<{1}.2f}'.format(DVD.getCost(), COL_WIDTH), end='')
        print('{0:<{1}s}'.format(DVD.getType(), COL_WIDTH),)
    print("\n")

# Function to display the values of a list of DVDs passed to it
def Display_DVD_Information_From_List(listOfDVD):
    LINE_LENGTH = 60
    NUM_COLUMNS = 4
    COL_WIDTH = LINE_LENGTH // NUM_COLUMNS
    print('{0:<{1}s}'.format("Title:", COL_WIDTH), end='')
    print('${0:<{1}s}'.format("Cost:", COL_WIDTH), end='')
    print('{0:<{1}s}'.format("Type:", COL_WIDTH),"\n")



    for i in range(len(listOfDVD)):
        print('{0:<{1}s}'.format(listOfDVD[i].getTitle(), COL_WIDTH), end='')
        print('${0:<{1}.2f}'.format(listOfDVD[i].getCost(), COL_WIDTH), end='')
        print('{0:<{1}s}'.format(listOfDVD[i].getType(), COL_WIDTH),)
    print("\n")
    

# Function to compute and display the total cost of the DVDs
#   passed to it as well as displaying the average cost
def DisplayTotalAndAverageCosts(DVD1, DVD2, DVD3):

    totalCost = DVD1.getCost()+DVD2.getCost()+DVD3.getCost()
    print("The total cost of the DVD's is: ${0:.2f}".format(totalCost))
    print("The average cost of the DVDs is:  ${0:.2f}".format(totalCost/3))

# Function to interactively change data values of the single
#   DVD object passed to it.
def ChangeDVD(aDVD):

    print("\nType 1 to change title\nType 2 to change type\nType 3 to change cost\nEnter any other number to exit")
    editDVD=int(input("Would you like to change the title, type, or cost?"))
    if editDVD == 1:
        newTitle = input("What is the name of the new Title? :")
        aDVD.setTitle(newTitle)
    elif editDVD == 2:
        aDVD.listValidDVDTypes()
        aDVD.setType(int(input("Enter a valid DVD Type: ")))
    elif editDVD == 3:
        newCost = float(input("What is the name of the new Cost? :"))
        aDVD.setCost(newCost)
    else:
        exit()
    return aDVD








