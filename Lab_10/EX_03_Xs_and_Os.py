#Kristen Ching
import random
xAndO = []
for i in range(0, 4):
    xAndO.append([])
    for j in range(0,4):
        switch = random.randint(1, 100)
        if switch == 1:
            xAndO[i].append("X")
        else:
            xAndO[i].append("O")
    for values in xAndO:
        output = ""
        for value in values:
            output += value
    print(output)
