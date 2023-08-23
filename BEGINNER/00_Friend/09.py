count_numbers = 0
sum_numbers = 0
flag = False
while not flag:
    a = int(input())
    if a == 0:
        flag = True
    else:
        sum_numbers += a
        count_numbers += 1
print(sum_numbers / count_numbers)