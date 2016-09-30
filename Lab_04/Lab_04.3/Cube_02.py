side = float(input("Enter the length of the side. "))

def calcSurf(side):
    global area
    area = float(6*(side**2))

calcSurf(side)

print("The surface area of a cube with", side, "length sides is", "{:10.5f}".format(area))
