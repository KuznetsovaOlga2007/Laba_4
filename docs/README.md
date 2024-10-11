# Geometric Library

Geometric Library is a Python library designed to perform geometric calculations. This library provides various functions to calculate areas, perimeters, and volumes of different geometric shapes, including circles, rectangles, and spheres.

## Key Features:
- Calculate area and perimeter for various shapes.
- Efficient algorithms for geometric computations.
- Easy to integrate with other projects.

## Функции библиотеки

### `square(n)`
Принимает число n, возвращает квадрат числа n.

- **Параметры**:
  - `n` (int или float): число для возведения в квадрат.
  
- **Возвращает**: 
  - (int или float): квадрат числа n.

- **Пример использования**:
  ```python
  result = square(4)  # Возвращает 16


commit fa14753d730ee63ebb1aa631d4171521b5f427a0 (HEAD -> docs/feature, origin/docs/feature)
Author: Darth Vader <iurmantaev@mail.ru>
Date:   Fri Oct 11 21:18:13 2024 +0300

    Добавлена документация к функциям

commit b5b0fae727ca72c317c383b39c0af73d6adcd81c (origin/develop, develop)
Author: Daniil.K <dlkay@yandex.ru>
Date:   Tue Mar 30 18:02:23 2021 +0300

    L-04: Update docs for calculate.py

commit d76db2ac7f69cc920ae2e6f669fb0671a7fa7d71
Author: Daniil.K <dlkay@yandex.ru>
Date:   Tue Mar 30 17:57:42 2021 +0300

    L-04: Add calculate.py

commit 51c40ebfd0e0b65f52fe5e54740cbb038e492db3
Author: smartiqa <info@smartiqa.ru>
Date:   Fri Mar 26 14:52:26 2021 +0300

:











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

