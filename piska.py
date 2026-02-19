zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]

# посадите медведя (bear) между львом и кенгуру
#  и выведите список на консоль
# TODO здесь ваш код
zoo.append('')
for i in range(1, 4):
    zoo[-i] = zoo[-i - 1]

print(zoo)
 
