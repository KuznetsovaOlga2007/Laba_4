# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a

# Общее описание решения
## square.py
### def area(a) **Возвращает площадь квадрата**
- def area(a): *Параметры: принимает число a*
-	return a * a ~~Возвращаемое значение: а в квадрате~~
###def perimeter(a) **Возвращает периметр квадрата**
- def perimeter(a): ***Параметры: принимает число а***
-	return 4 * a <sub>Возвращаемое значение: произведение 4 и а</sub>
## circle.py import math <sup>Импортируем библиотеку math, чтобы подключить math.pi</sup>
### def area(r) *Возращает площадь круга*
- def area(r): *Принимаемое занчение: число r - радус круга*
-   return math.pi * r * r *Возращаемое значение : произведение пи на радиус в квадрате*
###def perimeter(r): *Возращает периметр круга*
def perimeter(r): *Принимаемое занчение: число r - радус круга*
    return 2 * math.pi * r *Возращаемое значение : произведение 2 на пи на радус круга*

#History
- |Wed Oct 9 19:54:16 2024 +0300|5243784|Dasha Ivanova|Add documentation to circle.py|
- |Wed Oct 9 19:52:27 2024 +0300|feda408|Dasha Ivanova|Add documentation to square.py|
- |Thu Mar 4 14:55:29 2021 +0300|d078c8d|smartiqa|Docs added|
- |Thu Mar 4 14:54:08 2021 +0300|8ba9aeb|smartiqa|Circle and square added|
