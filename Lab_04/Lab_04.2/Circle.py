#Kristen Ching

r = float(input("Enter the radius of your circle. "))
pi = 3.141592653
def calcArea(radius):
    return "{:10.5f}".format((radius**2)*pi)

print ("The area of a circle with a radius of", r, "is", calcArea(r))
