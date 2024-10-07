
# общее описание решения
Программа представляет из себя консольное приложение, которое производит вычисления для различных геометрических фигур

# описание каждой функции с примерами вызова
## canc
функция принимает название фигуры, требуемое вычисление и размеры фигуры
следом функцию вызывает соответсвующую функцию для вычисления и выводит результат

calc('circle', 'area', 1) : 3.141592653589793

## area
функция в зависимости от фигуры принимает от 1 до 3 значений и выводит площадь (для треугольника выводит полупериметр)

пример для вызова для квадрата
area(1) : 1

## perimeter
функция в зависимости от фигуры принимает от 1 до 3 значений и выводит периметр

пример для вызова для квадрата
area(1) : 4

# история изменения проекта с хешами комитов
-d76db2a: Add calculate.py
-51c40eb: Doc updated for triangle
-d080c78: Triangle added
-d078c8d: Docs added
-8ba9aeb: Circle and square added

# How to use calculator:
1. Run `python calculate.py`
2. Enter the figure name. Available are Circle, Square.
3. Enter the function: Area or Perimeter.
4. Enter figure sizes. Radius for circle, one side for square.
5. Get the answer!

# Math formulas
## Area
- Circle: `S = πR²`
- Rectangle: `S = ab`
- Square: `S = a²`
- Triangle: `S = sqrt(p * (p-a) * (p-b) * (p-c))` where p is semiperimeter

## Perimeter
- Circle: `P = 2πR`
- Rectangle: `P = 2a + 2b`
- Square: `P = 4a`
- Triangle: `P = a + b + c`

