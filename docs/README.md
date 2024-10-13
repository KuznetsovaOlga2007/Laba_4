
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
<<<<<<< Updated upstream
=======
- def area(a, h):
- ##
Square:
*S = a?
- Triangle: *S = sqrt(p * (p-a) * (p-b) * (p-c))' where p is semiperimeter
## Perimeter
Circle: *P = 2nR*
Rectangle: *P = 2a + 2b*
Square: 'P = 4a'
Triangle: *P = a + b + c*
# Общее описание решения
## Square
- Задавая одну сторону находит площадь квадрата и его периметр
## Circle
- Задавая радиус находит площадь круга и его периметр
# Описание каждой функции с примерами вызова
## Функции для квадрата 
### area(a) - Нахождение площади квадрата
- Принимает число а (одну из сторон), возвращает квадрат числа а (его площадь)
```
python
def area(a):                        
    return a * a
#(a = 5） 
#(вернет число 25)
```
### perimeter(a) - Нахождение периметра квадрата
- Принимает число а (одну из сторон), возвращает число а умноженное на 4 (его периметр)
```
python 
def perimeter(a):
    return 4 * a
#(a = 5)
#(вернет число 20)
```
## Функции для круга
### area(a)
- Принимает число т (радиус круга), возвращает число п * r (площадь круга)
```
python 
def area(r): #(a = 4)
    return math.pi * I * I
 #(вернет число 50,24)
```
### perimeter（r）
- Принимает число т (радиус круга), возвращает число 2 * п * г (периметр круга)
```
python 
def perimeter(r):
    return 2 * math.pi * r 
#(a=4)
#(вернет число 25,12)
```
# L-03 
- Circle and square added 8ba9aeb3cea847b63a91ac378a2a6db758682460
- Docs added d078c8d9ee6155f3cb0e577d28d337b791de28e2
- Docs added

# L-04 
- Triangle added d080c7888b81955bad2ed78d58ad910526b5132a
- Doc updated for triangle 51c40ebfd0e0b65f52fe5e54740cbb038e492db3
- Add calculate.py d76db2ac7f69cc920ae2e6f669fb0671a7fa7d71
- Update docs for calculate.py  b5b0fae727ca72c317c383b39c0af73d6adcd81c
- Add rectangle.py

# L-05 
- Add user agreement
- Update Docs. Add user agreement info
>>>>>>> Stashed changes

