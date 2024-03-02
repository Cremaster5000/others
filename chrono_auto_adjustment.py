from datetime import datetime 
from os import system 
import time
"""In this script we run a chronometer litle function that can take diferent time of execution
on diferent CPU or enviroment, so the main purpose of this is to do litle adjusment in order to get
more acurate meassure of time"""
wait = 0.005 #variable used to set the time script is gonna wait during execution

def runChrono(run):
        minu = 0 #we set at zero individually minuts
        sec = 0  #seconds
        mili = 0 #and miliseconds
        while sec < run: #run is the total secons we are gonna run the chronometer
            system('clear')
            time_chrono = f"{minu:02d}:{sec:02d}:{mili:02d}" #using a fstring to 
            print(time_chrono)  #print it like a clock format          
            time.sleep(wait)
            mili += 1 #every loop we add one milisecond to the count
            if mili >= 100: #as we only use 2 digits on milisecond we only count to 100
                mili = 0
                sec += 1
            if sec >= 60: 
                minu+= 1 
                sec = 0
            if minu >= 60:
                minu = 0
            
run = 4
results = [] #this is important to verify the auto adjustment
init = datetime.now() #the first time we measure time of execution
runChrono(run)
passed_time = datetime.now()-init #total time executing the function
results.append(f"passed_time: {passed_time} ,wait:{wait}")
while passed_time.seconds != run:
    if passed_time.seconds > run: wait -= 0.0001 #little adjustment
    else: wait += 0.0001 #looking for fine tuning
    init = datetime.now() #on every loop we measure time of execution
    runChrono(run)
    passed_time = datetime.now()-init
    results.append(f"passed_time:{passed_time}, wait:{wait}")
print(results)
    
