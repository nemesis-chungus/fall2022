class Package:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
    def dropOff(self, driver, truckNumber):
        print(f"Delivered {self.name} weighing {self.weight} pounds by {driver} of truck {truckNumber}")

def __init__(self, truckNumber):
    self.truckNumber = truckNumber

class AmazonTruck:
    truckNumber = 589
    packages = []
    driver = "nobody"

    def load(self, package):
        self.packages.append(package)   # add the package to the truck

    def deliver(self):
        for package in self.packages:
            package.dropOff(self.driver, self.truckNumber)

xbox = Package("xbox", "9")
tshirt = Package("tshirt", "0.5")
blades = Package("rollerblades", "6")


truck = AmazonTruck()
truck.driver = "Joe"
truck.load(xbox)
truck.load(tshirt)
truck.load(blades)

truck.deliver()
