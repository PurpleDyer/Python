# a = 97  A = 65  z = 122  Z = 96

a = int(ord(input("Please Enter a Character: ")))

if 65 <= a <= 122:
    if 97 <= a <= 122:
        print("LowerCase")
    else:
        print("UpperCase")
else:
    print("This Character is not in the Alphabet")