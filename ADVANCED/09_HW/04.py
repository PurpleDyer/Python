def decorator(f):
    my_dict = {}
    def wrapper(*args, **kwargs):
        nonlocal my_dict
        inputs = str(args) + str(kwargs)
        if inputs in my_dict.keys():
            print("returned from cache!")
            return my_dict.get(inputs)
        res = f(*args, **kwargs)
        my_dict.update({inputs: res})
        return res
    return wrapper

# ================================

@decorator
def add(a, b):
    return a + b

# =================================

print(add(1, 2))
print(add(2, 2))
print(add(1, 2))
print(add(2, 4))