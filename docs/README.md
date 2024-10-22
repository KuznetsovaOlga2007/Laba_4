# Math formulas

Lib for geometric calculations

## Functions description

### Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = ah

### Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: S = a + b + c

### Circle

- `area` - returns area of circle
- `perimeter` - returns perimeter of circle

Example:

```python
from circle import area, perimeter

area(r=1)
perimeter(r=1)
```

### Triangle

- `area` - returns area of triangle
- `perimeter` - returns perimeter of triangle

Example:

```python
from triangle import area, perimeter

area(a=1, h=1)
perimeter(a=1, b=2, c=3)
```

### Rectangle

- `get_rectangle_area` - returns area of rectangle
- `get_rectangle_area` - returns perimeter of rectangle

Example:

```python
from rectangle import get_rectangle_area, get_rectangle_perimeter

get_rectangle_area(a=1, b=2)
get_rectangle_perimeter(a=1, b=2)
```

### Square

- `area` - returns area of square
- `perimeter` - returns perimeter of square

Example:

```python
from square import area, perimeter

area(a=1)
perimeter(a=1)
```

## Release Notes

```md
### 8ba9aeb3cea847b63a91ac378a2a6db758682460

- Added circle.py and square.py
```

```md
### d078c8d9ee6155f3cb0e577d28d337b791de28e2

- Updated README.md
```

```md
### 599dec455882dcca9c9f3fc6a3c2fcb70c786ac6

- Added rectangle.py
```

```md
### b4c63db61f16a6edca818c109c9c5748477db82f

- Fixed rectangle.py
- Added triangle.py
```
