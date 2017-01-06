#Kristen Ching
import math
class Distance:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.distance = float(self.distance)

    def setAll(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.distance = float(self.distance)

    def calcDist(self):
        self.distance = math.sqrt(self.x2-self.x1)*(self.x2-self.x1) + (self.y2-self.y1)*(self.y2-self.y1)

    def returnDist(self):
        return self.distance

def main():
    x1 = int(input("Please enter the first x coordinate. "))
    x2 = int(input("Please enter the second x coordinate. "))
    y1 = int(input("Please enter the first y coordinate. "))
    y2 = int(input("Please enter the second y coordinate. "))

    new = Distance(x1, x2, y1, y2)

    print("With user input...")
    calcDist()
    print("The distance between", self.x1, ",", self.y1, "and", self.x2, ",", self.y2, "is", new.returnDist(self))

    print("With modifiers...")
    setAll()
    calcDist()
    print("The distance between", self.x1, ",", self.y1, "and", self.x2, ",", self.y2, "is", new.returnDist(self))
main()   
