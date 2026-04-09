#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# есть список животных в зоопарке

zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]

def manage_zoo():
    zoo_list = zoo.copy()
    
    # посадите медведя (bear) между львом и кенгуру
    #  и выведите список на консоль
    # TODO здесь ваш код
    for i in range(1, 4):
        zoo_list[-i] = zoo_list[-i - 1]
    zoo_list[1] = 'bear'
    
    # добавьте птиц из списка birds в последние клетки зоопарка
    birds = ['rooster', 'ostrich', 'lark', ]
    #  и выведите список на консоль
    # TODO здесь ваш код
    zoo_list.extend(birds)
    
    # уберите слона
    #  и выведите список на консоль
    # TODO здесь ваш код
    zoo_list.pop(3)
    
    # выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
    # Номера при выводе должны быть понятны простому человеку, не программисту.
    # TODO здесь ваш код
    positions = []
    for i in range(len(zoo_list)):
        if zoo_list[i] == 'lion' or zoo_list[i] == 'lark':
            positions.append(i + 1)
    
    return {
        'zoo': zoo_list,
        'positions': positions
    }

if __name__ == "__main__":
    result = manage_zoo()
    print(result['zoo'])
    for pos in result['positions']:
        print(pos)
    
