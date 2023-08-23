a = int(input("Please Enter You Current Temp: "))

if a < 0:
    print("Freezing")
elif 0 <= a < 10:
    print("Very Cold")
elif 10 <= a < 20:
    print("Cold")
elif 20 <= a < 30:
    print("Normal")
elif 30 <= a < 40:
    print("Hot")
else:
    print("Very Hot")