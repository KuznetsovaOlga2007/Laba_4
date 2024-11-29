**Описание:**  
Этот проект содержит функции для расчета площади и периметра для трех геометрических фигур: круга, прямоугольника и квадрата. Каждая функция принимает необходимые параметры для вычислений и возвращает соответствующее значение. Код написан на Python и структурирован в виде отдельных модулей.

## Area
- **Circle**: \( S = \pi R^2 \)
- **Rectangle**: \( S = ab \)
- **Square**: \( S = a^2 \)

## Perimeter
- **Circle**: \( P = 2 \pi R \)
- **Rectangle**: \( P = 2a + 2b \)
- **Square**: \( P = 4a \)

---

## Commit History

- **commit `249284dd9b0a442121469cc59f429ecff9ca942f` (HEAD -> documentation)**  
  **Message**: add rectangle.py and and commented it  

- **commit `ab1e33a91d4ac29697e254ebbc3bd247e2495f4c`**  
  **Message**: commented out the functions  

- **commit `d078c8d9ee6155f3cb0e577d28d337b791de28e2` (origin/main, origin/HEAD, release, main, feature, develop)**   
  **Message**: L-03: Docs added  

- **commit `8ba9aeb3cea847b63a91ac378a2a6db758682460`**  
  **Message**: L-03: Circle and square added  

# Проект для вычисления площадей и периметров

### Функция `area`
**Файлы:**
- [rectangle.py](../rectangle.py)
- [circle.py](../circle.py)
- [square.py](../square.py)
- [triangle.py](../triangle.py)

**Описание:**  
Вычисляет площадь круга, прямоугольника, квадрата и треугольника на основе их сторон(ы) `a` или радиуса `r` (в зависимости от фигуры).

**Параметры:**  
- `r` (float): Радиус круга.
- `a` (int): Сторона квадрата.
- `a` (int) `b` (int): Стороны прямоугольника.
- `a` (int) `h` (int): Сторона и высота треугольника.

**Возвращает:**  
- `float`: Площадь круга.
- `int`: Площадь квадрата.
- `int`: Площадь прямоугольника.
- `int`: Площадь треугольника.


**Применение:**
```python
from circle.py import area
print(area(5))  # Ожидаемый результат: 78.53

from rectangle.py import area
print(area(5,4)) # Ожидаемый результат: 20

from square.py import area
print(area(3)) # Ожидаемый результат: 9

from triangle.py impoer area
print(area(4,5)) # Ожидаемый резльтат: 10
```
### Функция `perimeter`
**Файлы:**
- [rectangle.py](../rectangle.py)
- [circle.py](../circle.py)
- [square.py](../square.py)
- [triangle.py](../triangle.py)


**Описание:**  
Вычисляет длину окружности, квадрата, прямоугольника или треугольника на основе ее сторон(ы) `a` или радиуса `r`.

**Параметры:**  
- `r` (float): Радиус круга.
- `a` (int): Сторона квадрата.
- `a` (int) `b` (int): Стороны прямоугольника.
- `a` (int) `b` (int) `c` (int): Стороны треугольника.

**Возвращает:**  
- `float`: Длинну окружности.
- `int`: Периметр квадрата.
- `int`: Периметр прямоугольника.
- `int`: Периметр треугольника.

**Применение:**
```python
from rectangle.py import perimeter
print(perimeter(2,3))  # Ожидаемый результат: 10

from circle.py import perimeter
print(perimeter(3))  # Ожидаемый результат: 12.56

from square.py import perimeter
print(perimeter(5))  # Ожидаемый результат: 20

from triangle.py import perimeter
print(perimeter(5,4,3))  # Ожидаемый результат: 12
```