# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = (a*h)/2

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: P = a + b + c

# Functions
## Circle
### Area calculation
*(r - radius)*
```python
def area(r):
```
> Example: area(6) -> 113.09733552923255

### Perimeter calculation
*(r - radius)*
```python
def perimeter(r):
```
> Example: perimeter(6) -> 37.69911184307752

## Square
### Area calculation
*(a - side of the square)*
```python
def area(a):
```
> Example: area(3) -> 9

### Perimeter calculation
*(a - side of the square)*
```python
def perimeter(a):
```
> Example: perimeter(3) -> 12

## Triangle
### Area calculation
*(a - side of the triangle)*
*(h - triangle height)*
```python
def area(a, h):
```
> Example: area(3, 6) -> 9

### Perimeter calculation
*(a - first side of the triangle)*
*(b - second side of the triangle)*
*(c - third side of the triangle)*
```python
def perimeter(a, b, c):
```
> Example: perimeter(2, 3, 4) -> 9 

## Rectangle
### Area calculation
*(a - rectangle length)*
*(b - rectangle width)*
```python
def area(a, b):
```
> Example: area(3, 5) -> 15

### Perimeter calculation
*(a - rectangle length)*
*(b - rectangle width)*
```python
def perimeter(a, b):
```
> Example: perimeter(3, 5) -> 16 

# Changelog
- [Fixed triangle.py](https://github.com/hrennnn/geometric_lib/commit/2745347fd0ed2e0a2434072e225ef5f9c8308ecc)
- [Added rectangle.py](https://github.com/hrennnn/geometric_lib/commit/36f3bd5b8ddd718c9ea7cac8d939eaf338ba5c5a)
- [L-03: Docs added](https://github.com/hrennnn/geometric_lib/commit/d078c8d9ee6155f3cb0e577d28d337b791de28e2)
- [L-03: Circle and square added](https://github.com/hrennnn/geometric_lib/commit/8ba9aeb3cea847b63a91ac378a2a6db758682460)