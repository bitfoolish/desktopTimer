from plyer import battery, notification
import time

targetPercentage = 80 # 80% target charge

#stats = (battery.status)
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
        if(percent < 60): # if less than 60% sleep until likely around 60
            time.sleep((60 - percent) * 60)
        else: # between 60 and 80 just sleep in 5 min intervals
            probableTimeLeft = (targetPercentage - percent) + 2 
            notification.notify(
                title="Around " + str(probableTimeLeft) + " mins left",
                message="Current percentage --> " + str(percent) + "%"
            )
            time.sleep(probableTimeLeft*60)

