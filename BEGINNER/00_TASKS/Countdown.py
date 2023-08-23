import time

sec = int(input("Set The Timer in Seconds: ")) # getting the number of seconds the user wants to pass

ongoing_sec = 1
while ongoing_sec != sec + 1:
    time.sleep(1)
    print(f"Seconds Passed: {ongoing_sec}")
    ongoing_sec += 1 # this prevents the infinite while-loop