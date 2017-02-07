num1 = float(input("Enter a number. "))
num2 = float(input("Enter a number. "))
num3 = float(input("Enter a number. "))

def average(one, two, three):
    global avg
    avg = float(str((one+two+three)/3))

average(num1, num2, num3)
print("The average of", num1, num2, "and", num3, "is", "{:10.5f}".format(avg))
