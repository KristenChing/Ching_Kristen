#Kristen Ching
import random
class Inventory:
    def __init__(self, manuf, name, category = "", price = ""):
        self.manufacturer = manuf
        self.name = name
        self.upc = random.randint(0, 10000)
        self.category = category
        self.price = price

    def resetVals(self, manuf, name, category, price):
        self.manufacturer = manuf
        self.name = name
        self.category = category
        self.price = price
        self.upc = random.randint(0, 10000)

    def __str__(self):
        return "Item Info... \nManufacturer: " + self.manufacturer + \
        "\nName: " + self.name + \
        "\nCategory: " + self.category + \
        "\nPrice: $" + str(self.price) + \
        "\nUPC: #" + str(self.upc)
def main():
    manuf = input("Please enter manufacturer name. ")
    name = input("Please enter the name of the item. ")
    moreInfo = input("Do you wish to enter category and price information? Enter y/n ")
    if moreInfo == "y":
        item1 = Inventory(manuf, name)
        category = input("Please enter the category of the item. ")
        price = input("Please enter the price of the item. ")
        item1.resetVals(manuf, name, category, price)
    else:
        item1 = Inventory(manuf, name)
    print(item1.__str__())
main()
