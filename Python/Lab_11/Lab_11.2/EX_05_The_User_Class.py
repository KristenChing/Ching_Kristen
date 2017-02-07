#Kristen Ching
import random
class User:
    def __init__(self, firstName, lastName, avat=""):
        self.first = firstName
        self.last = lastName
        self.avatar = avat
        self.ID = random.randint(0, 100000)

    def setVals(self, firstName, lastName, avat):
        self.first = firstName
        self.last = lastName
        self.avatar = avat
        self.ID = random.randint(0, 100000)

    def __str__(self):
        return "Customer Info... \nFirst Name: " + self.first + \
        "\nLast Name: " + self.last + \
        "\navatar: " + self.avatar + \
        "\nUser ID: " + str(self.ID)

def main():
    firstName = input("Please enter your first name. ")
    lastName = input("Please enter your last name. ")
    createAvat = input("Would you like to use a public avatar? Enter y/n ")
    if createAvat == "y":
        avat = input("Please enter a name for your public avatar. ")
        user1 = User(firstName, lastName, avat)
    else:
        user1 = User(firstName, lastName)

    print(user1.__str__())
    
main()
