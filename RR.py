from Queue import *
from fileManager import *
from Processes import *
from FCFS import *
from memoryQueue import *

class executor_rr:
    def __init__(self,queue, delta, CSP, I_O_Duration):
        self.service_array = []
        self.quantum = 0
        self.queue = queue
        self.memoryQueue = memoryQueue()
        self.delta = delta
        self.delta_counter = 0
        self.total_cycles = 0
        self.CSP = CSP
        self.CSP_Counter = 0
        self.I_O_Duration = I_O_Duration
        self.ID_array = []
        self.arrival_times = {}
        self.finishing_times = {}

    def address_waiting(self):
        #check if waiting items have reached their arrival time
        waiting = []
        
        for item in self.queue.waiting_items:
##            print(item.getID())
            if item.getArrivalTime() <= self.total_cycles:
                waiting.append(item)
                self.queue.enqueue(item)

                if True:
                    self.memoryQueue.enqueue(item)
                    self.queue.items.remove(item)
##                print('enqueue', self.total_cycles)
                              
        for item in waiting:        
            self.queue.waiting_items.remove(item)
        #self.queue.userprint()

    def find_service(self):
        if self.CSP_Counter > 0:
            print('CSP')
            self.CSP_Counter -= 1
            return False
        #check if the queue is empty
        if self.memoryQueue.isEmpty():
            print('empty memory')
            return False

        First_Process = self.memoryQueue.items[-1]

        if self.delta_counter >= self.delta:
            self.memoryQueue.enqueue(self.memoryQueue.dequeue())
            self.delta_counter = 0
            

        if self.memoryQueue.items[-1].I_O_Freq < 0:
            if self.memoryQueue.items[-1] != First_Process:
                self.CSP_Counter = self.CSP
                self.delta_counter = 0
                if self.CSP_Counter > 0:
                    self.CSP_Counter -= 1
                    return False
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
                self.memoryQueue.enqueue(self.memoryQueue.dequeue())
                
                #Loop through looking for a process not in IO:if you get back to the original process, give up.
                while (self.memoryQueue.items[-1] != First_Process) and (self.memoryQueue.items[-1].I_O_Counter > 0):
                    self.memoryQueue.items[-1].I_O_Counter = self.I_O_Duration
                    self.memoryQueue.enqueue(self.memoryQueue.dequeue())
                if self.memoryQueue.items[-1].I_O_Counter > 0:
                    return False
                
                #check if we loaded a new process due to IO events
                if self.memoryQueue.items[-1] != First_Process:
                    self.CSP_Counter = self.CSP
                    self.delta_counter = 0
                    if self.CSP_Counter > 0:
                        self.CSP_Counter -= 1
                        return False
                return True
                                       
        return True

    def calc_total_turnaround(self):
        total_waiting = 0
        for time in self.finishing_times:
            total_waiting += self.finishing_times.get(time) - self.arrival_times.get(time)
##        print('waiting total', total_waiting)
##        print('arrival', self.arrival_times)
##        print('finishing', self.finishing_times)
        
        return total_waiting

    def I_O_Maitenence(self):
        for item in self.memoryQueue.items:
            if item.I_O_Counter > 0:
                item.I_O_Counter -= 1
                if item.I_O_Counter == 0:
                    item.I_O_Freq = item.I_O_Freq * -1

    def initialize_memory(self):
        for item in self.queue.items:
            #placeholder for memory class checking if there is room in memory
            if True:
                self.memoryQueue.enqueue(item)
                self.queue.items.remove(item)

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

        self.delta_counter += 1

    def cpu_cycle_rr(self):       
        if not self.queue.isWaiting():
            #print(self.queue.items[-1].CPU_total)
            self.address_waiting()
        
        if self.find_service():
##                print('service found')
            self.serve()

        self.I_O_Maitenence()
            #count down I/O events & quantum
        self.total_cycles += 1
