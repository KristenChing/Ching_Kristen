side = float(input("Enter the length of the side. "))

def calcSurf(side):
    return "{:10.5f}".format(float(6*(side**2)))

print("The surface area of a cube with", side, "length sides is", calcSurf(side))
