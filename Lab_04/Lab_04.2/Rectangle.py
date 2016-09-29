length = float(input("Enter the length. "))
width = float(input("Enter the width. "))

def calcPerim(l, w):
    return (2*(l+w))

print ("Your rectangle is", "{:10.5f}".format(calcPerim(length, width)), "sq feet around.")







