a = int(input("Please Enter a Number: "))
b = int(input("Please Enter Another Number: "))
c = int(input("Please Enter Another Number: "))

if a == b == c:
    print("Mosalas Motevazi ol\' Azla")
elif a == b != c or a == c != b or b == c != a:
    print("Mosalas Motesavi o\' Saghein")
else:
    print("Mosalas Mokhtalef ol\' Azla")