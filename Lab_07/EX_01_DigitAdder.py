#Kristen Ching
number = int(input("Please enter a number. "))
numsum = 0
num = number
while num > 0:
    numsum = num%10 + numsum
    num = int(num/10)
print ("The sum of the digits in", number, "is", numsum)
