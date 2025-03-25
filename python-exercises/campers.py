class Winnebago:
    def __init__(self):
        self._weight = 0

        print ("Winnebago built")

    @property
    def weight(self):
        return self._weight   
    @weight.setter
    def weight(self, s):
        self._weight = s
        
    

class Airstream:
    def __init__(self):
        self._weight = 0

        print ("Airstream built")
        
    @property
    def weight(self):
        return self._weight   
    @weight.setter
    def weight(self, s):
        self._weight = s