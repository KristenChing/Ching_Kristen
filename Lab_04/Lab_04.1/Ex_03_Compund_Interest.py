#Kristen Ching
r = int(input("Enter the interest rate. "))
p = int(input("Enter the principal. "))
n = int(input("Enter the number of times the loan is compounded per year. "))
t = int(input("Enter the life of the loan (in years). "))

def payment(r, p, n, t):
    return p*(1 + r/n)**(n*t)

cost = payment(r, p, n, t)
print("The total cost of the loan is", cost) 
