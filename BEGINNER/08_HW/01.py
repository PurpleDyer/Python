phrase = "Hello world"

#------------------------------------------------------------

phrase2 = ""
for i in phrase:
    if i == 'e':
        phrase2 += 'eeeeee'
    else:
        phrase2 += i
print(phrase2)

#------------------------------------------------------------

phrase2 = ""
while len(phrase2) <= 3:
    phrase2 += phrase[len(phrase2)]
print(phrase2)

#------------------------------------------------------------

temp_phrase = phrase.replace(" ", "")
phrase2 = ""
index = 0
while True:
    if index + 1 < len(phrase):
        phrase2 += temp_phrase[index]
        index += 4
    else:
        phrase2 += 'ddddddd'
        break

print(phrase2)

#------------------------------------------------------------

phrase2 = ""
index = 0
while index != 5:
    phrase2 += phrase[index]
    index += 1
print(phrase2[::-1])

#------------------------------------------------------------

phrase2 = ""
index = 6
while index < len(phrase):
    if phrase[index] != 'l':
        phrase2 += phrase[index]
    index += 1
print(phrase2) # WRONG => NO OUTPUT

#------------------------------------------------------------

phrase2 = ""
index = 0
for i in phrase:
    if i == 'o':
        phrase2 += i*7
        break
    else:
        phrase2 += i
print(phrase2)