# Operating Systems - Section 1
# Team 4: Abe Lusk, Christian Murphy, PT Prigoda, Jess Quint, & Victoia Slater
# Phase 2
# October 31, 2018


# import tools needed to preform specifically coded python functions
from graphics import *
from time import *
from random import *
from Queue import *
from fileManager import *
from Processes import *
from FCFS import *
from RR import *
from SPN import *
from SRT import *


def get_throughput(numProc, totCyc, numCyc):
    throughput = (numProc/totCyc)*numCyc
    return throughput

def draw_output(gwin, array, IDarray, totalP):
##def draw_output(gwin, array, totalP):
    # This function will display a simulation of the running CPU in the GUI
    # It will order the processes based on arrival time and then it will display how each is served

    # draw the x and y axis that outline the graph
    yLine = Rectangle(Point(80,70), Point(81,470))
    yLine.draw(gwin)
    xLine = Rectangle(Point(80,70), Point(660,71))
    xLine.draw(gwin)

    # variable that represents total number of processes
    numProcesses = totalP
    # variable for tatring y position of first process ID number
    count = 120

    # space out the process ID numbers as they are drawn to the screen, and draw them
    for i in range(len(IDarray)):
        process = Text(Point(50,count), str(IDarray[i]))
        count = count + 50
        process.draw(gwin)
##    for i in range(1,totalP+1):
##        process = Text(Point(50,count), str(i))
##        count = count + 50
##        process.draw(gwin)

    # array for storing the heights where each bar should appear on the window
    heightsList = []
    # starting height values for top and bottom of the first bar
    topy = 110
    bottomy = 130
    # loop through the number of processes, and assign y values for each process bar
    for i in range(1,totalP+1):
        ptHeight = [topy,bottomy]
        topy += 50
        bottomy += 50
        heightsList.append(ptHeight)

    # draw bars to simulate the scheduling of all processes until completion of all processes
    # length each bar should be so that the entire simulation fits within the space dedicated in the GUI

    total_blocks = 0
    total_IO = 0
    for x in array:
        if x >= 0:
            total_blocks += 1
        else:
            total_IO += 1
    
##    blocksize = (580-(total_IO))//total_blocks
    blocksize = 580//total_blocks
    # starting x-values for first process that is served
    counter1 = 80
    counter2 = 81
    
    # loop through array that hops which process was served during each block of time
    for i in range(len(array)):
        # for each entry array[i] i would be the acitve process
        activeProcess = array[i]
##        print(activeProcess)
        if activeProcess < 0:
            activeProcess = abs(activeProcess)
            newBar = Rectangle(Point(counter1+1, heightsList[activeProcess-1][0]), Point(counter2+1, heightsList[activeProcess-1][1]))
            newBar.draw(gwin)
            newBar.setOutline('red')
            counter1 += 2
            counter2 += 2
        else:
            activeProcess = abs(activeProcess)
            # fill in the block until it is the length of one block of time
            for j in range(blocksize):
                newBar = Rectangle(Point(counter1+j, heightsList[activeProcess-1][0]), Point(counter2+j, heightsList[activeProcess-1][1]))
                newBar.draw(gwin)
                newBar.setOutline('light blue')
            # increment x value so next process bar starts where the last left off
            counter1 += blocksize
            counter2 += blocksize

#from COM 110 programming assingment 3
def drawButton(gwin, pt1, pt2, words, col, txtCol):
    button1=Rectangle(pt1, pt2)
    button1.setFill(col)
    button1.setOutline(col)
    button1.draw(gwin)
    #Put label on button
    button1Label = Text(Point((pt1.getX()+pt2.getX())/2, (pt1.getY()+pt2.getY())/2), words)
    button1Label.setFill(txtCol)
    button1Label.draw(gwin)

#from COM 110 programming assingment 4
def inputBox(gwin,height,instruct): #create input boxes
    #height controls how high up or how low down on the graphic window
    #   the input box is drawn
    #instruct is a text object to be drawn to the left of the input box
    #   instruct tells user what to enter in each input box
    #1.create text object for the prompt
    prompt=Text(Point(780,height),instruct)
    prompt.setSize(12)
    prompt.draw(gwin)
    #2.create entry object for the input box
    inputBox=Entry(Point(885,height),20)
    inputBox.setFill("white")
    inputBox.draw(gwin)
    #3. return the inputBox to main function so we can use its stored info later
    return inputBox

