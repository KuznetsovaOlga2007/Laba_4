<<<<<<< HEAD

# How to use calculator:
1. Run `python calculate.py`
2. Enter the figure name. Available are Circle, Square.
3. Enter the function: Area or Perimeter.
4. Enter figure sizes. Radius for circle, one side for square.
5. Get the answer!
=======
# Общее описание решения
**Geometric Lib** - библиотека, написанная на Python, предоставляющая функция для вычисления геометрических характеристик фигур (прямоугльник, квадрат, окружность). Библиотеку можно использовать в других проектах, импортировав ее и соответствующие функции.

**Возможности**
- Вычисление площади и периметра прямоугольника
- Вычисление площади и периметра квадрата
- Вычисление площади и периметра окружности

# Описание каждой функции с примерами вызова
- **Функция для вычисления площади прямоугольника**
    Параметры:
        a (int) - длина стороны прямоугольника
        b (int) - длина другой стороны прямоугольника
    Возвращаемое значение:
        a*b - площадь треугольника
    '''
    def area(a, b):
        return a * b 
    '''
    Пример:
        '''
        from geometric_lib import area
        rectangle_area=area(3,5)
        print(rectangle_area)
        
        '''
    Выходные данные: 15

- **Функция для вычисления периметра прямоугольника**
    Параметры:
        a (int) - длина стороны прямоугольника
        b (int) - длина другой стороны треугольника
    Возвращаемое значение:
        2*(a+b) - периметр треугольника 
    '''
    def perimeter(a, b):
        return 2*(a + b) 
    '''
    Пример:
        '''
        from geometric_lib import perimetr
        rectangle_perimetr=perimetr(3,5)
        print(rectangle_perimetr)
        '''
        Выходные данные: 16

- **Функция для вычисления площади квадрата**
    Параметры:
        a (int) - длина стороны квадрата
    Возвращаемое значение:
        a*a - площадь квадрата 
    '''
    def area(a):
        return a * a
    '''
    Пример:
    '''
    from geometric_lib import area
        square_area=area(2,2)
        print(square_area)
    '''
    Выходные данные: 4

- **Функция для вычисления периметра квадрата**
    Параметры:
        a (int) - длина стороны квадрата
    Возвращаемое значение:
        4*a - периметр квадрата 
    '''
    def perimeter(a):
        return 4 * a
    '''
    Пример:
    '''
    from geometric_lib import perimeter
        perimeter_area=aperimeter(2,2)
        print(perimeter_area)
    '''
    Выходные данные: 8

- **Функция для вычисления площади круга**
    Параметры:
        r(int) - радиус круга
    Возращаемое значение:
        pi*r*r - площадь круга 
    '''
    import math
    def area(r):
        return math.pi * r * r
    '''
    Пример:
    '''
    from geometric_lib import area
        circle_area=area(5)
        print(circle_area)
    '''
    Выходные данные: 78.53981633974483

- **Функция для вычисления периметра круга**
    Параметры:
        r (int) - радиус круга
    Возвращаемое значение:
        2*pi*r - периметр круга
    '''
    def perimeter(r):
        return 2 * math.pi * r
    '''
    Пример:
    '''
    from geometric_lib import perimeter
        circle_perimeter=perimeter(5)
        print(circle_perimeter)
    '''
    Выходные данные: 31.41592653589793

# История изменений
commit fb740d826a68a14b48953c370db7be7b3465223b (HEAD -> develop)
Author: Vadim_E <elezoffv@yandex.ru>
Date:   Fri Oct 11 01:57:22 2024 +0300

    Добавил документацию для функций

commit d078c8d9ee6155f3cb0e577d28d337b791de28e2 (origin/main, origin/HEAD, main)
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:55:29 2021 +0300

    L-03: Docs added

commit 8ba9aeb3cea847b63a91ac378a2a6db758682460
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:54:08 2021 +0300

    L-03: Circle and square addedg


>>>>>>> main

# Math formulas
## Area
- Circle: `S = πR²`
- Rectangle: `S = ab`
- Square: `S = a²`
- Triangle: `S = sqrt(p * (p-a) * (p-b) * (p-c))` where p is semiperimeter

## Perimeter
<<<<<<< HEAD
- Circle: `P = 2πR`
- Rectangle: `P = 2a + 2b`
- Square: `P = 4a`
- Triangle: `P = a + b + c`
=======
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a

>>>>>>> main

