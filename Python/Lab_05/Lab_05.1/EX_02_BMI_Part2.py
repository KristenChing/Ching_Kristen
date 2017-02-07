#Kristen Ching
#Kristen Ching
height = float(input("Please enter your height (in inches) "))
weight = float(input("Please enter your weight (in pounds/lbs) "))
def calcBMI(h, w):
    global BMI
    BMI = w*0.45/((h*0.025)**2)
    if BMI >= 39.9:
        return "Morbidly Obese"
    elif BMI >= 35:
        return "Very Obese"
    elif BMI >= 29.9:
        return "Obese"
    elif BMI >= 25:
        return "Overweight"
    elif BMI > 18.5:
        return "Normal"
    elif BMI < 18.5:
        return "Underweight"
        
condition = calcBMI(height, weight)
print("Your BMI is:", BMI)
print("You are", condition)
