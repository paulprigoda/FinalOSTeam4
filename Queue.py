from Queue import *
from fileManager import *
from Processes import *
from FCFS import *

class Queue:
    def __init__(self):
        self.items = []
        self.waiting_items = []

    #returns if queue is empty
    def isEmpty(self):
        return self.items == []

    def isWaiting(self):
        return self.waiting_items == []

    #adds itme to queue
    def enqueue(self, item):
        self.items.insert(0,item)

    def enqueueWaiting(self, item):
        self.waiting_items.insert(0,item)

    #takes out item in queue
    def dequeue(self):
        return self.items.pop()

    #returns the legnth of queue
    def size(self):
        return len(self.items)

    def total_Length(self):
        return len(self.items) + len(self.waiting_items)

    #prints out all items in the queue
    def userprint(self):
        print("The active list of processes are:")
        #creates an output file of active processes
        outputfile = open("outputfile.txt", "w")
        for i in range(len(self.items), 0, -1):
            #writes to output file
            print(self.items[i-1].getData(), file = outputfile)
            #writes to outputfile in shell
##            print(self.items[i-1].getData())

    #prints out all items in the queue
    def userprintwaiting(self):
        print("The list of waiting processes are:")
        #creates an output file of active processes
        for i in range(len(self.waiting_items), 0, -1):
            #writes to outputfile in shell
            print(self.waiting_items[i-1].getData())
                       

    #pushes all items from data into queue
    def multipush(self, items):
        for i in items:
            self.enqueue(i)

    def multipushWaiting(self, items):
        for i in items:
            self.enqueueWaiting(i) 