def drawTable(win, processID, serviceTime, arrivalTime, ioFrequency):
    actualID = Text(Point(1040, 130), processID)
    actualID.setSize(10)
    actualID.draw(win)
    actualArrival = Text(Point(1095, 130), arrivalTime)
    actualArrival.setSize(10)
    actualArrival.draw(win)
    actualService = Text(Point(1147, 130), serviceTime)
    actualService.setSize(10)
    actualService.draw(win)
    actualFreq = Text(Point(1199, 130), ioFrequency)
    actualFreq.setSize(10)
    actualFreq.draw(win)


def drawTable2(win, text):
    y = 130
    for x in text:
        x = x.split(',')
        actualID = Text(Point(1040, y), x[0])
        actualID.setSize(10)
        actualID.draw(win)
        actualArrival = Text(Point(1095, y), x[4])
        actualArrival.setSize(10)
        actualArrival.draw(win)
        actualService = Text(Point(1147, y), x[1])
        actualService.setSize(10)
        actualService.draw(win)
        actualFreq = Text(Point(1199, y), x[3])
        actualFreq.setSize(10)
        actualFreq.draw(win)
        y = y + 30

def runEverything(win):

    #Buttons
    #exit button
    drawButton(win, Point(1220,10), Point(1240,30), "x", "red", "white")
    #reset button
    drawButton(win, Point(1170,10), Point(1210,30), "reset", "grey", "black")
    #Run button
    #   either first 5 input boxs are non empty or everything but last is empty
    #   run fcfs or rr algorithm
    drawButton(win, Point(740,470), Point(950,490), "ADD PROCESS", "grey", "black")
