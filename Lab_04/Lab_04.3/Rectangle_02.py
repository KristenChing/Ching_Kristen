length = float(input("Enter the length. "))
width = float(input("Enter the width. "))

def calcPerim(l, w):
    global perimeter
    perimeter = (2*(l+w))

calcPerim(length, width)
print ("Your rectangle is", "{:10.5f}".format(perimeter), "sq feet around.")







