#Kristen Ching
item1 = input("Please enter item 1: ")
price1 = float(input("Please enter the price: "))
item2 = input("Please enter item 2: ")
price2 = float(input("Please enter the price: "))
item3 = input("Please enter item 3: ")
price3 = float(input("Please enter the price: "))
subtotal = float(price1 + price2 + price3)
tax = 0.01*subtotal
total = subtotal + tax

def receipt(item, price):
    print ("*{:>15}{:<10}".format(item, ".......") + price)

print ("<<<<<<<<<<<<<<<__Receipt__>>>>>>>>>>>>>>>>\n")
receipt(item1, str(price1))
receipt(item2, str(price2))
receipt(item3, str(price3))
receipt("Subtotal:", str(subtotal))
receipt("Tax:", str(tax))
receipt("Total:", str(total))
print ("__________________________________________")
print ("* Thank you for your support *")
