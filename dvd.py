##########################################################
#   CS217:      DVD Class
#   Assignment: Lab 2
#   Author:     James Burch
#   Date:       10/27/2016
#   Filename:   dvd.py
#   Purpose:    Modelling DVD Objects
##########################################################
from lab2GlobalFunctions import *


DVD_Types = ["Game", "Word", "Compiler", "Spreadsheet",
                 "Dbase", "Presentation", "None"]
class DVD:

    def __init__(self, InTitle, InDVDType="None", InCost=0.0):
        
        #Validating Title
        if len(InTitle) > 0:
            self.__Title = InTitle
        else:
            while not len(InTitle) > 0:
                InTitle = input("Invalid title -- re-enter: ")
            self.__Title = InTitle
            
        # Validation DVD Type
        if InDVDType in DVD_Types:
            self.__DVDType = InDVDType
        else:
            print("Invalid DVD Type")
            DVD_Type_Num = 0
            while not 1 <= DVD_Type_Num <= len(DVD_Types):
                self.listValidDVDTypes()
                DVD_Type_Num = int(input("Enter number of valid DVD type: "))
            self.__DVDType = DVD_Types[DVD_Type_Num - 1]
            
        # Validating Cost
        if InCost >= 0.0:
            self.__Cost = InCost
        else:
            while not InCost >= 0:
                InCost = float(input("Invalid cost -- re-enter cost (>= 0.0): "))
            self.__Cost = InCost

    def setTitle(self, newTitle):
        self.__Title = newTitle if len(newTitle) > 0 else self.__Title

    def getTitle(self):
        return self.__Title

    def setType(self, newType):
        if newType == 1:
            self.__DVDType = DVD_Types[0]
        elif newType == 2:
            self.__DVDType = DVD_Types [1]
        elif newType == 3:
            self.__DVDType = DVD_Types[2]
        elif newType == 4:
            self.__DVDType = DVD_Types[3]
        elif newType == 5:
            self.__DVDType = DVD_Types[4]
        elif newType == 6:
            self.__DVDType = DVD_Types[5]
        elif newType == 7:
            self.__DVDType = DVD_Types[6]
        else:
            print("Invalid DVD Type")
            DVD_Type_Num = 0
            while not 1 <= DVD_Type_Num <= len(DVD_Types):
                self.listValidDVDTypes()
                DVD_Type_Num = int(input("Enter number of valid DVD type: "))
            self.__DVDType = DVD_Types[DVD_Type_Num - 1]

    def getType(self):
        return self.__DVDType

    def setCost(self, newCost):
        self.__Cost = newCost if newCost >= 0.0 else self.__Cost

    def getCost(self):
        return self.__Cost




    # Support method listing valid DVD Types
    def listValidDVDTypes(self):
        print("\nValid DVD types are:")
        for num in range(len(DVD_Types)):
            print(num + 1, '\t', DVD_Types[num])

    def loadInformation(self):
        self.__Title = "Unknown"
        self.setTitle(input("Enter the title of this DVD: "))
        self.listValidDVDTypes()
        self.setType(int(input("Enter a valid DVD Type: ")))
        self.__Cost = 0.0
        self.setCost(float(input("Enter the cost of this DVD: $")))

if __name__ == '__main__':
    aDVD = DVD("Myst", "Game", 32.95)
    # badDVD = DVD("", "Honda", -32.45)
    anotherDVD = DVD("Python is Fun!")
    print("anotherDVD's title is:", anotherDVD.getTitle())
    print("anotherDVD's type is:", anotherDVD.getType())
    print("anotherDVD's cost is: $", anotherDVD.getCost(), sep='')
    anotherDVD.setTitle("Python is NOT fun!")
    anotherDVD.setType("Compiler")
    anotherDVD.setCost(100.00)
    print("anotherDVD's title is:", anotherDVD.getTitle())
    print("anotherDVD's type is:", anotherDVD.getType())
    print("anotherDVD's cost is: ${:.2f}".format(anotherDVD.getCost()), sep='')






               
