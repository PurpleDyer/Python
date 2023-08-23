a = int(input())
b = int(input())
c = int(input())
# a, b, c = list(map(int, input().split()))

if a == b == c:
    print("motevazi ol azla")
elif (a == b != c) or (a != b == c) or (a == c != b):
    print("sagheine")
else:
    print("fuck off")