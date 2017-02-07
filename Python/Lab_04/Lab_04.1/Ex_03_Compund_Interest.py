#Kristen Ching
r = float(input("Enter the interest rate. "))
p = float(input("Enter the principal. "))
n = float(input("Enter the number of times the loan is compounded per year. "))
t = float(input("Enter the life of the loan (in years). "))

def payment(r, p, n, t):
    return p*((1 + r/n)**(n*t))/(12*t)

cost = payment(r, p, n, t)
print("The total payment of the loan is ${:0.2f}".format(cost)) 
