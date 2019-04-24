from Queue import *
from fileManager import *
from Processes import *
from FCFS import *

class main_memory:

    def __init__(self):
        self.memory = [0] * 4096
        self.mem_Used = 0
        self.mem_Left = 4096

    # need functions that:
    # 1. check if process can fit
    # 2. load process into open slots in memory
    # 3. remove process from memory once completed
    # 4. compaction - eliminate internal fragmentation to create bigger gap

    # (1) WORKING
    def process_fit(self,process):
        if int(process.getMem()) < self.mem_Left:
            return True
        else:
            print("false")
            return False
        
    # (2) WORKING
    def load_process(self,process):
        counter = 0
        temp_spot = 0 # temporary index for where process will be loaded
        largest_spot = 0 # current biggest consecutive chunk of free memory
        first_spot = 0 # where to insert process 
        for i in range(len(self.memory)):
            if self.memory[i] == 0:
                if counter == 0:
                    temp_spot = i
                counter +=1
            else:
                if counter > largest_spot:
                    largest_spot = counter
                    first_spot = temp_spot
                counter = 0
            
        if largest_spot < counter:
            largest_spot = counter
            first_spot = temp_spot
                
        if int(process.getMem()) <= largest_spot:
            #load starting at first_spot
            for i in range(int(process.getMem())):
                self.memory[first_spot+i] = process.getID()
        else:
        #perform compaction
            self.compaction()
        #recall load process
            self.load_process(process)

        self.mem_Used += int(process.getMem())
        self.mem_Left = 4096 - self.mem_Used

    # (3) WORKING
    def remove_process(self,process):
        ID = process.getID()
        for cell in self.memory:
            if cell == ID:
                index = self.memory.index(cell)
                self.memory[index] = 0

        self.mem_Used -= int(process.getMem())
        self.mem_Left += int(process.getMem())

    # (4) WORKING
    def compaction(self):
        temp_list = []
        for i in range(len(self.memory)):
            if self.memory[i] != 0:
                temp_list.append(self.memory[i])
        adder = 4096 - len(temp_list)
        for i in range(adder):
            temp_list.append(0)
        self.memory = temp_list

##def main():
##    MainMem = main_memory()
##    scheduler = Queue()
##    File_manager = filemanager("textfile.txt")
##    readyitems = File_manager.getReady_items()
##    notReadyItems = File_manager.getNot_Ready_items()
##    scheduler.multipush(readyitems)
##    scheduler.multipushWaiting(notReadyItems)
####    scheduler.userprint()
####    MainMem.process_fit(scheduler.items[0])
####    print(scheduler.items[1].getID())
##    MainMem.load_process(scheduler.items[1])
####    print(scheduler.items[2].getID())
##    MainMem.load_process(scheduler.items[2])
##    MainMem.remove_process(scheduler.items[1])
####    print(scheduler.items[1].getID())
##    MainMem.load_process(scheduler.items[1])
####    print(scheduler.items[0].getID())
##    MainMem.load_process(scheduler.items[0])
##    
##main()
        
