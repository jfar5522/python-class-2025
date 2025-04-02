class Animal:
    def __init__(self, w, h, wid):  
        self._weight=w
        self._height=h
        self._width=wid
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
        print("Animal eats")

class Mammal(Animal):
    def __init__(self, w, h, wid):
        super().__init__(h,w,wid)    
    paws = 4
    legs = 4
    eyes = 2
    fur = True
    warmBlooded = True
    tamed = False
    farmable = False


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

class Arachnid(Animal):
    def __init__(self, w, h, wid):
        super().__init__(h,w,wid)    
    legs = 8
    thorax = 1
    buildsWebs = True
    creepy = True
    food = "Insects"


class Dog(Mammal):    
    def eat(self):
        print("Dog eats")

class Bass(Fish):
    def eat(self):
        print("Bass eats")


class Spider(Arachnid):
    def eat(self):
        print("Spider eats")
