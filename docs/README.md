# Описание проекта 
Проект представляет собой несколько файлов, предназначенных для работы с геометрическими фигурами, написанных на python и объединённых в одну библиотеку

## Описание файлов
1. **circle.py** - функции для работы с кругами.
2. **rectangle.py** - функции для работы с прямоугольниками.
3. **square.py** - функции для работы с квадратами.

## Документация к модулям

## circle.py

Модуль для работы с кругами.

### Функции

### `area(r: double) -> double`

Вычисляет площадь круга по заданному радиусу.

**Параметры:**
- `r` (double): радиус круга.

**Возвращает:**
- double: площадь круга.

**Пример использования:**

```python
from circle import area

result = area(5)
print(result)  # Вывод: 78.539816
```

### `perimeter(r: double) -> double`

Вычисляет периметр (длину окружности) круга по заданному радиусу.

**Параметры:**
- `r` (double): радиус круга.

**Возвращает:**
- double: периметр круга.

**Пример использования:**

```python
from circle import perimeter

result = perimeter(5)
print(result)  # Вывод: 31.415927
```

---

## rectangle.py

Модуль для работы с прямоугольниками.

### Функции

### `area(a: double, b: double) -> double`

Вычисляет площадь прямоугольника по заданной ширине и высоте.

**Параметры:**
- `a` (double): ширина прямоугольника.
- `b` (double): высота прямоугольника.

**Возвращает:**
- double: площадь прямоугольника.

**Пример использования:**

```python
from rectangle import area

result = area(4, 5)
print(result)  # Вывод: 20
```

### `perimeter(a: double, b: double) -> double`

Вычисляет периметр прямоугольника по заданной ширине и высоте.

**Параметры:**
- `a` (double): ширина прямоугольника.
- `b` (double): высота прямоугольника.

**Возвращает:**
- double: периметр прямоугольника.

**Пример использования:**

```python
from rectangle import perimeter

result = perimeter(4, 5)
print(result)  # Вывод: 18
```

---

## square.py

Модуль для работы с квадратами.

### Функции

### `area(a: double) -> double`

Вычисляет площадь квадрата по заданному радиусу.

**Параметры:**
- `a` (double): сторона квадрата.

**Возвращает:**
- double: площадь квадрата.

**Пример использования:**

```python
from square import area

result = area(4)
print(result)  # Вывод: 16.0
```

### `perimeter(a: double) -> double`

Вычисляет периметр квадрата по заданному радиусу.

**Параметры:**
- `a` (double): сторона квадрата.

**Возвращает:**
- double: периметр треугольника.

**Пример использования:**

```python
from square import perimeter

result = perimeter(5)
print(result)  # Вывод: 20.0
```
---

### Хэши последних коммитов
* 438b89a1dfc58d90e9036fe431771427965cd1ff L-05: Add user agreement
* 6adb96248a4d00d3bea13bd95d78ef52352cd1b4 L-03: Docs added
| * 30494317cde4419be779c14306561e0eaa78b88b (HEAD -> feature, origin/feature) L-04: Add rectangle.py
| | * b5b0fae727ca72c317c383b39c0af73d6adcd81c (origin/develop) L-04: Update docs for calculate.py
| | * d76db2ac7f69cc920ae2e6f669fb0671a7fa7d71 L-04: Add calculate.py
| | * 51c40ebfd0e0b65f52fe5e54740cbb038e492db3 L-04: Doc updated for triangle
| | * d080c7888b81955bad2ed78d58ad910526b5132a L-04: Triangle added
| |/  
| * d078c8d9ee6155f3cb0e577d28d337b791de28e2 (origin/main, origin/HEAD, main) L-03: Docs added
|/  
* 8ba9aeb3cea847b63a91ac378a2a6db758682460 L-03: Circle and square added