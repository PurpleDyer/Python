f = open("file2.txt", "r")

my_list = f.read().splitlines() # getting information from the file and splitting them by lines
main_list = []

for idx in range(len(my_list)):
    main_list.append(my_list[idx].split()) # adding the elements of information with no space between them to another list called "main_list"

print(main_list)

change = input("What Do You Want To Change?: ").lower() # getting which value the user wants to be changed 
changeto = input("Please Enter The Changed Settings: ") # getting the value the user wants it to change to

for i in main_list:
    if i[0] == change:
        i[-1] = changeto
        break            # finding the wanted value and changing it

print(main_list)

last_string = ""
g = open("file2.txt", "w") # opening the file as a "write" type

for i in main_list:
    idx = 0
    while idx < len(i):
        last_string += i[idx] + " "
        idx += 1
    last_string += "\n"               # saving all the changed information in a string called "last_string"
    
g.write(last_string)  # adding the changed information which was stored in "last_string" to the file