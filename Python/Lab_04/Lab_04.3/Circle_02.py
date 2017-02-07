#Kristen Ching
r = float(input("Enter the radius of your circle. "))
pi = 3.14
def calcArea(radius):
    global area
    area = (radius**2)*pi

calcArea(r)
print ("The area of a circle with a radius of", r, "is",  "{:10.5f}".format(area))
