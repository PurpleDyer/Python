from datetime import datetime

hour = float(str(str(datetime.now()).split()[1]).split(":")[0])
minute = float(str(str(datetime.now()).split()[1]).split(":")[1])
second = float(str(str(datetime.now()).split()[1]).split(":")[2])

if not (hour//10)%2:
    print("yes")
else:
    print((hour%10 + minute%10 + second%10)/3) 