# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a

## File circle.py
- import math - Эта строка импортирует библиотеку math.pi. Библиотека math.pi предоставляет доступ к математическим константам и функциям, в нашем случае требуется число Пи.
- def area(r): - Создает функцию под названием area, которая принимает аргумент r(радиус круга).
- return math.pi * r * r - Эта строка вычисляет площадь круга. math.pi - это константа, число Пи. return возвращает результат вычисления из функции area.
- def perimeter(r): - Создает функцию под названием perimeter, которая принимает аргумент r (радиус круга).

- return 2 * math.pi * r - Эта строка выполняет вычисление периметра круга. 2 * math.pi * r -  вычисляет длину окружности. return возвращает результат вычисления  из функции perimeter.

## File square.py
- def area(a): - Создает функцию под названием area, которая принимает аргумент a(сторона квадрата).
- return a * a -  Вычисляет квадрат числа a. return возвращает результат вычисления из функции area.
- def perimeter(a): -  Определяет функцию с именем perimeter, которая принимает аргумент a(сторона квадрата).
- return 4 * a - Вычисляет периметр квадрата. return возвращает результат вычисления из функции perimeter.
# Area
## Описание
Функция вычисляет площадь круга
## Параметры
* r - радиус круга
## Возвращает значение 
*  Площадь круга
## Примеры
* >area(5)
  > >78.53981633974483
# perimeter
## Описание
Функция вычисляет периметр круга
## Параметры
* r - радиус круга
## Возвращает значение 
*  Периметр круга
## Примеры
* >perimeter(5)
  > >31.415955359
# Area
## Описание
Функция вычисляет площадь квадрата
## Параметры
* a - сторона квадрата
## Возвращает значение 
*  Площадь квадрата
## Примеры
* >area(2)
  > >4
# perimeter
## Описание
Функция вычисляет периметр квадрата
## Параметры
* a - сторона квадрата
## Возвращает значение 
* Периметр квадрата
## Примеры
* >perimeter(2)
  > >8

#History
commit d2b9714fa3fd05fd1cf27b79c1fd32b3482fe3fe (HEAD -> main)
Author: Alexandra Smirnova <smirnovaad13@gmail.com>
Date:   Wed Oct 9 21:17:43 2024 +0300

    Add documentation to circle.py

commit ff6a2a6a274ab5c5740a1b14d024540307e8bfe5
Author: Alexandra Smirnova <smirnovaad13@gmail.com>
Date:   Wed Oct 9 21:15:38 2024 +0300

    Add documentation to square.py

commit d078c8d9ee6155f3cb0e577d28d337b791de28e2 (origin/main, origin/HEAD)
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:55:29 2021 +0300

    L-03: Docs added

commit 8ba9aeb3cea847b63a91ac378a2a6db758682460
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:54:08 2021 +0300

    L-03: Circle and square added
