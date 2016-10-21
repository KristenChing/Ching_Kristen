#Kristen Ching
num = int(input("Please enter an integer. "))
tableSize = int(input("What size do you want the table to be? "))
print("_"*3 + "|" + "_"*3)
for i in range(num, tableSize + 1):
    print(" {:0} |  {:0}".format(num, num*i))
