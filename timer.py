import time
from plyer import notification

print(time.time())

userTimer = int(input("How many seconds?\n" )) 
endTime = userTimer + time.time()
print(time.time(), endTime)
while (time.time() < (endTime)):
    time.sleep(1)
print(f'{time.time()}, time is up you slept for {userTimer} seconds!')