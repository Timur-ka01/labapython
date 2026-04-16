from .area import square as calculate_square  # Переименовываем импорт

def power(area_value):  # Переименовываем параметр
    return area_value * 100

def power_room(room):
    area = room.width * room.length
    return power(area)

def power_apartment(apartment):
    total_area = 0  # Переименовываем переменную
    for room in apartment.rooms:
        total_area += room.width * room.length
    return power(total_area)

def power_building(building):
    total_area = 0  # Переименовываем переменную
    for apartment in building.apartments:
        for room in apartment.rooms:
            total_area += room.width * room.length
    return power(total_area)

def power_object(object):
    area = calculate_square(object)  # Используем переименованный импорт
    return power(area)