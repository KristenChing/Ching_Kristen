#Kristen Ching
math = input("Please enter a mathematical expression. AND USE SPACES!!! ")
equation = math.split(" ")
i = 0
while i < len(equation):
    if i < len(equation) and ((equation[i] == "*" or equation[i] == "/")):
        if equation[i] == "*":
            equation[i] = equation[i-1] * equation[i+1]
        else:
            equation[i] = equation[i-1] / equation[i+1]
        equation.remove(equation[i-1])
        equation.remove(equation[i])
    i += 1
    
while i < len(equation):
    if i < len(equation) and ((equation[i] == "+" or equation[i] == "-")):
        if equation[i] == "+":
            equation[i] = equation[i-1] + equation[i+1]
            print(equation)
        else:
            equation[i] = equation[i-1] - equation[i+1]
        equation.remove(equation[i-1])
        equation.remove(equation[i])
    i += 1
print(equation)



