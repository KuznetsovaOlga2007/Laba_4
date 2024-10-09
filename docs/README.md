# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a

.4 Введите размеры фигуры. Радиус для круга, одна сторона для квадрата.
.5 Получите ответ!

# Общее описание
## Файл circle.py 
- import math — импортируем библиотеку math. Он предоставляет доступ к математическим функциям и константам, таким как число Пи (math.pi). Благодаря ему мы можем использовать math.pi.

- def area(r): — определяет функцию под названием area, которая принимает один аргумент r. r — это переменная, которая хранит значение радиуса, переданное в функцию.

- return math.pi * r * r вычисляем площадь круга. math.pi — это константа, представляющая число Пи. r * r — это радиус в квадрате. return возвращает результат вычисления из функции area.

- def периметр(r): — определяем функцию под названием периметр, которая принимает один аргумент r.

- return 2 * math.pi * r — эта строка вычисляет периметр круга. 2 * math.pi * r — вычисляет длину окружности. return возвращает результат вычисления.

## Файл square.py 
- def area(a): — определяем функцию с именем area, она принимает аргумент a (переменная, которая будет хранить значение, переданное в функцию).
- return a * a — вычисляем квадрат числа a. return возвращает результат вычисления.
- def perimeter(a): — определяем функцию с именем perimeter, она принимает один аргумент a.
- return 4 * a — вычисляет 4, умноженное на a. return возвращает результат вычисления.

# Область
## Описание
Функция вычисляет площадь круга
## Параметры
** *r** (float) радиус круга
## Возвращает значение 
* (float) Площадь круга
## Примеры
* >область (5)
  > >78.53981633974483
# периметр
## Описание
Функция вычисляет периметр круга
## Параметры
** *r** (float) радиус круга
## Возвращает значение 
* (float) Периметр круга
## Примеры
* >периметр(5)
  > >31.415955359
# Область
## Описание
Функция вычисляет площадь квадрата
## Параметры
** *a** (int) сторона квадрата
## Возвращает значение 
* (int) Площадь квадрата
## Примеры
* >область (5)
  > >25
# периметр
## Описание
Функция вычисляет периметр квадрата
## Параметры
** *r** (int) сторона квадрата
## Возвращает значение 
* (int) Периметр квадрата
## Примеры
* >периметр(5)
  > >20
   
   commit b2fb01d47a7b32b47e2710e0f9f29666322dab0c (HEAD -> main)
Author: Polina Yakovleva <yakovlevap146gmail.com>
Date:   Wed Oct 9 22:46:10 2024 +0300

    Added documentation to circle

commit 0b1200f7bd33e0cba4ac41e4d6818b51f91b2fb5
Author: Polina Yakovleva <yakovlevap146gmail.com>
Date:   Wed Oct 9 22:45:48 2024 +0300

    Added documentation to square

commit d078c8d9ee6155f3cb0e577d28d337b791de28e2 (origin/main, origin/HEAD)
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:55:29 2021 +0300

    L-03: Docs added

commit 8ba9aeb3cea847b63a91ac378a2a6db758682460
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:54:08 2021 +0300

    L-03: Circle and square added

# История
- Wed Oct 9 22:46:10 2024 +0300 | b2fb01d | Polina Yakovleva | Added documentation to circle
- Wed Oct 9 22:45:48 2024 +0300 | 0b1200f |Polina Yakovleva  | Added documentation to square
- Thu Mar 4 14:55:29 2021 +0300 | d078c8d | smartiqa | L-03: Docs added
- Thu Mar 4 14:54:08 2021 +0300| 8ba9aeb | smartiqa | L-03: Circle and square added

