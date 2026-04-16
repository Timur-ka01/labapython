#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def calculate_area(radius):
    """
    Вычисляет площадь круга по формуле S = π * r^2
    radius: радиус круга (int или float)
    Возвращает площадь с точностью до 4 знаков после запятой (float)
    """
    pi = 3.1415926
    area = pi * (radius ** 2)
    return round(area, 4)

def is_point_inside_circle(point, radius, center=(0, 0)):
    """
    Проверяет, лежит ли точка внутри круга
    point: кортеж (x, y) — координаты точки
    radius: радиус круга
    center: кортеж (x, y) — координаты центра круга (по умолчанию (0, 0))
    Возвращает True, если точка внутри круга, иначе False
    """
    x, y = point
    cx, cy = center
    # Вычисляем расстояние от точки до центра круга
    distance = ((x - cx) ** 2 + (y - cy) ** 2) ** 0.5
    return distance < radius

def get_circle_info(radius):
    # Читаем радиус круга с входа пользователя
    # Выводим площадь круга с заданным радиусом
    area = calculate_area(radius)
    
    # Определяем координаты первой точки
    point_1 = (23, 34)
    # Проверяем, лежит ли точка внутри круга с радиусом 42 и центром в (0, 0)
    point_1_inside = is_point_inside_circle(point_1, radius)
    
    # То же самое для второй точки
    point_2 = (30, 30)
    point_2_inside = is_point_inside_circle(point_2, radius)
    
    return {
        'area': area,
        'point_1_inside': point_1_inside,
        'point_2_inside': point_2_inside
    }

if __name__ == "__main__":
    radius = int(input())
    info = get_circle_info(radius)
    print(info['area'])
    if info['point_1_inside']:
        print('True')
    else:
        print('False')
    if info['point_2_inside']:
        print('True')
    else:
        print('False')
