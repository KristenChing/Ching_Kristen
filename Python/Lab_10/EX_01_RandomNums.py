#Kristen Ching
import random
numsList = []
for i in range(0, 4):
    numsList.append([])
    for x in range (0, 4):
        numsList[i].append(random.randint(0, 100))
print(numsList)
##for nums in numsList:
##    output = ""
##    for num in nums:
##        output += str(num) + " "
##    print(output)
