from datetime import datetime

hour = str(str(datetime.now()).split()[1]).split(":")[0]
minute = str(str(datetime.now()).split()[1]).split(":")[1]

if hour == "05" and minute == "06":
    print("Morning")
elif hour == "13" and minute == "14":
    print("Noon")
elif hour == "20" and minute == "20":
    print("Night") 