my_list = []

# ==========================

def decorator(f):
    global my_list
    if not f.__name__ in my_list:
        my_list.append(f.__name__)
        print(my_list)
    def wrapper(*args, **kwargs):
        res = f(*args, **kwargs)
        return res
    return wrapper

# ==========================

@decorator
def add(a, b):
    return a + b

@decorator
def multiply(a, b):
    return a * b

@decorator
def greeting(name):
    return f"welcome, {name}!"