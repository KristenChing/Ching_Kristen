#Kristen Ching
import math
class Distance:
    def __init__(self, x1, y1, x2, y2):
        self.xOne = x1
        self.xTwo = x2
        self.yOne = y1
        self.yTwo = y2
        self.distance = 0

    def setValues(self, x1, y1, x2, y2):
        self.xOne = x1
        self.xTwo = x2
        self.yOne = y1
        self.yTwo = y2
        self.distance = 0

    def getDist(self):
        self.distance = math.sqrt((self.xTwo - self.xOne)**2 + (self.yTwo - self.yOne)**2)
        return self.distance
    def getxOne(self):
        return self.xOne
    def getyOne(self):
        return self.yOne
    def getxTwo(self):
        return self.xTwo
    def getyTwo(self):
        return self.yTwo


def main():
    x1 = int(input("Please enter the first x coordinate. "))
    x2 = int(input("Please enter the second x coordinate. "))
    y1 = int(input("Please enter the first y coordinate. "))
    y2 = int(input("Please enter the second y coordinate. "))

    print("With user input...")
    new = Distance(x1, y1, x2, y2)
    print("The distance between", new.getxOne(), ",", new.getyOne(), "and", new.getxTwo(), ",", new.getyTwo(), "is", new.getDist())

    print("With modifiers...")
    new.setValues(2, 2, 3, 3)
    print("The distance between", new.getxOne(), ",", new.getyOne(), "and", new.getxTwo(), ",", new.getyTwo(), "is", new.getDist())
main()  
