#Kristen Ching
num = int(input("Please enter an integer. "))
tableSize = int(input("What size do you want the table to be? "))
print("_"*3 + "|" + "_"*3)
for i in range(num, tableSize + 2):
    print(" {:0} |  {:0}".format(i - 1, num*(i-1)))
