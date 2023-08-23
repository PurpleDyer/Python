import time

my_list = [chr(92), '|', '/','—']
looper = 1

while True:
    a = str()
    b = my_list[looper%len(my_list)]
    time.sleep(0.15)
    print(f"{a}\r{a+b}", flush=True, end="")
    a = b
    looper += 1