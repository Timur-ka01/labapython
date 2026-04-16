from .models import Room, Apartment, Building

def square_room(room):
    return room.width * room.length

def square_apartment(apartment):
    t = 0
    for room in apartment.rooms:
        t += square_room(room)
    return t

def square_building(building):
    t = 0
    for apartment in building.apartments:
        t += square_apartment(apartment)
    return t

def square(object):
    if isinstance(object, Room):
        return square_room(object)
    elif isinstance(object, Apartment):
        return square_apartment(object)
    elif isinstance(object, Building):
        return square_building(object)
    
