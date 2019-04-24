from Queue import *
from fileManager import *
from Processes import *
from FCFS import *

#file manager class           
class filemanager:
    
    def __init__(self, file):

        #empty list
        self.items = []
        self.ready_items = []
        self.not_ready_items = []
        #read file
        inputFile = open(file,"r")
        text = inputFile.readlines()

        #for items in the file
        for i in text:
            #split the items
            commaline = i.split(",")
            if self.verify(commaline):
                #append items seperately
                self.items.append(Processes(commaline))
            else:
                #else reject it
                print("Process "+str(commaline)+" rejected, invalid data")

        for item in self.items:
            if item.getArrivalTime() == 0:
                self.ready_items.append(item)
            else:
                self.not_ready_items.append(item)
                
            

        #list priority in order
##        for i in range(3, 0, -1):
##            for item in self.items:
##                #append to other empty list
##                if int(item.getPriority()) == i:
##                    self.sorted_items.append(item)

    #return the sorted items
    def getReady_items(self):
        return self.ready_items

    def getNot_Ready_items(self):
        return self.not_ready_items

    #verify if data is valid       
    def verify(self, commaline):
##        print(len(commaline))
        for i in range(len(commaline)):

            #checking is process id is valid
            if i == 0:
                try:
                    int(commaline[i])
                except ValueError:
                    return False
                if len(commaline[i]) != 4:
                    return False

##            #checking is priority is valid
##            if i == 1:
##                try:
##                    int(commaline[i])
##                except ValueError:
##                    return False
##                if int(commaline[i]) > 3 or int(commaline[i]) < 1:
##                    return False

            if i == 1:
                try:
                    int(commaline[i])
                except ValueError:
                    print('failed')
                    return False
                    
                if int(commaline[i]) <= 1:
                    print('failed')
                    return False

            if i == 2:
                try:
                    int(commaline[i])
                except ValueError:
                    print('failed')
                    return False
                    
                if int(commaline[i]) > int(commaline[i-1]):
                    print('failed')
                    return False

            if i == 3:
                try:
                    int(commaline[i])
                except ValueError:
                    print('failed')
                    return False
                    
                if int(commaline[i]) < 0:
                    print('failed')
                    return False

            if i == 4:
                try:
                    int(commaline[i])
                except ValueError:
                    print('failed')
                    return False
                    
                if int(commaline[i]) < 0:
                    print('failed')
                    return False
                
            if i == 5:
                try:
                    int(commaline[i])
                except ValueError:
                    print('failed')
                    return False
                    
                if int(commaline[i]) < 0:
                    print('failed')
                    return False

            #checking if user is valid
            if i == 6:
                if str(commaline[i]) !=  "pprigoda\n":
                    return False

            #checking the CPU cycles if not negative

        return True

        #sort items based on prioriy
        #multipush items
