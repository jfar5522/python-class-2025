try:
    import sys
    import os
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "classes")))

    import campers

except ModuleNotFoundError: 
    #You aren't using my file system, so make sure the module file is in the same place as this program!
    #To run this program with my file system in mind download it here on my github! https://github.com/jfar5522/python    
    import campers

class Automobile:
    maker = "Ford"
    def __init__(self,model,price):
        self._model = model
        self._price = price
        
    @property
    def model(self):
        return self._model
    @model.setter
    def model(self,s):
        self._model = s        

    @property
    def price(self):
        return self._price
    @price.setter
    def price(self,s):
        self._price = s

    @classmethod
    def changeCarMaker(cls, nMaker):
        cls.maker = nMaker



car=Automobile("Camry", 70000)
Automobile.maker = "Toyota"

car.model = "Revuelto"
Automobile.maker = "Lamborghini"
car.price = 1000000

print(car.maker, car.model, f"priced at ${car.price:,}")

car1=Automobile("Sedan", 60000)
car2=Automobile("SUV", 80000)
car3=Automobile("Highlander", 90000)
# Automobile.maker = "Toyota"

# car1.maker = "GM"
# car2.maker = "Honda"
# car3.maker = "BMW"

Automobile.changeCarMaker("Toyota")

print(car1.maker, car2.maker, car3.maker)

winnebago=campers.Winnebago()
airstream=campers.Airstream()
winnebago.weight=7000
airstream.weight=8000
