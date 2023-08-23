def decorator(f):
    count = 0
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"{f.__name__} function called {count} times")
        res = f(*args, **kwargs)
        return res
    return wrapper

# ============================

@decorator
def add(a,b):
    return a + b

# ===========================

add(1, 1)
add(2, 2)
add(3, 3)