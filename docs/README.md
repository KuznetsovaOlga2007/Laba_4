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
Реализованы функции для вычисления площадей и периметров классичсеких геометрических фигур.

# Функции
## Для квадрата
### def perimeter(a): 
**Реализация и описание**
``` py
def perimeter(a):
	'''Принимает сторону квадрата, возвращает его периметр'''
    return 4 * a
```
**Примеры использования**
```py
print(perimeter(4))
>>> 16
print(perimeter(1))
>>> 4
```
### def area(a): 
**Реализация и описание**
``` py
def area(a):
	'''Принимает сторону квадрата, возвращает его площадь'''
    return a * a
```
**Примеры использования**
```py
print(perimeter(4))
>>> 16
print(perimeter(1))
>>> 1
```

## Для окружности
### def perimeter(a): 
**Реализация и описание**
``` py
import math
def perimeter(r):
	'''Принимает радиус окружности, возвращает длину окружности'''
    return 2 * math.pi * r
```
**Примеры использования**
```py
print(perimeter(4))
>>> 25.132741228718345
print(perimeter(1))
>>> 6.283185307179586
```
### def area(a): 
**Реализация и описание**
``` py
import math
def area(r):
	'''Принимает радиус окружности, возвращает площадь окружности''' 
	return math.pi * r * r
```
**Примеры использования**
```py
print(perimeter(4))
>>> 50.26548245743669
print(perimeter(1))
>>> 3.141592653589793
```
# История изменения проекта
``` cmd
commit d078c8d9ee6155f3cb0e577d28d337b791de28e2 (HEAD -> documentation, upstream/main, origin/main, origin/HEAD, forked-origin/main, main, develop)
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:55:29 2021 +0300

    L-03: Docs added

commit 8ba9aeb3cea847b63a91ac378a2a6db758682460
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:54:08 2021 +0300

    L-03: Circle and square added
```

