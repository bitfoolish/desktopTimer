import tkinter as tk
import time

window = tk.Tk()

window.config(bg="#9B3B34")


minsRqst=tk.IntVar()
secsRqst=tk.IntVar()
minsRqst.set(0)
secsRqst.set(0)


def startTimer():
    mins=minsRqst.get()
    secs=secsRqst.get()
    #print(type(secs))


    print(f"mins: {minsRqst.get()}")
    print(f"secs: {secsRqst.get()}")


    total = ((60*mins) + secs)
    print(total)

    decreaseTimer(minsRqst,secsRqst,total)

def decreaseTimer(minsRqst,secsRqst,total):
    
    if(total == 0):
        return(timeRemLabel.config(text="Time's up"))

    else:       
        if((secsRqst.get() == 0) and not (minsRqst == 0)):
    #        print(type(secs))
            secsRqst.set(59)
            minsRqst.set(minsRqst.get() - 1)

        else:
            #print(type(secs))
            secsRqst.set(secsRqst.get() - 1)

        timeRemLabel.config(text=f"{minsRqst.get():02d}:{secsRqst.get():02d}")
        
    window.after(1000, decreaseTimer, minsRqst, secsRqst, total-1) 


welcome = tk.Label(
    text="Please enter your desired time below",
    fg="black"
)

startButton = tk.Button(
    text="Start Timer",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
    command=startTimer
)

terminateProgram = tk.Button(
    text="Exit program",
    bg="grey",
    fg="yellow",
    command=window.destroy
)


minsLabel = tk.Label(
    text="Minutes: "
)

minsEntry = tk.Entry(
    textvariable= minsRqst
)

secsLabel = tk.Label(
    text="Seconds: "
)

secsEntry = tk.Entry(
    textvariable=secsRqst
)


timeRemLabel = tk.Label(
    text=f"{minsRqst.get()}:{secsRqst.get()}"
)

welcome.pack()

minsLabel.pack() # Appears on startup
minsEntry.pack() # Appears on startup, where user enters minute count

secsLabel.pack() # Appears on startup
secsEntry.pack() # Appears on startup, where user enters second count

timeRemLabel.pack()
startButton.pack()

terminateProgram.pack() # can click anytime to end program/timer
window.mainloop()