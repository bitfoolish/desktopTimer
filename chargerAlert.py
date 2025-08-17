from plyer import battery, notification

stats = (battery.status)

if battery.status['percentage'] >= 80: # battery level at 80 or above
    notification.notify(
        title="Battery has reached 80%", 
        message="Disconnect charger!"
    )

else:
    notification.notify(
        title="battery very low", 
        message="charge me up",
    )
#    print("battery too low")

## while loop until it no longer charging, maybe sleep for 5 mins and only notify once at 80