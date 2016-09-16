num1 = 13
num2 = 7
sum = 13 + 7
print (num1, "plus", num2, "equals", sum)

def newFunc(name, address, city, state, zipcode):
    print (name, "\n", address, "\n", city, ",", state, ",", zipcode)

newFunc("Kristen Ching", "nowhere", "San Diego", "California", "92130")

def surfaceArea(length, height, width):
    area = (length*height)*2 + (height*width)*2 + (width*length)*2
    print ("The surface area of your rectangle is " + str(area))

surfaceArea(12, 134, 37)
