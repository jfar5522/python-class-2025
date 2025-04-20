class Animal:
    pass

class Lion(Animal):
    def __repr__(self):
        return super().__repr__()

class Tiger(Animal):
    pass

class Bear(Animal):
    pass


class Zoo:
    def __init__(self):
        self.animals = []
    def addAnimal(self, a):
        self.animals.append(a)

    def __len__(self):
        return len(self.animals)
    
    def __getitem__(self, index):
        return self.animals[index]
    
    def __setitem__(self, index, animal):
        self.animals[index] = animal
    def __delitem__(self, index):
        del self.animals[index]

    def __iter__(self):
        self.currentIndex = 0
        return self
    
    def __next__(self):
        if self.currentIndex >= len(self.animals):
            raise StopIteration
        index=self.currentIndex
        self.currentIndex += 1
        return self.animals[index]
    
    def __contains__(self, animal):
        for a in self.animals:
            if animal == a:
                return True
        return False
    
myZoo = Zoo()
myZoo.addAnimal(Lion())
myZoo.addAnimal(Tiger())
myZoo.addAnimal(Bear())

print(len(myZoo))
myZoo[0] = Tiger()
print(myZoo[0])


    