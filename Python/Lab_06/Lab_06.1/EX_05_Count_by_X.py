#Kristen Ching
num1 = int(input("Please enter a number. "))
num2 = int(input("Please enter another number. "))
output = ""
for x in range(num2, num1 + 1, num2):
    output = output + "\t" + str(x)
print (output)
