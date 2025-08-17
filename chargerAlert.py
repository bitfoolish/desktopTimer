from plyer import battery, notification
import time

targetPercentage = 80 # 80% target charge

if not battery.status['isCharging']: # exit program as user doesn't have their device charging
    raise ValueError("Plug in your charger and run again!\n")

while battery.status['isCharging']: # when charger is on 
    percent = battery.status['percentage']

    if percent >= targetPercentage: # battery level at 80 or above
        notification.notify(
            title="Battery has reached " + str(targetPercentage) + "%", 
            message="Disconnect charger --->  " + str(percent) + " %",
        )
        time.sleep(3*60) # send reminder every 3 minutes to unplug charger

    else: # battery not yet at target percentage
        notification.notify(
            title="Keep going", 
            message="Battery at " + str(percent) + "%, " + str(targetPercentage - percent) + " to go",
        )
        if(percent < 70): # if less than 70% sleep until likely around 70
            time.sleep((70 - percent) * 60)
        else: # between 70 and 80 just sleep until predicated finish time
            probableTimeLeft = (targetPercentage - percent) + 2 
            notification.notify(
                title="Around " + str(probableTimeLeft) + " mins left",
                message="Current percentage --> " + str(percent) + "%"
            )
            print(probableTimeLeft)
            time.sleep(probableTimeLeft*60)
