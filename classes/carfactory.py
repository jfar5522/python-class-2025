import cars

class CarFactory:
    numberOfBuiltCars = 0 
    def __init__(self):
 
        print("CarFactory created")

    @classmethod
    def addAnotherCar(cls):
        cls.numberOfBuiltCars += 1

    def buildCar(self, make, model, paint):
        car = cars.Automobile()
        car.make = make
        car.model = model 
        car.paint = paint
        CarFactory.addAnotherCar()
        return car
    