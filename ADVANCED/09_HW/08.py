import time

# ===================

def decorator(f):
    def wrapper(*args, **kwargs):
        time.sleep(1)
        res = f(*args, **kwargs)
        return res
    return wrapper

# ====================

@decorator
def add(a, b):
    return a + b

# ====================

print(add(1, 2))
print(add(2, 5))