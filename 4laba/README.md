# Отчет
## Условие задачи
1. написать функцию замыкаие для получение текста от API
2. написать декоратор ограничиывающий частоту вызова функции
## Описанеие проделанной работы 
импортируем библиотеку request для обращения к API
импортируем библиотеку time из которой возьмем фнукции для ограничения частоты вызова
создаем функцию f(), в ней создаем еще одну функцию f1(), это и будет замыкание
в функции f1() вводим переменую r в коорой делаем запрос к API и возращаем объект
с помощью json разбираем текст ответа в формат словаря
в переменной n обращаемся к нужным данным 
и возращаем переменную n

создаем функцию limit_calls(x), которая будет слыжить декоратором
задаем переменную которая будет содержать данные последнего вызова last_calls
вводим функцию wrapper()
для того что бы работать с переменной из внешней функции используем nonlocal last_call
вводим переменню now которая хранит в себе текущее время 
сравниваем текущее время и время последнего вызова функции, если прошлом меньше двух секунд, то функция не выполняеться, если больше то функция выполняеться, и значение last_call обновляеться

## Результат программы 
![[https://github.com/Timur-ka01/labapython/blob/master/image/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202026-03-10%20182330.png?raw=true](https://github.com/Timur-ka01/labapython/blob/master/image/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202026-03-10%20182406.png?raw=true)](https://github.com/Timur-ka01/labapython/blob/master/image/4laba.png?raw=true)

## Ссылки на используемые материалы 
1. [Вложенные списки питон](https://sky.pro/wiki/python/rabota-s-vlozhennymi-spiskami-v-python/)
2. [обход списка с произвольной вложенностью](https://www.reddit.com/r/learnpython/comments/ic7s4b/traversing_an_arbitrarily_nested_list/?tl=ru&rdt=33433)
3. [Функция isinstance](https://docs-python.ru/tutorial/vstroennye-funktsii-interpretatora-python/funktsija-isinstance/)
4. [Функция extend](https://sky.pro/wiki/python/metod-extend-v-python-dobavlenie-neskolkih-elementov-v-spisok/)


