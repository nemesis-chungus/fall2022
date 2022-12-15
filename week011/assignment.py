class Package:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
    def dropOff(self, driver):
        print(f"Delivered {self.name} weighing {self.weight} pounds by {driver} of truck {truck.Number}")

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
            package.dropOff(self.driver)

xbox = Package("xbox")
xbox.weight = ("9")
tshirt = Package("tshirt")
tshirt.weight = ("0.5")
blades = Package("rollerblades")
blades.weight = ("6")

truck = AmazonTruck()
truck.driver = "Joe"
truck.load(xbox)
truck.load(tshirt)
truck.load(blades)

truck.deliver()
