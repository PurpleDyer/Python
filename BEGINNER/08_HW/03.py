scores = []
counter = 0

while counter != 3:
    scores.append(input("Enter Your Score: "))
    counter += 1

if all(scores) == False:
    print("Bravo Bravo")

print(scores)