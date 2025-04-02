#import function modules from the "lib" or "classes" folder. Make sure they are available and named correctly!
try:
    import sys
    import os
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "lib")))
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "classes")))

    import animal
   
except ModuleNotFoundError as e:
    print(f"{e}!\n"
        f"Please ensure the {e} module is named correctly and either:\n"
        "  - In the same directory as this program, or\n"
        "  - In the 'lib' or 'classes' folder one level above this program's directory.\n"
        "To use my file system setup, download it from: https://github.com/jfar5522/python-class-2025")
    sys.exit(f"Import failure! {e} available!")


dog = animal.Dog(5,5,5)
dog.eat()
bass = animal.Bass(5,5,5)
bass.eat()

print(dog.eyes)