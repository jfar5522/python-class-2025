import automobileparts

class Automobile:
    def __init__(self):
        self._make=""
        self._model = ""
        self.paint = ""
        self._tires = []
        self._doors = []
        for i in range(4):
            self._tires.append(automobileparts.Tire())
            self._tires.append(automobileparts.Door())
        self._engine=automobileparts.Engine()
        self._steeringWheel = automobileparts.SteeringWheel
        print("Automobile created")

    @property
    def make(self):
        return self._make
    @make.setter
    def make(self,val):
        self._make = val

    @property
    def model(self):
        return self._model
    @model.setter
    def model(self, val):
        self._model = val

    @property
    def paint(self):
        return self._paint
    @paint.setter
    def paint(self, val):
        self._paint = val

    