##    drawButton(win, Point(850,470), Point(950,490), "RUN RR", "grey", "black")
    #Run Test Data Set FCFS
    drawButton(win, Point(710,190), Point(840,210), "FCFS", "grey", "black")
    #Run Test Data Set RR
    drawButton(win, Point(850,190), Point(980,210), "RR", "grey", "black")
    #Run FCFS class data
    drawButton(win, Point(710,220), Point(840,240), "SPN", "grey", "black")
    #Run RR class data
    drawButton(win, Point(850,220), Point(980,240), "SRT", "grey", "black")
    
    #Define input area
    inputArea = Rectangle(Point(710,250),Point(980,500))
    inputArea.setOutline("black")
    inputArea.draw(win)
    #Get inputs
    inputID=inputBox(win,280,"Process ID: ")
    inputUser=inputBox(win,310,"Username: ")
    inputArrive=inputBox(win,340,"Arrival Time: ")
    inputServe=inputBox(win,370,"Service Time: ")
    inputIOFreq=inputBox(win,400,"I/O Frequency: ")
    #or
    inputTXT=inputBox(win,430,"Data Set: ")

    #space to show algorithm completion
    output = Rectangle(Point(20,40),Point(690,500))
    output.setOutline("black")
    output.draw(win)

    #space to show clock cycles
    clock = Rectangle(Point(710,40),Point(980,180))
    clock.setOutline("black")
    clock.draw(win)
    clockPrompt=Text(Point(845,70),"CPU Cycles")
    clockPrompt.setSize(24)
    clockPrompt.draw(win)

    #space to print out user errors
    errors = Rectangle(Point(20,510),Point(980,590))
    errors.setOutline("black")
    errors.draw(win)
    erPrompt=Text(Point(110,520),"")
    erPrompt.setSize(12)
    erPrompt.draw(win)
    # create text object to display errors or throughput
    errorList = Text(Point(360,545), "")
    errorList.draw(win)
    # create text object to finishing times
    finishings = Text(Point(360, 540), "")
    finishings.draw(win)
    # create text object to throughput time
    throughput = Text(Point(360, 565), "")
    throughput.draw(win)
    # create text object to turnaround time
    turnaround = Text(Point(360, 580), "")
    turnaround.draw(win)

    #create empty box to be filled in representing data set
    tableBox = Rectangle(Point(1000,40), Point(1235,365))
    tableBox.draw(win)
    tableTitle = Text(Point(1117,70),"Data Set")
    tableTitle.setSize(24)
    tableTitle.draw(win)
    idText = Text(Point(1040,100),"Process ID")
    idText.setSize(10)
    idText.draw(win)
    arrivalText = Text(Point(1095,100),"Arrival \n Time")
    arrivalText.setSize(10)
    arrivalText.draw(win)
    serviceText = Text(Point(1147,100),"Service \n Time")
    serviceText.setSize(10)
    serviceText.draw(win)
    ioText = Text(Point(1199,100),"I/O Freq")
    ioText.setSize(10)
    ioText.draw(win)
    tableLine = Rectangle(Point(1010,115),Point(1225,115))
    tableLine.draw(win)
    x = 1070
    for i in range(3):
        tableDivider = Rectangle(Point(x, 95), Point(x, 355))
        tableDivider.draw(win)
        x = x + 50
        
    #Display CPU cycles
    timer=Text(Point(845,110),"")
    timer.setSize(24)
    timer.draw(win)


    teamLogo = Image(Point(1125,500), "newlogo.gif")
    teamLogo.draw(win)

    # get user click stored in a variable to later take x and y values
    pt = win.getMouse()


    # make program continue to run until user clicks within exit button
    while not(pt.getX()>=1220 and pt.getX()<=1240 and pt.getY()>=10 and pt.getY()<=30):

        #if user clicks the reset button
        #   reset screen so they can choose to run something different
        if pt.getX()>=1170 and pt.getX()<=1210 and pt.getY()>=10 and pt.getY()<=30:
            erPrompt.setText("")
            errorList.setText("")
            finishings.setText("")
            throughput.setText("")
            turnaround.setText("")
            timer.setText("")
            block2 = Rectangle(Point(30,60), Point(680,500))
            block2.setFill('white')
            block2.setOutline('white')
            block2.draw(win)
            block3 = Rectangle(Point(1000,40), Point(1235,365))
            block3.setFill('white')
            block3.setOutline('white')
            block3.draw(win)
            runEverything(win)
            return print("reset")
            ###########################
            

        #if user clicks ADD PROCESS
        elif pt.getX() >=740 and pt.getX()<=950 and pt.getY()>=470 and pt.getY()<=490:
            erPrompt.setText("")
            errorList.setText("")
            finishings.setText("")
            throughput.setText("")
            turnaround.setText("")

            # if the user is trying to add an individual process
            if (inputID.getText() != "" and inputUser.getText() !="" and inputArrive.getText() !="" and inputServe.getText() !="" and inputIOFreq.getText() !="" and inputTXT.getText() == ""):
                
                #check validity of inputs for a new process
                check1 = False
                #check validity of inputed process ID i.e. it is an int of four digits
                while check1 == False:
                    check1 = True
                    #get the input
                    processID = inputID.getText()
                    length = len(processID)
                    #check if each character's ASCII value is within the values of the single digit integers
                    for i in range(length):
                        num = ord(processID[i])
                        if num<48 or num>57:
                            check1=False
                    if check1 == False:
                        erPrompt.setText("The following errors have occured: ")
                        errorList.setText("Error ID, numbers only")
                    else:
                        #check if the input is of length 4
                        if length != 4:
                            check1 = False
                            erPrompt.setText("The following errors have occured: ")
                            errorList.setText("Error iD, not 4 digits")

                # check the validity of the service time i.e. service time is an integer
                check3 = False
                while check3 == False:
                    check3 = True
                    serviceTime = inputServe.getText()
                    length = len(serviceTime)
                    #check if each character's ASCII value is within the values of the single digit integers
                    for i in range(length):
                        num = ord(serviceTime[i])
                        if num<48 or num>57:
                            check3 = False
                    if check3 == False:
                        erPrompt.setText("The following errors have occured: ")
                        errorList.setText("Error Service †ime, must be an integer")

                # check the validity of the I/O Frequency i.e. I/O freq is an integer
                check5 = False
                while check5 == False:
                    check5 = True
                    ioFrequency = inputIOFreq.getText()
                    length = len(ioFrequency)
                    for i in range(length):
                        num = ord(ioFrequency[i])
                        if num<48 or num>57:
                            check5 = False
                    if check5 == False:
                        erPrompt.setText("The following errors have occured: ")
                        errorList.setText("Error IO Freq, must be an integer")

                # check the validity of the arrival time i.e. arrival time must be an integer
                check6 = False
                while check6 == False:
                    check6 = True
                    arrivalTime = inputArrive.getText()
                    length = len(arrivalTime)
                    for i in range(length):
                        num = ord(arrivalTime[i])
                        if num<48 or num>57:
                            check6 = False
                    if check6 == False:
                        erPrompt.setText("The following errors have occured: ")
                        errorList.setText("Error Arrival Time, must be an integer")

                processUsername = inputUser.getText()                       
                #create queue class instance
                drawTable(win, processID, serviceTime, arrivalTime, ioFrequency)
                scheduler = Queue()
                #create array to pass to be made into a process object
                newProcess = [str(processID), str(serviceTime), "0", str(ioFrequency), str(arrivalTime), processUsername]
                #create new process object and add it to the queue
                scheduler.enqueue(Processes(newProcess))

            else:
                #print error message if user input is not valid
                errorList.setText("Please fill in the first five input boxes with valid parameters.")

        #if user clicks SPN
        elif pt.getX() >=710 and pt.getX()<=840 and pt.getY()>=220 and pt.getY()<=240:
            erPrompt.setText("")
            errorList.setText("")
            finishings.setText("")
            throughput.setText("")
            turnaround.setText("")

            #create file manager
            scheduler = Queue()
            spn_executor = executor_SPN(scheduler, 0, 5)
            
            File_Manager = filemanager(inputTXT.getText())

            #call fucntions
            readyitems = File_Manager.getReady_items()
            notReadyItems = File_Manager.getNot_Ready_items()
            
            
            scheduler.multipush(readyitems)
            scheduler.multipushWaiting(notReadyItems)

            scheduler.userprint()

            totalProcesses = scheduler.total_Length()

            while not scheduler.isEmpty() or not scheduler.isWaiting() or not spn_executor.Stack.isEmpty():
                spn_executor.cpu_cycle_SPN()
                timer.setText(spn_executor.get_total_cycles())
            scheduler.userprint()           
