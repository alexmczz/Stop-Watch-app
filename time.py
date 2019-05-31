import time
import datetime

class Clock():
    def __init__(self, s):
        self.seconds = s
    
    def cal(self):
        now = datetime.datetime.now()
        print("Current date and time: ")
        print (now.strftime("%Y-%m-%d %H:%M"))

     
    def timer(self):
        while True:
            try:
                #promps user number of seconds.
                entry = input("Press any Character to quit. Type Seconds to Start: ")
                seconds = int(entry)
                

                #if user presses q program will stop
                if seconds < 0:
                    print("Seconds must be greater than 0")
                else:
                    
                    while seconds > -1:

                        #waits 1 second between each Int
                        time.sleep(1)

                        #prints out each Int
                        print("{}".format(seconds))

                        #Subtracts 1 per second until 0
                        seconds -= 1
                        
                    print("Times Up!")
                    print(clock.cal())
            except ValueError:
                print("Good Bye!")
                break

    
clock = Clock(0)
clock.timer()
