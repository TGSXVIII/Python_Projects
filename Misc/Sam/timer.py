from Misc.Sam import time

seconds = time.time()
print("Time in seconds since the epoch:", seconds)
local_time = time.ctime(seconds)
print("Local time:", local_time)

# Timer starts
startTime = time.time()
lastTime = startTime
lapnum = 1
value = ""

print("Press ENTER for each lap.\nType Q and press ENTER to stop.")

while value.lower() != "q":
    # Input for the ENTER key press
    value = input()

    # The current lap-time
    laptime = round((time.time() - lasttime), 2)

    # Total time elapsed since the timer started
    totaltime = round((time.time() - starttime), 2)

    # Printing the lap number, lap-time, and total time
    print("Lap No. " + str(lapnum))
    print("Total Time: " + str(totaltime))
    print("Lap Time: " + str(laptime))

    print("*" * 20)

    # Updating the previous total time and lap number
    lasttime = time.time()
    lapnum += 1

print("Exercise complete!")