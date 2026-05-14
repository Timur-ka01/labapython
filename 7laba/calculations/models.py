from abc import ABC, abstractmethod

class Geo(ABC):
    @abstractmethod
    def area(self): pass

class Room(Geo):
    def __init__(self, w=0, l=0):
        self.w = w
        self.l = l
    
    @property
    def w(self):
        return self._w
    
    @w.setter
    def w(self, v):
        if v > 0:
            self._w = v
        else:
            self._w = 0   # если отрицательное - ставим 0
    
    def area(self): return self.w * self.l
    
    # Dunder-методы (ровно 2)
    def __str__(self): return f"Комната {self.w}x{self.l} = {self.area():.1f}м²"
    def __mul__(self, x): return Room(self.w * x, self.l * x)

class Apartment(Geo):
    def __init__(self):
        self.rooms = []
    
    def area(self): 
        s = 0
        for r in self.rooms:
            s = s + r.area()
        return s
    
    # Dunder-методы (ровно 2)
    def __str__(self): return f"Квартира: {len(self)} комн, {self.area():.1f}м²"
    def __len__(self): return len(self.rooms)

class Building(Geo):
    def __init__(self):
        self.apartments = []
    
    def area(self):
        s = 0
        for a in self.apartments:
            s = s + a.area()
        return s
    
    # Dunder-методы (ровно 2)
    def __str__(self): return f"Дом: {len(self)} кв, {self.area():.1f}м²"
    def __len__(self): return len(self.apartments)