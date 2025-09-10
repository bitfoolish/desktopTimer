import tkinter as tk
import time

window = tk.Tk()

window.config(bg="#9B3B34")


minsRqst=tk.IntVar()
secsRqst=tk.IntVar()


def startTimer():
    mins=minsRqst.get()
    secs=secsRqst.get()

    print(f"mins: {mins}")
    print(f"secs: {secs}")


    total = ((60*mins) + secs)
    print(total)

    decreaseTimer(mins,secs,total)

#    time.sleep(total)

def decreaseTimer(mins,secs,total):
    
    if(secs == 0):
        secs = 59
        mins -= 1

    else:
        secs -= 1

    minsLabel = tk.Label(
        text="Mins: " + str(mins) + "Secs: " + str(secs)
    )

    minsLabel.pack()
#    time.sleep(1) 
    total -= 1
    if(total == 0):
        return None
    else:
        decreaseTimer(mins,secs,total)

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


welcome.pack()
startButton.pack()

minsLabel.pack()
minsEntry.pack()

secsLabel.pack()
secsEntry.pack()

terminateProgram.pack()
window.mainloop()