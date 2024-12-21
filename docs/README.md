<<<<<<< HEAD
[Ссылки на проект в Overleaf] (https://www.overleaf.com/read/rmdhyfxshfrt#796a76) 
# Geometric Library

This Python code defines a library of functions for calculating the area and perimeter of various geometric shapes. It includes calculations for circles, rectangles, squares and triangles.

## Functions

### Circle Calculations

#### `area(r)`
Calculates the area of a circle.

*   **Parameters:**
    *   `r`: The radius of the circle (a numerical value).
*   **Returns:**
    *   The area of the circle (a numerical value).
*   **Example:**
    ```python
    import math
    area_of_circle = area(5)
    print(f"The area of a circle with radius 5 is: {area_of_circle}") # Output: The area of a circle with radius 5 is: 78.53981633974483
    ```
#### `perimeter(r)`
Calculates the perimeter (circumference) of a circle.

*   **Parameters:**
    *   `r`: The radius of the circle (a numerical value).
*   **Returns:**
    *   The perimeter of the circle (a numerical value).
*   **Example:**
     ```python
     perimeter_of_circle = perimeter(5)
     print(f"The perimeter of a circle with radius 5 is: {perimeter_of_circle}") # Output: The perimeter of a circle with radius 5 is: 31.41592653589793
     ```
### Rectangle Calculations

#### `area(a, b)`
Calculates the area of a rectangle.

*   **Parameters:**
    *   `a`: The length of one side of the rectangle (a numerical value).
    *   `b`: The length of the other side of the rectangle (a numerical value).
*   **Returns:**
    *   The area of the rectangle (a numerical value).
*   **Example:**
    ```python
    area_of_rectangle = area(4, 6)
    print(f"The area of a rectangle with sides 4 and 6 is: {area_of_rectangle}") # Output: The area of a rectangle with sides 4 and 6 is: 24
    ```

#### `perimeter(a, b)`
Calculates the perimeter of a rectangle.

*   **Parameters:**
    *   `a`: The length of one side of the rectangle (a numerical value).
    *   `b`: The length of the other side of the rectangle (a numerical value).
*   **Returns:**
    *   The perimeter of the rectangle (a numerical value).
*   **Example:**
     ```python
     perimeter_of_rectangle = perimeter(4,6)
     print(f"The perimeter of a rectangle with sides 4 and 6 is: {perimeter_of_rectangle}") # Output: The perimeter of a rectangle with sides 4 and 6 is: 20
    ```

### Square Calculations

#### `area(a)`
Calculates the area of a square.

*   **Parameters:**
    *   `a`: The length of one side of the square (a numerical value).
*   **Returns:**
    *   The area of the square (a numerical value).
*  **Example:**
     ```python
     area_of_square = area(5)
     print(f"The area of a square with sides of 5 is: {area_of_square}") # Output: The area of a square with sides of 5 is: 25
     ```
#### `perimeter(a)`
Calculates the perimeter of a square.

*   **Parameters:**
    *   `a`: The length of one side of the square (a numerical value).
*   **Returns:**
    *   The perimeter of the square (a numerical value).
*   **Example:**
    ```python
    perimeter_of_square = perimeter(5)
    print(f"The perimeter of a square with sides of 5 is: {perimeter_of_square}") # Output: The perimeter of a square with sides of 5 is: 20
    ```

### Triangle Calculations

#### `area(a, h)`
Calculates the area of a triangle.

*   **Parameters:**
    *   `a`: The length of the base of the triangle (a numerical value).
    *   `h`: The height of the triangle (a numerical value).
*   **Returns:**
    * The area of the triangle (a numerical value).
* **Example:**
     ```python
     area_of_triangle = area(5, 6)
     print(f"The area of a triangle with base 5 and height 6 is: {area_of_triangle}") # Output: The area of a triangle with base 5 and height 6 is: 15.0
     ```

#### `perimeter(a, b, c)`
Calculates the perimeter of a triangle.

*   **Parameters:**
    *   `a`: The length of the first side of the triangle (a numerical value).
    *   `b`: The length of the second side of the triangle (a numerical value).
    *   `c`: The length of the third side of the triangle (a numerical value).
*   **Returns:**
    * The perimeter of the triangle (a numerical value).
*  **Example:**
     ```python
     perimeter_of_triangle = perimeter(3, 4, 5)
     print(f"The perimeter of a triangle with sides 3, 4, and 5 is: {perimeter_of_triangle}") # Output: The perimeter of a triangle with sides 3, 4, and 5 is: 12
     ```
## Project Modification History

| Commit Hash                            |             Description         |
|----------------------------------------|---------------------------------|
|1d86eb5cea14318ea7b3d0c561ff07c0bc6845d8 new file has been added
d078c8d9ee6155f3cb0e577d28d337b791de28e2 L-03: Docs added
8ba9aeb3cea847b63a91ac378a2a6db758682460 L-03: Circle and square added
=======

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

>>>>>>> b5b0fae727ca72c317c383b39c0af73d6adcd81c
