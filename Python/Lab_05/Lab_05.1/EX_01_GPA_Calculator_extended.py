#Kristen Ching
#Extended edition (NOTE: It's called 'extended' for a reason.)
#Made for the fun of it ;)
#Sorry, I'm just really proud of this. :D
grade1 = input("Please enter your science grade. ")
grade2 = input("Please enter your math grade. ")
grade3 = input("Please enter your history grade. (If none, type 'none') ")
grade4= input("Please enter your english grade. ")
grade5 = input("Please enter your PE grade. ")
grade6 = input("Please enter your first elective grade. (If none, type 'none') ")
grade7 = input("Please enter your second elective grade. (If none, type 'none') ")
grade8 = input("Please enter your third elective grade. (If none, type 'none') ")
classes = 8
if grade8 == "none":
    classes -=1
def gradeNull(grade):
    global classes
    if grade == "none":
        classes -=1
    return grade   
def calcPoints(grade):
    if grade == "A":
        return 4.0
    if grade == "B":
        return 3.0
    if grade == "C":
        return 2.0
    if grade == "D":
        return 1.0
    if grade == "F" or "none":
        return 0.0

GPA = (calcPoints(grade1) + calcPoints(grade2) + calcPoints(gradeNull(grade3)) + calcPoints(grade4) + calcPoints(grade5) + calcPoints(gradeNull(grade6)) + calcPoints(gradeNull(grade7)) + calcPoints(grade8))/classes
print ("Your GPA is", GPA)    
