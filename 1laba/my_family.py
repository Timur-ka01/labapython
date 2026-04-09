#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['mother', 'father', 'brother', 'cat']


# список списков приблизителного роста членов вашей семьи
my_family_height = [
    # ['имя', рост],
    ['N', '165'],
    ['A', '177'],
    ['R', '180'],
    ['K', '30']
]

def get_family_info():
    # Выведите на консоль рост отца в формате
    #   Рост отца - ХХ см
    father_height = my_family_height[1][1]
    
    # Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
    #   Общий рост моей семьи - ХХ см
    total_height = 0
    for i in range(0, 3):
        total_height += int(my_family_height[i][1])
        i += 1
    
    return {
        'father_height': father_height,
        'total_height': total_height
    }

if __name__ == "__main__":
    info = get_family_info()
    print('Рост отца -', info['father_height'])
    print('Общий рост моей семьи -', info['total_height'])