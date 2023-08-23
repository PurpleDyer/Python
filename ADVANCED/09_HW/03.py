f = open("file.txt", "r")
file = f.read()

def decorator(f):
    def wrapper(*args, **kwargs):
        global file
        res = f(*args, **kwargs)
        new_file = open("file.txt", "w")
        new_file = file + "\n input: " + args + kwargs + "output: " + res
        return res
    return wrapper

@decorator
def add(a, b):
    return a + b

add(2, 5)
add(1, 2)
add(6, 6)

# !   THIS DOESNT WORK    !