########################################
# CS217: Modelling a DVD
# Assignment: Lab 2
# Author: James Burch
# Date: 11/07/2016
# File Name: Lab 2.py
# Purpose: Modeling DVD by there there different attributes using Object Oriented programming
########################################

# imports (if any)
#from dvd import DVD
from lab2GlobalFunctions import *






def main():

    
    DVD1 = DVD("Final Fantasy", "Game", 59.99)
    DVD2 = DVD("CPR Training", "Presentation", 19.99)
    DVD3 = DVD("Avatar", "None", 24.99)

    listDVD = [DVD1, DVD2, DVD3]

    #for i in range(len(listDVD)):
    #    print(listDVD[i].getTitle())

    #Display_DVD_Information_From_List(listDVD)

    Display_DVD_Information(DVD1, DVD2, DVD3)














    
    '''
    Display_DVD_Information(DVD1, DVD2, DVD3)
    DVD1.loadInformation()
    DVD2.loadInformation()
    DVD3.loadInformation()
    Display_DVD_Information(DVD1, DVD2, DVD3)
    DisplayTotalAndAverageCosts(DVD1, DVD2, DVD3)
    ChangeDVD(DVD1)
    ChangeDVD(DVD2)
    Display_DVD_Information(DVD1, DVD2, DVD3)
    DisplayTotalAndAverageCosts(DVD1, DVD2, DVD3)
    '''
main()



