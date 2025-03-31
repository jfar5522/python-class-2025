#THIS IS THE MAIN FILE
#Got bugs? Please let me know!

#import function modules from the "lib" or "classes" folder. Make sure they are available and named correctly!
try:
    import sys
    import os
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "lib")))
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "classes")))

    import carfactory
   
except ModuleNotFoundError as e:
    print(f"{e}!\n"
        f"Please ensure the {e} module is named correctly and either:\n"
        "  - In the same directory as this program, or\n"
        "  - In the 'lib' or 'classes' folder one level above this program's directory.\n"
        "To use my file system setup, download it from: https://github.com/jfar5522/python-class-2025")
    sys.exit(f"Import failure! {e} available!")


#NOTE, create an infinte loop for users to input their own cars to build and then have those cars be put into a file for
#future reference! Would be an interesting project wouldn't you say?
factory = carfactory.CarFactory()
car1 = factory.buildCar("BMW","M3","Maroon")
car2 = factory.buildCar("Toyota", "Camri", "Indigo")
print(factory.numberOfBuiltCars)
print(car1.make)
print(car1.model)
print(car1.paint + "\n")
print(car2.make)
print(car2.model)
print(car2.paint)


