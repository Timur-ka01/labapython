#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Верхнеуровневый модуль, который использует логику из модулей-заданий
"""

from __init__ import (
    get_distances,
    calculate_area,
    is_point_inside_circle,
    calculate_expression,
    get_movies,
    get_family_info,
    manage_zoo,
    calculate_song_times,
    decrypt_message,
    analyze_flowers,
    get_best_prices,
    calculate_store_items
)

def main():
    print("=" * 60)
    print("ЗАДАНИЕ 00: Расстояния между городами")
    print("=" * 60)
    distances = get_distances()
    for city, dist in distances.items():
        print(f"{city}: {dist}")
    
    print("\n" + "=" * 60)
    print("ЗАДАНИЕ 01: Площадь круга и точки")
    print("=" * 60)
    print(f"Площадь круга радиусом 42: {calculate_area(42)}")
    print(f"Точка (23,34) внутри круга: {is_point_inside_circle((23,34), 42)}")
    print(f"Точка (30,30) внутри круга: {is_point_inside_circle((30,30), 42)}")
    
    print("\n" + "=" * 60)
    print("ЗАДАНИЕ 02: Операции с числами")
    print("=" * 60)
    print(f"1 * (2 + 3) * 4 + 5 = {calculate_expression()}")
    
    print("\n" + "=" * 60)
    print("ЗАДАНИЕ 03: Любимые фильмы")
    print("=" * 60)
    movies = get_movies()
    print(f"Первый фильм: {movies['first']}")
    print(f"Последний фильм: {movies['last']}")
    print(f"Второй фильм: {movies['second']}")
    print(f"Второй с конца: {movies['second_last']}")
    
    print("\n" + "=" * 60)
    print("ЗАДАНИЕ 04: Моя семья")
    print("=" * 60)
    family_info = get_family_info()
    print(f"Рост отца: {family_info['father_height']} см")
    print(f"Общий рост семьи: {family_info['total_height']} см")
    
    print("\n" + "=" * 60)
    print("ЗАДАНИЕ 05: Зоопарк")
    print("=" * 60)
    zoo_info = manage_zoo()
    print(f"Зоопарк: {zoo_info['zoo']}")
    print(f"Клетки lion и lark: {zoo_info['positions']}")
    
    print("\n" + "=" * 60)
    print("ЗАДАНИЕ 06: Песни")
    print("=" * 60)
    songs_info = calculate_song_times()
    print(f"Три песни звучат: {songs_info['first_three']} минут")
    print(f"Другие три песни звучат: {songs_info['second_three']} минут")
    
    print("\n" + "=" * 60)
    print("ЗАДАНИЕ 07: Секретное сообщение")
    print("=" * 60)
    print(f"Расшифрованное сообщение: {decrypt_message()}")
    
    print("\n" + "=" * 60)
    print("ЗАДАНИЕ 08: Сад и луг")
    print("=" * 60)
    flowers = analyze_flowers()
    print(f"Все цветы: {flowers['all_flowers']}")
    print(f"Общие цветы: {flowers['common']}")
    print(f"Только в саду: {flowers['only_garden']}")
    print(f"Только на лугу: {flowers['only_meadow']}")
    
    print("\n" + "=" * 60)
    print("ЗАДАНИЕ 09: Магазины")
    print("=" * 60)
    sweets = get_best_prices()
    for product, shops_list in sweets.items():
        print(f"{product}: {shops_list}")
    
    print("\n" + "=" * 60)
    print("ЗАДАНИЕ 10: Склад")
    print("=" * 60)
    store_items = calculate_store_items()
    for item, info in store_items.items():
        print(f"{item} - {info['quantity']} шт, стоимость {info['cost']} руб")

if __name__ == "__main__":
    main()