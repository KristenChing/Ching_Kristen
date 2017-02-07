#Kristen Ching
w = int(input("Please enter the WIDTH of your box in INCHES. "))
l = int(input("Please enter the LENGTH of your box in INCHES. "))
h = int(input("Please enter the HEIGHT of your box in INCHES. "))

def boxes_are_stupid(w, l , h):
    volume = w*l*h
    return 0.000578704*volume

cube_foot_volume = boxes_are_stupid(w, l, h)
print ("The measurement of your box's volume in cubic feet is", cube_foot_volume)
    
