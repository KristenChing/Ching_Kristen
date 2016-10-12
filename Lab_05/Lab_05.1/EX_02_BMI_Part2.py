#Kristen Ching
#Kristen Ching
height = float(input("Please enter your height (in inches) "))
weight = float(input("Please enter your weight (in pounds/lbs) "))
def calcBMI(h, w):
    global BMI
    BMI = w*0.45/((h*0.025)**2)
    if BMI < 18.5:
        return "Underweight"
    if (BMI > 18.5) and (BMI < 24.9):
        return "Normal"
    if (BMI > 25) and (BMI <29.9 ):
        return "Overweight"
    if (BMI > 29.9) and (BMI < 34.9):
        return "Obese"
    if (BMI > 35) and (BMI < 39.9):
       return "Very Obese"
    if (BMI > 39.9):
        return "Morbidly Obese"
condition = calcBMI(height, weight)
print("Your BMI is:", BMI)
print("You are", condition)
