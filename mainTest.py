from Queue import *
from memoryQueue import *
from fileManager import *
from Processes import *
from FCFS import *

def main():
    scheduler = Queue()
    fcfs_executor = executor_fcfs(scheduler, 2, 5)
    
    File_Manager = filemanager('textfile.txt')

    readyitems = File_Manager.getReady_items()
    notReadyItems = File_Manager.getNot_Ready_items()
    
    
    scheduler.multipush(readyitems)
    scheduler.multipushWaiting(notReadyItems)
    scheduler.userprint()

    while not scheduler.isEmpty():
        fcfs_executor.cpu_cycle_fcfs()
    scheduler.userprint()

main()
