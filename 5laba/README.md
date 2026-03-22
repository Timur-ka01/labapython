# Отчет
## Условие задачи
Создать генератор, который будет брать файл, и обрабатывать его по следующим условиям:
если строка больше допустимого лимита, то сделать срез строки
перевернуть каждую строку
## Описанеие проделанной работы 
задаем функцую f()
вводим переменную k которая распаковывает нужный файл
задаем лимит
заводим каждую строку нашего файла под цикл, задаем условие если строка по длине больше нашего лимита, обрезаем ее
вводим переменну word которая разбвает нашу строку в список
вводим переменую result в которой через map применяем изменение к каждому объекту. в map через лямбду вводим разворот входящей строки
соединяем нашу разбитую строку в целое через join
через yield возращаем результат тем самым делая генератор

## Результат программы 
![Uploading image.png…](https://github.com/Timur-ka01/labapython/blob/master/image/5laba.png?raw=true)

## Ссылки на используемые материалы 
1. [КЕГЭ](https://pythonru.com/biblioteki/kratkoe-rukovodstvo-po-biblioteke-python-requests)
3. [генератор python](https://skillbox.ru/media/code/generatory_python_chto_eto_takoe_i_zachem_oni_nuzhny/)
4. [time python](https://docs.python.org/3/library/time.html)
5. [map() python](https://skillbox.ru/media/code/funkciya-map-v-python-zachem-nuzhna-i-kak-ey-polzovatsya/)

