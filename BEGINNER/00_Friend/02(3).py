my_list = [int(i) for i in input("Please Enter Your Numbers Seperated With Spaces: ").split()] 
print(True) if max(my_list)%10 == max(map(lambda x: x%10, my_list)) else print(False) 