#Kristen Ching
class MPH:
    def __init__(self, dist, hours, mins):
        self.distance = dist
        self.hours = hours
        self.minutes = mins
        self.mph = 0

    def setAll(self, dist, hours, mins):
        self.distance = dist
        self.hours = hours
        self.minutes = mins
        self.mph = 0

    def getHours(self):
        return self.hours
    def getMins(self):
        return self.minutes
    def getDist(self):
        return self.distance

    def findMPH(self):
        self.mph = self.distance/(self.hours + self.minutes/60)
        return self.mph

def main():
    dist = int(input("Please enter a distance. "))
    hours = int(input("Please enter a time (hours). "))
    mins = int(input("Please enter a time (minutes). "))

    print("From inputs... ")
    new = MPH(dist, hours, mins)
    print(new.getDist(), "in", new.getHours(), " hours and ", new.getMins(), "minutes = ", new.findMPH(), "mph.")

    print("Using modifiers.... ")
    new.setAll(433, 4, 40)
    print(new.getDist(), "in", new.getHours(), " hours and ", new.getMins(), "minutes = ", new.findMPH(), "mph.")
main()
