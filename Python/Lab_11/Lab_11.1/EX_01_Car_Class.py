#Kristen Ching
class Car:
    def __init__(self, p, i , e, t):
        self.paint = p
        self.interior = i
        self.engine = e
        self.tires = t

    def setCustom(self, p, i, e, t):
        self.paint = p
        self.interior = i
        self.engine = e
        self.tires = t

    def getPaint(self):
        return self.paint
    def getInterior(self):
        return self.interior
    def getEngine(self):
        return self.engine
    def getTires(self):
        return self.tires

def main():
    p = input("Please enter the paint color you want for your car. ")
    i = input("Please enter the interior type you want for your car. ")
    e = input("Please enter the engine you want for your car. ")
    t = input("Please enter the tires you want for your car. ")

    print("example car...")
    car1 = Car("red w/ gold fleek", "Corinthian leather (Brown)", "5 litre v8 507hp", "20 inch Priellis")
    print("Your vehicle is ready...")
    print("Paint:\t", car1.getPaint())
    print("Interior:\t", car1.getInterior())
    print("Engine:\t", car1.getEngine())
    print("Tires:\t", car1.getTires())
    print("\n")

    print("Your car...")
    car1.setCustom(p, i, e, t)
    print("Your vehicle is ready...")
    print("Paint:\t", car1.getPaint())
    print("Interior:\t", car1.getInterior())
    print("Engine:\t", car1.getEngine())
    print("Tires:\t", car1.getTires())
    print("\n")

main()

class Human:
    def __init__(self, h, e , s):
        self.hair = h
        self.eyes = e
        self.skin = s

    def reset(self, h, e , s):
        self.hair = h
        self.eyes = e
        self.skin = s

    def gethair(self):
        return self.hair
    def getskin(self):
        return self.skin
    def geteyes(self):
        return self.eyes

def main():
    h = input("Please enter hair color. ")
    e = input("Please enter eye color. ")
    s = input("Please enter skin color. ")

    print("You...")
    driver1 = Human(h, e, s)
    print("Hair:\t", driver1.gethair())
    print("Eyes:\t", driver1.geteyes())
    print("Skin:\t", driver1.getskin())
    print("\n")

    print("Your friend...")
    driver1.reset("null", "nullobject", "0000000000")
    print("Hair:\t", driver1.gethair())
    print("Eyes:\t", driver1.geteyes())
    print("Skin:\t", driver1.getskin())
    print("\n")

main()

