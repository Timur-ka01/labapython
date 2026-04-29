from abc import ABC, abstractmethod

class Geo(ABC):
    @abstractmethod
    def area(self): pass

class Room(Geo):
    def __init__(self, w=0, l=0):
        self._w = w
        self._l = l
    
    @property
    def w(self): return self._w
    @w.setter
    def w(self, v):
        if v > 0: self._w = v
    
    @property
    def l(self): return self._l
    @l.setter
    def l(self, v):
        if v > 0: self._l = v
    
    def area(self): return self.w * self.l
    def __str__(self): return f"Комната {self.w}x{self.l} = {self.area():.1f}м²"
    def __mul__(self, x): return Room(self.w * x, self.l * x)

class Apartment(Geo):
    def __init__(self):
        self.rooms = []
    def area(self): return sum(r.area() for r in self.rooms)
    def __str__(self): return f"Квартира: {len(self)} комн, {self.area():.1f}м²"
    def __len__(self): return len(self.rooms)
    def __getitem__(self, i): return self.rooms[i]

class Building(Geo):
    def __init__(self):
        self.apartments = []
    def area(self): return sum(a.area() for a in self.apartments)
    def __str__(self): return f"Дом: {len(self)} кв, {self.area():.1f}м²"
    def __len__(self): return len(self.apartments)