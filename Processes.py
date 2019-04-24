from Queue import *
from fileManager import *
from Processes import *
from FCFS import *

#processes class           
class Processes:
    def __init__(self, process_data):

        self.data = process_data
        self.ID = process_data[0]
##        self.priority = process_data[1]
        self.CPU_cycles = int(process_data[1])
        self.CPU_total = int(process_data[2])
        self.I_O_Freq = int(process_data[3])
        self.arrival_time = int(process_data[4])
        self.name = process_data[6]
        self.mem = process_data[5]
        self.I_O_Counter = 0
        
        #data verification

        #variables

    #return name
    def getName(self):
        return self.name

    def getMem(self):
        return self.mem

    #return ID
    def getID(self):
        return self.ID

    #return data
    def getData(self):
        return self.data

##    #retur priority
##    def getPriority(self):
##        return self.priority

    def getCPU_cycles(self):
        return self.CPU_cycles
    
    def getCPU_total(self):
        return self.CPU_total

    def getArrivalTime(self):
        return self.arrival_time

    def getI_O_Freq(self):
        return self.I_O_Freq

    def getI_O_Counter(self):
        return self.I_O_Counter
