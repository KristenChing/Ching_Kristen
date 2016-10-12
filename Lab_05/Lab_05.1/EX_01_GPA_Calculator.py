#Kristen Ching
grade1 = input("Please enter your science grade. ")
grade2 = input("Please enter your math grade. ")
grade3 = input("Please enter your history grade. ")
grade4= input("Please enter your english grade. ")
grade5 = input("Please enter your PE grade. ")
grade6 = input("Please enter your first elective grade. ")
grade7 = input("Please enter your second elective grade. ")
classes = 7 
def calcPoints(grade):
    if grade == "A":
        return 4.0
    if grade == "B":
        return 3.0
    if grade == "C":
        return 2.0
    if grade == "D":
        return 1.0
    if grade == "F":
        return 0.0

GPA = (calcPoints(grade1) + calcPoints(grade2) + calcPoints(grade3) + calcPoints(grade4) + calcPoints(grade5) + calcPoints(grade6) + calcPoints(grade7)/classes)
print ("Your GPA is", GPA)    