##            print('done2')
            
            inputFile = open(inputTXT.getText(),"r")
            text = inputFile.readlines()
            
            drawTable2(win, text)
            id_array, array = spn_executor.curate_data()

            #array = fcfs_executor.get_array()
            #id_array = fcfs_executor.get_ID_array()
            
            draw_output(win,array,id_array,totalProcesses)

            count = 1
            erPrompt.setText("")
            finishings.setText("Finishing Times: "+str(spn_executor.finishing_times))
            throughput.setText("The throughput for this execution was "+str(get_throughput(totalProcesses, spn_executor.get_total_cycles(), count))+" processes completed per "+str(count)+" CPU cycles.")
            turnaround.setText("The average turnaround time for this execution was "+(str(spn_executor.calc_total_turnaround() / totalProcesses)+" cycles."))

##################################################################################
            
        #if user clicks SRT
        elif pt.getX() >=850 and pt.getX()<=980 and pt.getY()>=220 and pt.getY()<=240:
            erPrompt.setText("")
            errorList.setText("")
            finishings.setText("")
            throughput.setText("")
            turnaround.setText("")

            #create file manager
            scheduler = Queue()
            srt_executor = executor_SRT(scheduler, 0, 5)
            
            File_Manager = filemanager(inputTXT.getText())

            #call fucntions
            readyitems = File_Manager.getReady_items()
            notReadyItems = File_Manager.getNot_Ready_items()
            
            
            scheduler.multipush(readyitems)
            scheduler.multipushWaiting(notReadyItems)

            scheduler.userprint()

            totalProcesses = scheduler.total_Length()

            while not scheduler.isEmpty() or not scheduler.isWaiting() or not srt_executor.Stack.isEmpty():
                srt_executor.cpu_cycle_SRT()
                timer.setText(srt_executor.get_total_cycles())
            scheduler.userprint()           
##            print('done2')
            
            inputFile = open(inputTXT.getText(),"r")
            text = inputFile.readlines()
            
            drawTable2(win, text)
            id_array, array = srt_executor.curate_data()

            #array = fcfs_executor.get_array()
            #id_array = fcfs_executor.get_ID_array()
            
            draw_output(win,array,id_array,totalProcesses)

            count = 1
            erPrompt.setText("")
            finishings.setText("Finishing Times: "+str(srt_executor.finishing_times))
            throughput.setText("The throughput for this execution was "+str(get_throughput(totalProcesses, srt_executor.get_total_cycles(), count))+" processes completed per "+str(count)+" CPU cycles.")
            turnaround.setText("The average turnaround time for this execution was "+(str(srt_executor.calc_total_turnaround() / totalProcesses)+" cycles."))

