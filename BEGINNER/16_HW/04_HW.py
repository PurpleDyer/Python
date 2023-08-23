first_str = input("Please Enter Your String: ")
second_str = input("Please Enter Another String: ")

if len(first_str) > len(second_str):
    print(f"Diff: {len(first_str) - len(second_str)}")
elif len(first_str) < len(second_str):
    print(f"Diff: {len(second_str) - len(first_str)}")
else:
    print("They Have The Same Length!")