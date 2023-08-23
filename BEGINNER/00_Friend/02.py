a = int(input())
b = int(input())
c = int(input())
max_num = max(a, b, c)%10
if max_num >= a%10 and max_num >= b%10 and max_num >= c%10:
    print(True)
else:
    print(False)