import tkinter as tk
import time
from plyer import notification

class Timer:
    def __init__(self):
        self.window = tk.Tk()
        self.window.config(bg="#9B3B34")

        self.minsRqst=tk.IntVar()
        self.secsRqst=tk.IntVar()
        self.minsRqst.set(0)
        self.secsRqst.set(0)

        self.welcome = tk.Label(text="Please enter your desired time below", fg="black")

        self.startButton = tk.Button(
            text="Start Timer",
            width=25,
            height=5,
            bg="blue",
            fg="yellow",
            command=self.startTimer
        )

        self.terminateProgram = tk.Button(
            text="Exit program",
            bg="grey",
            fg="yellow",
            command=self.window.destroy
        )


        self.minsLabel = tk.Label(text="Minutes: ")
        self.minsEntry = tk.Entry(textvariable= self.minsRqst)
        self.secsLabel = tk.Label(text="Seconds: ")
        self.secsEntry = tk.Entry(textvariable=self.secsRqst)


        self.timeRemLabel = tk.Label( text=f"{self.minsRqst.get()}:{self.secsRqst.get()}" )

        self.welcome.pack()
        self.minsLabel.pack() # Appears on startup
        self.minsEntry.pack() # Appears on startup, where user enters minute count
        self.secsLabel.pack() # Appears on startup
        self.secsEntry.pack() # Appears on startup, where user enters second count

        self.timeRemLabel.pack()
        self.startButton.pack()

        self.terminateProgram.pack() # can click anytime to end program/timer
        self.window.mainloop()


    def startTimer(self):
        mins=self.minsRqst.get()
        secs=self.secsRqst.get()

        print(f"mins: {self.minsRqst.get()}")
        print(f"secs: {self.secsRqst.get()}")

        total = ((60*mins) + secs)
        print(total)

        self.decreaseTimer(self.minsRqst,self.secsRqst,total)

    def decreaseTimer(self, minsRqst,secsRqst,total):
        if(total == 0): # when timer reaches 0
            self.notify() # notify the user
            return(self.timeRemLabel.config(text="Time's up"))
        
        else:       
            if((secsRqst.get() == 0) and not (minsRqst == 0)):
                secsRqst.set(59)
                minsRqst.set(minsRqst.get() - 1)

            else:
                secsRqst.set(secsRqst.get() - 1)

            self.timeRemLabel.config(text=f"{minsRqst.get():02d}:{secsRqst.get():02d}")
            
        self.window.after(1000, self.decreaseTimer, minsRqst, secsRqst, total-1) 

    def notify(self): # notifies user timer has ended
        notification.notify(
            title="Timer has ended", 
            message="Want to start again?",
        )


if __name__ == "__main__":
    Timer()