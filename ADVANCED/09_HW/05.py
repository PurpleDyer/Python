def decorator(f):
    def wrapper(*args, **kwargs):
        try:
            res = f(*args, **kwargs)
            return res
        except ZeroDivisionError:
            return "Can not divide by zero"
    return wrapper

# =======================

@decorator
def divide(a, b):
    return a / b

# ========================

print(divide(6, 2))
print(divide(6, 0))