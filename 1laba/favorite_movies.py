#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть строка с перечислением фильмов

my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

# Выведите на консоль с помощью индексации строки, последовательно:
#   первый фильм
#   последний
#   второй
#   второй с конца

# Запятая не должна выводиться.  Переопределять my_favorite_movies нельзя
# Использовать .split() или .find()или другие методы строки нельзя - пользуйтесь только срезами,
# как указано в задании!

def get_movies():
    # TODO здесь ваш код
    return {
        'first': my_favorite_movies[0:10],
        'last': my_favorite_movies[-15:],
        'second': my_favorite_movies[12:25],
        'second_last': my_favorite_movies[-22:-17]
    }

if __name__ == "__main__":
    movies = get_movies()
    print(movies['first'])
    print(movies['last'])
    print(movies['second'])
    print(movies['second_last'])