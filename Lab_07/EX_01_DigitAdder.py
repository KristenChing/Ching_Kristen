#Kristen Ching
num = int(input("Please enter a number. "))
numsum = 0
while num > 0:
    numsum = num%2
    num = num/10
print (numsum)
