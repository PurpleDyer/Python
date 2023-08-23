"""
Move Opportunity

 -> 25 - (x) = y
 -> 25 - [5th] = 0
 -> 25 - 5x = 0
 -> x = 5 => 2*10 => x * 4
 -> final => "100 - x*4"
 x = night

"""
import time
import random

night = int(input("Please Enter Which Night You Want To Play: "))

while True:
    time.sleep(1)
    r = random.randint(0,100)
    print(r)
    if r > (100-(5*(night*4))):
        print("Freddy Moved...")
    else:
        print("Failed Move [Freddy]")