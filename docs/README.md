# Math formulas
## Area
- Circle: S = πR²
- Square: S = a²
## Perimeter
- Circle: P = 2πR
- Square: P = 4a

# Файл circle.py 
Возвращает площадь и периметр круга.

### 1. Area.
```angular2html
def area(r):
    return math.pi * r * r
```
Принимает на вход радиус круга и возвращает его площадь.
#### Пример:
````
print(area(3))
````
Функция принимает значение 3 и возвращает площадь - 9π

### 2.Perimeter
```angular2html
def perimeter(r):
    return 2 * math.pi * r
```
Принимает на вход радиуc круга и возвращает его периметер.
#### Пример:
````
print(perimeter(3))
````
Функция принимает значение 3 и возвращает площадь - 6π

# Файл square.py
Возвращает площадь и периметр квадрата.

### 1. Area.
```angular2html
def area(a):
    return a * a
```
Принимает на вход сторону квадрата и возвращает его площадь.
#### Пример:
````
print(area(3))
````
Функция принимает значение 3 и возвращает площадь - 9

### 2.Perimeter
```angular2html
def perimeter(a):
    return 4 * a
```
Принимает на вход сторону квадрата и возвращает его периметер.
#### Пример:
````
print(perimeter(3))
````
Функция принимает значение 3 и возвращает периметер - 12

## История commits

1. Thu Mar 4 14:54:08 2021 
    - commit hash: 8ba9aeb3cea847b63a91ac378a2a6db758682460
    - changes: "L-03: Circle and square added"
    - author: smartiqa <info@smartiqa.ru>
2. Thu Mar 4 14:55:29 2021 
    - commit hash: d078c8d9ee6155f3cb0e577d28d337b791de28e2
    - changes: "L-03: Docs added"
    - author: smartiqa <info@smartiqa.ru>
