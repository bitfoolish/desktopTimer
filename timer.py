import time
from plyer import notification

print(time.time())

userTimer = int(input("How many seconds?\n" )) 
#endTime = userTimer + time.time()
#print(time.time(), endTime)
#while (time.time() < (endTime)):
print(f'going to sleep for {userTimer} seconds\n  Current time: {time.time()}')
time.sleep(userTimer)
print(f'  Current time: {time.time()}, time is up you slept for {userTimer} seconds!')