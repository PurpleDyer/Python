a, b, c, d = input("Please Enter 4 Numbers Seperated With Spaces: ").split()
a, b, c, d = int(a), int(b), int(c), int(d)
n = int(input("Please Enter The Power Value: "))

top_res = [a*a+b*c, a*b+b*d]
bottom_res = [c*a+d*c, c*b+d*d]

for i in range(n-2):
    top_res[0], top_res[1] = top_res[0] * (a*a+b*c), top_res[1] * (a*b+b*d)
    bottom_res[0], bottom_res[1] = bottom_res[0] * (c*a+d*c), bottom_res[1] * (c*b+d*d)

print(f"{top_res}\n{bottom_res}")