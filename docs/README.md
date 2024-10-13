# Общее описание решения (Обновлённая версия)
This code is a Python script for calculating the area and perimeter of shapes such as a circle and a square.
The script allows the user to enter the name of the shape, the desired function (area or perimeter) and the dimensions of the shape.
As a result, the program calculates the value and displays it on the screen.
The script uses the `circle` and `square` modules, which must contain the appropriate functions to perform the calculations.
The input data is checked for correctness, which helps to avoid errors during program execution.

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

## Work of Functions
Functions accepts data depending on the type of figure
for a circle:
	R int() - radius of a circle
for a rectangle:
	a int() - first side
	b int() - second side
for a square:
	a int() - side
for a triangle:
	a int() - first side
	b int() - second side
	c int() - third side
	
for example:
	if we calculate perimeter of circle program gets R and return 2πR
	if we calculate area of triangle, programgets a, b, c and return sqrt(p * (p-a) * (p-b) * (p-c))
	

## Commit history
- b5b0fae727ca72c317c383b39c0af73d6adcd81c (origin/develop) L-04: Update docs for calculate.py
- d76db2ac7f69cc920ae2e6f669fb0671a7fa7d71 L-04: Add calculate.py
- 51c40ebfd0e0b65f52fe5e54740cbb038e492db3 L-04: Doc updated for triangle
- d080c7888b81955bad2ed78d58ad910526b5132a L-04: Triangle added
- d078c8d9ee6155f3cb0e577d28d337b791de28e2 (origin/main, main) L-03: Docs added
- 8ba9aeb3cea847b63a91ac378a2a6db758682460 L-03: Circle and square added


