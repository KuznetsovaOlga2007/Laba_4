# Math formulas
## Solution steps:
### 1. Realise area function in each type of shapes files:
### Area
- Circle: S = πR²
- Square: S = a²
### 2. Realise perimeter function un each type of shapes files
### Perimeter
- Circle: P = 2πR
- Square: P = 4a
## Functions describe:
### Area in circle.py:
```
def area(r): 
    return math.pi * r * r
```
This function return area of circle by math formula.
#### Example:
```
print(area(5))
```
Will return area of circle with radius 5 and print - 25π.

### Area in square.py:
```
def area(a):
    return a * a
```
This function return area of square by math formula.
#### Example:
```
print(area(5))
```
Will return area of circle with  side 5 and print - 25.

### Perimeter in circle.py:
```
def perimeter(r):
    return 2 * math.pi * r

```
This function return area of square by math formula.
#### Example:
```
print(perimeter(5))
```
Will return area of circle with radius 5 and print - 10π.

### Perimeter in square.py:
```
def perimeter(a):
    return 4 * a
```
This function return area of square by math formula.
#### Example:
```
print(perimeter(5))
```
Will return area of circle with radius 5 and print - 20.
## Commits history
1. Thu Mar 4 14:54:08 2021
   - Commit hash: 8ba9aeb3cea847b63a91ac378a2a6db758682460
   - Changes: "L-03: Circle and square added"


2. Thu Mar 4 14:55:29 2021
    - Commit hash: d078c8d9ee6155f3cb0e577d28d337b791de28e2
    - Changes: "L-03: Docs added"


3. Wed Oct 9 17:51:57 2024
    - Commits hash: 1f3f8f5416485bcc381a782727d6dafac3ae0b02
    - Changes: "add blocks of comments in the functions"