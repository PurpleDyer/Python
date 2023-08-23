import math

a = int(input("Enter a Number for a: "))
b = int(input("Enter a Number for b: "))
c = int(input("Enter a Number for c: "))

Ans1 = (-b + int(math.sqrt(b**2 - 4*a*c))) // (2*a)
Ans2 = (-b - int(math.sqrt(b**2 - 4*a*c))) // (2*a)

print(Ans1, "And", Ans2)