class Room:
    def __init__(self, width, length):
        self.width = width
        self.length = length


class Apartment:
    def __init__(self):
        self.rooms = []


class Building:
    def __init__(self):
        self.apartments = []