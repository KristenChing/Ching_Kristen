#Kristen Ching
item1 = input("Please enter the name of the item. ")
price1 = float(input("Please enter the price of the item. "))
item2 = input("Please enter the name of the item. ")
price2 = float(input("Please enter the price of the item. "))
item3 = input("Please enter the name of the item. ")
price3= float(input("Please enter the price of the item. "))
item4 = input("Please enter the name of the item. ")
price4 = float(input("Please enter the price of the item. "))
subtotal = price1 + price2 + price3 + price4

def discount(subtotal):
    if subtotal >= 2000:
        return subtotal*0.85
    if not subtotal >= 2000:
        return float(subtotal)
    

def format(item, price):
    print("{:>10}............{:<10.2f}".format(item, price))


print("<<<<<<<<<<< Receipt >>>>>>>>>>>>>>")
format(item1, price1)
format(item2, price2)
format(item3, price3)
format(item4, price4)
format("Subtotal", subtotal)
format("Total (without tax)", discount(subtotal))
print("_" * len("<<<<<<<<<<< Receipt >>>>>>>>>>>>>>"))
print("Thank you.")




