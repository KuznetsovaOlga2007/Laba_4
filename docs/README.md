
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


# General description of the solution

This project is a console calculator that allows you to calculate the area and perimeter
of various shapes. The user enters the name of the figure, selects a function (area or perimeter) and enters the required dimensions. The calculator uses mathematical formulas to perform calculations and displays the result on the screen.

The project is developed in Python and uses standard libraries to perform mathematical operations.

# Functions
## Circle
### `def area(r):`
- Calculates the area of a given radius

*Example of a call*
```python
print(area(10))
314.1592653589793
```
### `def perimeter(r):`
- Calculates the length of a circle with a given radius

*Example of a call*
````python
print (perimeter(10))
62.83185307179586
````


## Square
### `def area(a):`
- Calculates the area of a square by a given side

*Example of a call*
```python
print(area(10))
100
```
### `def perimeter(a):`
- Calculates the perimeter of a square by a given side

*Example of a call*
```python
print(perimeter(10))
40
```

## Triangle
### `def area(a, b, c):`
- Calculates the semi-perimeter of a triangle given sides

*Example of a call*
```python
print(area(10, 10, 10))
15.0
```
### `def perimeter(a, b, c):`
-  Calculates the perimeter of a triangle given sides

*Example of a call*
```python
print(area(10, 10, 10))
30
```

## Calculate
### `def calc(fig, func, size):`
- Calculates the area or perimeter of a selected shape based on given sides

*Example of a call*
```python
print (calc('square', 'area', [10]))
100
```

# The history of changes with commit hashes

1. **d76db2a L-04: Add calculate.py**

Added a function to calculate the area and perimeter of shapes

2. **51c40eb L-04: Doc updated for triangle**

Added function description with the examples of calls
3. **d080c78 L-04: Triangle added**

Added a function to calculate the area and perimeter of a triangle
4. **d078c8d (upstream/main, main) L-03: Docs added**

Added documentation for functions
5. **8ba9aeb L-03: Circle and square added**

Added a function to calculate the area and perimeter of circle and square


