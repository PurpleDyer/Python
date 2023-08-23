phrase = "Hello World"
phrase2 = ""
counter = 0

for i in phrase:
    if i == 'l' and counter != 2:
        phrase2 += 'L'
        counter += 1
    else:
        phrase2 += i
        
print(phrase2)