from Queue import *
from memoryQueue import *
from fileManager import *
from Processes import *
from FCFS import *

class executor_fcfs:
    #things to add: context switch penalty
    #I/O events
    #I/O freq

    #TO do: check if there is an i/o event--integer divis of total served
    #if there is then move on to the next, add CSP
    
    def __init__(self, queue, CSP, I_O_Duration):
        self.total_cycles = 0
        #pass the queue
        #for loops that counts up, once its higher than the CPU cycle number
        self.ID_array = []
        self.service_array = []
        self.I_O_Events = []
        self.queue = queue
        self.memoryQueue = memoryQueue()
        self.CSP = CSP
        self.I_O_Duration = I_O_Duration
        self.arrival_times = {}
        self.finishing_times = {}
        self.CSP_Counter = 0

    def readyToServe(self):
        if self.CSP_Counter > 0:
            print('CSP')
            self.CSP_Counter -= 1
            return False
        #check if the queue is empty
        if self.memoryQueue.isEmpty():
            print('empty memory')
            return False

        First_I_O = self.memoryQueue.items[-1]

        if self.memoryQueue.items[-1].I_O_Freq < 0:
            self.memoryQueue.items[-1].I_O_Freq = self.memoryQueue.items[-1].I_O_Freq * -1
            return True

        if self.memoryQueue.items[-1].CPU_total == 0:
            return True

        #check if there will be any I/O events
        if self.memoryQueue.items[-1].I_O_Freq != 0:
            #see if there will be an i/o event one in the future
            if (self.memoryQueue.items[-1].CPU_total)%self.memoryQueue.items[-1].I_O_Freq == 0:
                print('i/o')
                if self.memoryQueue.items[-1].I_O_Counter == 0:
                    self.memoryQueue.items[-1].I_O_Counter = self.I_O_Duration
                    self.ID_array.append(str(int(self.memoryQueue.items[-1].ID)*-1))
                    print(ID_array)
                self.memoryQueue.enqueue(self.memoryQueue.dequeue())
                
                #Loop through looking for a process not in IO:if you get back to the original process, give up.
                while (self.memoryQueue.items[-1] != First_I_O) and (self.memoryQueue.items[-1].I_O_Counter > 0):
                    self.memoryQueue.items[-1].I_O_Counter = self.I_O_Duration
                    self.memoryQueue.enqueue(self.memoryQueue.dequeue())
                if self.memoryQueue.items[-1].I_O_Counter > 0:
                    return False
                
                #check if we loaded a new process due to IO events
                if self.memoryQueue.items[-1] != First_I_O:
                    self.CSP_Counter = self.CSP
                    if self.CSP_Counter > 0:
                        self.CSP_Counter -= 1
                        return False
                return True
                                       
        return True

    def address_waiting(self):
        #check if waiting items have reached their arrival time
        waiting = []
        
        for item in self.queue.waiting_items:

            if item.getArrivalTime() <= self.total_cycles:
                waiting.append(item)
                self.queue.enqueue(item)
                #placeholder True for if there is memory available                                       
                if True:
                    print('new item in')
                    self.memoryQueue.enqueue(item)
                    self.queue.items.remove(item)
                
                              
        for item in waiting:
            self.queue.waiting_items.remove(item)

    def I_O_Maitenence(self):
        for item in self.memoryQueue.items:
            print(item.I_O_Counter)
            if item.I_O_Counter > 0:
                item.I_O_Counter -= 1
                if item.I_O_Counter == 0:
                    print('freq flipped')
                    item.I_O_Freq = item.I_O_Freq * -1

    def serve(self):
        if self.memoryQueue.items[-1].getID() not in self.ID_array:
            self.ID_array.append(self.memoryQueue.items[-1].getID())

        self.memoryQueue.items[-1].CPU_total += 1
        self.service_array.append(self.memoryQueue.items[-1].getID())

        print(self.memoryQueue.items[-1].ID, self.memoryQueue.items[-1].CPU_total)

        if self.memoryQueue.items[-1].CPU_total >= self.memoryQueue.items[-1].CPU_cycles:
                
            self.finishing_times[self.memoryQueue.items[-1].getID()] = self.total_cycles+1
            self.arrival_times[self.memoryQueue.items[-1].getID()] = self.memoryQueue.items[-1].getArrivalTime()

            self.memoryQueue.dequeue()
            self.CSP_Counter = self.CSP

            #remove this process from our memory database
            #then see if new processes can be loaded into memory
            
    def initialize_memory(self):
        for item in self.queue.items:
            #placeholder for memory class checking if there is room in memory
            if True:
                self.memoryQueue.enqueue(item)
                self.queue.items.remove(item)
                
    def cpu_cycle_fcfs(self):
        if not self.queue.isWaiting():
            self.address_waiting()

        if self.readyToServe():
            self.serve()

        self.I_O_Maitenence()

        self.total_cycles += 1
