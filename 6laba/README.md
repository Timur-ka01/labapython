# Отчет
## Условие задачи
Сделать программу, которая считает площадь и тепло для комнаты, квартиры или дома. Тепло считается по формуле 100 Вт на 1 м². Еще нужно сохранять результат в Word и Excel.
## Описанеие проделанной работы 
Написал классы для объектов
В файле models.py создал три класса: Room (комната с шириной и длиной), Apartment (квартира, в которой есть список комнат) и Building (дом, в котором есть список квартир).

### Сделал расчет площади
В area.py написал функции:

square_room() – умножает ширину на длину.

square_apartment() – суммирует площади всех комнат.

square_building() – суммирует площади всех квартир.

square() – универсальная функция, которая сама определяет тип объекта.

### Сделал расчет тепла
В heat.py написал функцию power(), которая умножает площадь на 100. Для удобства сделал общую функцию power_object().

### Сделал интерфейс
В main.py на tkinter сделал окошко с:

переключателем (комната / квартира / дом)

полями для ввода данных (размеры комнат, этажи, количество квартир и т.д.)

кнопками "Рассчитать", "Сохранить в файл" и "История БД" (историю делал, но ее убрали).

### Сохранение в файлы
С помощью библиотек python-docx и openpyxl реализовал сохранение последнего результата в report.docx и report.xlsx.

## Результат программы 
![[Uploading image.png…](https://github.com/Timur-ka01/labapython/blob/master/image/5laba.png?raw=true)](https://github.com/Timur-ka01/labapython/blob/master/image/labaa6.png?raw=true)

## Ссылки на используемые материалы 
1. [КЕГЭ](https://pythonru.com/biblioteki/kratkoe-rukovodstvo-po-biblioteke-python-requests)
3. [генератор python](https://skillbox.ru/media/code/generatory_python_chto_eto_takoe_i_zachem_oni_nuzhny/)
4. [time python](https://docs.python.org/3/library/time.html)
5. [map() python](https://skillbox.ru/media/code/funkciya-map-v-python-zachem-nuzhna-i-kak-ey-polzovatsya/)
