# Zoe Jimenez, Time of Day python
import time

current = time.time()
local_time = time.localtime(current)
hour = local_time.tm_hour



if hour >= 18 and hour <= 22:
    print("Good evening, the moon is coming up!")
elif hour >= 12:
    print("Good afternoon, have you eaten yet?")
elif hour >= 6:
    print("Goodmorning! Rise and shine!")
else:
    print("Go to bed what are you doing up at this time of day??")

