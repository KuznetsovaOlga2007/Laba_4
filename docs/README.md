# Math formulas
## Area
- Circle: S = πR²
Число [π](https://ru.wikipedia.org/wiki/%D0%9F%D0%B8_(%D1%87%D0%B8%D1%81%D0%BB%D0%BE)) - это отношение длины окружности к ее диаметру.
R - радиус круга.
```python 3
import math

def area(r):
    return math.pi * r * r
```
***Результат работы функции для числа r = 1:***
**3,1415926535897932384626433832795**

- Rectangle: S = ab
a - длина прямоугольника.
b - ширина прямоугольника.
```python 3
def area(a, b):
    return a * b
```
***Результат работы функции для a = 2 и b = 1:***
**2**

- Square: S = a²
a - сторона квадрата.
```python 3
def area(a):
    return a * a
```
***Результат работы функции для a = 2:***
**4**

- Triangle: S = ah/2
a - сторона треугольника.
h - высота треугольника, проведенная к стороне a.
```python 3
def area(a, h):
    return (a * h) / 2
```
***Результат работы функции для a = 2, h = 1:***
**1**
	
## Perimeter
- Circle: P = 2πR
Число [π](https://ru.wikipedia.org/wiki/%D0%9F%D0%B8_(%D1%87%D0%B8%D1%81%D0%BB%D0%BE)) - это отношение длины окружности к ее диаметру.
R - радиус круга.
```python 3
import math

def perimeter(r):
    return 2 * math.pi * r
```
***Результат работы функции для числа r = 0.5:***
**3,1415926535897932384626433832795**

- Rectangle: P = 2a + 2b
a - длина прямоугольника.
b - ширина прямоугольника.
```python 3
def perimeter(a, b):
    return (a + b) * 2
```
***Результат работы функции для a = 2, b = 1:***
**6**

- Square: P = 4a
a - сторона квадрата.
```python 3
def perimeter(a):
    return 4 * a
```
***Результат работы функции для a = 2:***
**8**

- Triangle: P = a+b+c
a, b, c - стороны треугольника.
```python 3
def perimeter(a, b, c):
    return a + b + c
```
***Результат работы функции для a = 2, b = 3, c = 2:***
**7**


**История коммитов:**
ca4a6ff7f79dd1d34751f7630f33894ad6b8d9bb
***Сохранение изменений в файлах circle.py, square.py, созданы файлы triangle.py, rectangle.py.***