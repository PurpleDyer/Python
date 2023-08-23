import time 

# ====================

def decorator(f):
    def wrapper(*args, **kwargs):
        first_timer = time.perf_counter()
        res = f(*args, **kwargs)
        second_timer = time.perf_counter()
        print(f"the {f.__name__} function took {second_timer - first_timer}ms to run")
        return res
    return wrapper

# =====================

@decorator
def add(a, b):
    return a + b

# =====================

add(2, 4)
add(2, 5)