##################################################################################

        #if user clicks FCFS 
        elif pt.getX() >=710 and pt.getX()<=840 and pt.getY()>=190 and pt.getY()<=210:
            erPrompt.setText("")
            errorList.setText("")
            finishings.setText("")
            throughput.setText("")
            turnaround.setText("")

            #set up queue
            scheduler = Queue()
            #set up instance of executor that will run fcfs algorithm
            fcfs_executor = executor_fcfs(scheduler, 0, 5)

            #get file from input box and manage file by checking validity and creating process objects
            File_Manager = filemanager(inputTXT.getText())

            #call fucntions to get our lists of ready and waiting items
            readyitems = File_Manager.getReady_items()
            notReadyItems = File_Manager.getNot_Ready_items()
            
            #push ready and waiting items into appropriate queues
            scheduler.multipush(readyitems)
            scheduler.multipushWaiting(notReadyItems)

##                scheduler.userprint()

            #used for drawing in the GUI
            totalProcesses = scheduler.total_Length()

            #run algorithm until both the ready queue and the waiting queue are empty
            #   i.e. all processes have been served
            #   display clock cycles as algorithm runs
            while not scheduler.isEmpty() or not scheduler.isWaiting():
                fcfs_executor.cpu_cycle_fcfs()
                timer.setText(fcfs_executor.get_total_cycles())
            #scheduler.userprint()           
##                print('done')

            #once algorithm completes, display how a simulation of how the algorithm ran

            inputFile = open(inputTXT.getText(),"r")
            text = inputFile.readlines()
            
            drawTable2(win, text)
            
            array = fcfs_executor.get_array()
            id_array = fcfs_executor.get_ID_array()
            draw_output(win,array,id_array, totalProcesses)

            count = 1
            erPrompt.setText("")
            finishings.setText("Finishing Times: "+str(fcfs_executor.finishing_times))
            throughput.setText("The throughput for this execution was "+str(get_throughput(totalProcesses, fcfs_executor.get_total_cycles(), count))+" processes completed per "+str(count)+" CPU cycles.")
            turnaround.setText("The average turnaround time for this execution was "+(str(fcfs_executor.calc_total_turnaround() / totalProcesses)+" cycles."))
                
        #if user clicks RR
        elif pt.getX() >=850 and pt.getX()<=980 and pt.getY()>=190 and pt.getY()<=210:
            erPrompt.setText("")
            errorList.setText("")
            finishings.setText("")
            throughput.setText("")
            turnaround.setText("")

            #create file manager
            scheduler = Queue()
            rr_executor = executor_rr(scheduler, 2,0, 5)
            
            File_Manager = filemanager(inputTXT.getText())

            #call fucntions
            readyitems = File_Manager.getReady_items()
            notReadyItems = File_Manager.getNot_Ready_items()
            
            
            scheduler.multipush(readyitems)
            scheduler.multipushWaiting(notReadyItems)

##                scheduler.userprint()

            totalProcesses = scheduler.total_Length()

            while not scheduler.isEmpty() or not scheduler.isWaiting():
                rr_executor.cpu_cycle_rr()
                timer.setText(rr_executor.total_cycles)
            #scheduler.userprint()           
##                print('done')
            inputFile = open(inputTXT.getText(),"r")
            text = inputFile.readlines()
            
            drawTable2(win, text)
            
            array = rr_executor.daddyList
            id_array = rr_executor.IDarray
            draw_output(win,array,id_array,totalProcesses)

            count = 1
            erPrompt.setText("")
            finishings.setText("Finishing TImes: "+str(rr_executor.finishing_times))
            throughput.setText("The throughput for this execution was "+str(get_throughput(totalProcesses, rr_executor.total_cycles, count))+" processes completed per "+str(count)+" CPU cycles.")
            turnaround.setText("The average turnaround time for this execution was "+(str(rr_executor.calc_total_turnaround() / totalProcesses)+" cycles."))            
            
    # close graphic window
        pt = win.getMouse()
    win.close()

def main():

    #create GUI Window
    WIDTH=1250
    HEIGHT=600
    gwin = GraphWin("Team 4 Phase 3", WIDTH, HEIGHT)

    runEverything(gwin)

main()
