class Automobile:
    def __init__(self, price, model):
        self.weight = 0
        self._weight = self.weight
        self.milage = 0 
        self._mileage = self.milage
        self.price = price
        self._price = self.price
        self.model = model

    @property
    def weight(self):
        return self._weight
    @weight.setter
    def weight(self, s):
        self._weight = s

    @property
    def mileage(self):
        return self._mileage
    @mileage.setter
    def mileage(self, s):
        self._mileage = s 

    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, s):
        self._price = s              

    def __str__(self):
        return f"This car is a {self.model} model, it weighs {self.weight}, it has a mileage of {self.milage} and it costs ${self.price:,}"
    
    def calculatePrice(self):
        if self.milage > 200000:
            self.price = 10000
        else:
            self.price = 40000
    
    def driveCar100000Miles(self):
        self.milage += 100000




bronco = Automobile("bronco",37995)
civic = Automobile("civic", 24250)

bronco.weight = 4960
bronco.milage = 200001
civic.weight = 6100
civic.milage = 30000

print(bronco)
print(civic)

bronco.calculatePrice()

civic.calculatePrice()

i = 0
for i in range(3):
    bronco.driveCar100000Miles()
    civic.calculatePrice()

# i = 0
# for i in range(3):
#     civic.driveCar100000Miles()

bronco.calculatePrice()    
civic.calculatePrice()

print(bronco)
print(civic)

