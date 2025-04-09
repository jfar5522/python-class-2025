try:
    import sys
    import os
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "lib")))
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "classes")))

    import aniactions
   
except ModuleNotFoundError as e:
    print(
        f"{e}! Please ensure the module is named correctly and either:\n"
        "  - In the same directory as this program, or\n"
        "  - In the 'lib' or 'classes' folder one level above this program's directory.\n"
        "To use my file system setup, download it from: https://github.com/jfar5522/python-class-2025")
    sys.exit(f"Import failure! {e} available!")




class Animal:
    def __init__(self, w, h, wid):  
        self._weight=w
        self._height=h
        self._width=wid
    
    def __str__(self):
        return f"{self.__class__.__name__} weighs {self.weight:,}lb has a height of {self.height:,}ft and a width of {self.width:,}ft"
        
        
    @property
    def weight(self):
        return self._weight
    @weight.setter
    def weight(self, val):
        self._weight = val
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, val):
        self._height = val
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self, val):
        self._width = val
    
    
    def eat(self):
        print(f"{self.__class__.__name__} eats")

class Mammal(Animal):
    def __init__(self, w, h, wid):
        super().__init__(h,w,wid)    
    
    arms = 0
    hands = 0
    paws = 4
    legs = 4
    eyes = 2
    fur = True
    hair = True
    whiskers = False
    warmBlooded = True
    tamed = False
    domesticated = False

class Avian(Animal):
    def __init__(self, w, h, wid):
        super().__init__(h,w,wid)
    
    wings = 2
    legs = 2
    talons = 0
    canFly = True
    warmBlooded = True
    



class Reptile(Animal):
    def __init__(self, w, h, wid):
        super().__init__(h,w,wid)  

    feet = 4
    legs = 4
    scales = True
    coldBlooded = True



class Fish(Animal):
    def __init__(self, w, h, wid):
        super().__init__(h,w,wid)  

    eyes = 2
    scales = True


class Insect(Animal):
    def __init__(self, w, h, wid):
        super().__init__(h,w,wid)  

    legs = 6
    thorax = 3
    wings = 0
    canFly = False

class Arachnid(Animal):
    def __init__(self, w, h, wid):
        super().__init__(h,w,wid)    

    legs = 8
    thorax = 1
    buildsWebs = True
    creepy = True
    food = "Insects"


class Dog(Mammal):
    tamed = True
    domesticated = True
    
class Bass(Fish):
    pass

class Spider(Arachnid):
    pass


class Clifford(Dog):
    def __init__(self, w=174165, h=25, wid=5):
        super().__init__(h,w,wid) 
    