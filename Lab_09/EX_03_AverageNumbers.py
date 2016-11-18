#Kristen Ching
import random
numbers = []
for x in range(0, 10):
    numbers.append(str(random.randint(1, 100)))
print("Numbers...")
output = ""
for x in numbers:
    output = output + x + " "
print(output)
print("\n")
def average(numbers):
    integer = 0
    numsum = 0
    for num in numbers:
        num = int(num)
        numsum = numsum + num
        integer += 1
    return str(numsum/integer)
        
print("The average of the above numbers is..." + average(numbers))
