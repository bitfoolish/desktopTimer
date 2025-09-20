import tkinter as tk
#import time
from plyer import notification
from playsound import playsound

class Timer:
    def __init__(self):
        self.window = tk.Tk() 
        self.window.config(bg="#9B3B34") # background colour for timer app
        self.window.geometry('300x200')

        self.minsRqst=tk.IntVar() #
        self.secsRqst=tk.IntVar()

#        self.minsRqst.set()
 #       self.secsRqst.set(1)

        self.welcome = tk.Label(text="Please enter your desired time below", fg="black") # Welcome message to user at top of program

        # when user clicks button it will begin the timer
        self.startButton = tk.Button( 
            text="Start Timer",
            width=25,
            height=5,
            bg="blue",
            fg="yellow",
            command=self.startTimer
        )

        # user may click this button to exit the program at any time
        self.terminateProgram = tk.Button( 
            text="Exit program",
            bg="grey",
            fg="yellow",
            command=self.window.destroy
        )

        self.userTimerName = tk.StringVar()

        self.nameTimer = tk.Entry(
            textvariable=self.userTimerName,
            justify="center")

        
        self.minsLabel = tk.Label(text="Minutes: ")
        self.minsEntry = tk.Entry(textvariable= self.minsRqst) # textbox for user to enter desired minute count, input saved in variable
        self.secsLabel = tk.Label(text="Seconds: ")
        self.secsEntry = tk.Entry(textvariable=self.secsRqst) # textbox for user to enter desired minute count, input saved in variable


        self.timeRemLabel = tk.Label( text=f"{self.minsRqst.get():02d}:{self.secsRqst.get():02d}" ) # displays how long is currently left

        # Appears on startup
        self.welcome.pack()
        self.minsLabel.pack() 
        self.minsEntry.pack() # where user enters minute count
        self.secsLabel.pack()
        self.secsEntry.pack() # where user enters second count
        self.secsEntry.bind("<FocusIn>", self.handleSecsEntryFocus)
        self.minsEntry.bind("<FocusIn>", self.handleMinsEntryFocus)
        self.secsEntry.bind("<FocusOut>", self.handleSecsEntryOutOfFocus)
        self.minsEntry.bind("<FocusOut>", self.handleMinsEntryOutOfFocus)

        self.timeRemLabel.pack()
        self.startButton.pack() # user clicks to begin timer

        self.terminateProgram.pack() # can click anytime to end program/timer
        self.nameTimer.pack(pady=(20))
        self.window.mainloop()

    def handleSecsEntryFocus(self, event):
        if self.secsEntry.get() == '0':
            self.secsEntry.delete(0,tk.END)

    def handleSecsEntryOutOfFocus(self, event):
        if self.secsEntry.get() == '':
            self.secsEntry.insert(0, '0')        ############# should this be '0' or 0, does it matter??

    def handleMinsEntryFocus(self, event):
        if (self.minsEntry.get() == '0') and (self.secsEntry.get() == '' or self.secsEntry.get() == '0'):
            self.minsEntry.delete(0,tk.END)

    def handleMinsEntryOutOfFocus(self, event):
        if self.minsEntry.get() == '':
            self.minsEntry.insert(0, '0')        ############# should this be '0' or 0, does it matter??

    # method to start timer
    def startTimer(self):
        mins=self.minsRqst.get()
        secs=self.secsRqst.get()

        #print(f"mins: {self.minsRqst.get()}")
        #print(f"secs: {self.secsRqst.get()}")

        total = ((60*mins) + secs) # count how many seconds the timer will take
        #print(total)

        self.decreaseTimer(self.minsRqst,self.secsRqst,total) 

    def decreaseTimer(self, minsRqst,secsRqst,total):
        if(total == 0): # when timer reaches 0
            self.notify() # notify the user
            return(self.timeRemLabel.config(text="Time's up", font=("Times New Roman", 12, "bold"), width=40, bg="#FF991C")) # Stretch Label to near edges, change font
        
        else:       
            if((secsRqst.get() == 0) and not (minsRqst == 0)): # E.g. when we reach 1:00 --> 0:59
                secsRqst.set(59) # second count set to 59
                minsRqst.set(minsRqst.get() - 1) # decrease minute count by 1

            else:
                secsRqst.set(secsRqst.get() - 1) # decrease second count by 1

            self.timeRemLabel.config(text=f"{minsRqst.get():02d}:{secsRqst.get():02d}") # update the label for  
            
        self.window.after(1000, self.decreaseTimer, minsRqst, secsRqst, total-1) # each second decrease total time remaining by 1

    def notify(self): # notifies user timer has ended
        notification.notify(
            title="Timer has ended", 
            message="Want to start again?",
            app_icon='',
            app_name='Timer App'
        )
       # playsound('../Soundd-1-1.m4a')
        #playsound('../Soundd-1-1.m4a')


if __name__ == "__main__":
    Timer()