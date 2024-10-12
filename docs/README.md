
# How to use calculator:
1. Run `python calculate.py`
2. Enter the figure name. Available are Circle, Square.
3. Enter the function: Area or Perimeter.
4. Enter figure sizes. Radius for circle, one side for square.
5. Get the answer!

* Example 1: Circle Perimeter
 	+ Input: Figure name: circle, Function name: perimeter, Size: 10
	+ Output: perimeter of circle is 31.41592653589793
* Example 2: Square Area
	+ Input: Figure name: square, Function name: area, Size: 5
	+ Output: area of square is 25
* Example 3: Circle Area
	+ Input: Figure name: circle, Function name: area, Size: 10
	+ Output: area of circle is 314.1592653589793

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

# Calculator code breakdown:
**Step 1: Importing Modules**

* The code starts by importing two modules: `circle` and `square`. These modules are assumed to contain functions for calculating the perimeter and area of each shape.

**Step 2: Defining Variables**

* Three lists are defined:
	+ `figs`: a list containing the figure names, which are `circle` and `square`.
	+ `funcs`: a list containing the function names, which are `perimeter` and `area`.
	+ `sizes`: an empty dictionary that will be used to store the number of sizes required for each figure and function combination.

**Step 3: Defining the `calc` Function**

* The `calc` function is defined, which takes three arguments:
	+ `fig`: the figure name (either `circle` or `square`).
	+ `func`: the function name (either `perimeter` or `area`).
	+ `size`: a list of sizes required for the calculation.
* The function asserts that the figure and function names are valid, and then uses the `eval` function to dynamically call the corresponding function from the imported modules.
* The result of the calculation is printed to the console.

**Step 4: Main Program**

* The main program starts by initializing three variables:
	+ `fig`: an empty string to store the figure name.
	+ `func`: an empty string to store the function name.
	+ `size`: an empty list to store the sizes required for the calculation.

**Step 5: Inputting Figure Name**

* A `while` loop is used to input the figure name from the user. The loop continues until a valid figure name is entered (either `circle` or `square`).

**Step 6: Inputting Function Name**

* Another `while` loop is used to input the function name from the user. The loop continues until a valid function name is entered (either `perimeter` or `area`).

**Step 7: Inputting Sizes**

* A third `while` loop is used to input the sizes required for the calculation. The loop continues until the correct number of sizes is entered, which is determined by the `sizes` dictionary. For example, if the figure is a circle and the function is perimeter, only one size is required.

**Step 8: Calling the `calc` Function**

* Once the figure name, function name, and sizes are input, the `calc` function is called with these arguments.

# History of changes

* Early Development (March 2021)
         +The project started with the addition of circle and square shapes (commit `8ba9aeb3cea847b63a91ac378a2a6db758682460` by `smartiqa` on March 4, 2021)
         +Docs were added for the initial shapes (commit `d078c8d9ee6155f3cb0e577d28d337b791de28e2` by `smartiqa` on March 4, 2021)
* Feature Branch Development (March 2021)
         + A feature branch was created, and the following changes were made:
         + Rectangle shape was added (commit `30494317cde4419be779c14306561e0eaa78b88b` by `Daniil.K` on March 30, 2021)
         + Calculate.py was added (commit `d76db2ac7f69cc920ae2e6f669fb0671a7fa7d71` by `Daniil.K` on March 30, 2021)
         + Docs were updated for calculate.py (commit `b5b0fae727ca72c317c383b39c0af73d6adcd81c` by `Daniil.K` on March 30, 2021)
* Main Branch Development (March 2021)
         + Triangle shape was added (commit `d080c7888b81955bad2ed78d58ad910526b5132a` by `smartiqa` on March 26, 2021)
         + Docs were updated for triangle (commit `51c40ebfd0e0b65f52fe5e54740cbb038e492db3` by `smartiqa` on March 26, 2021)
* Release Branch Development (April 2021)
         + A release branch was created, and the following changes were made:
         + User agreement was added (commit `438b89a1dfc58d90e9036fe431771427965cd1ff` by `Danny` on April 19, 2021)
         + Docs were updated with user agreement info (commit `86edb1c3dd57fa9abc7ba2ec7052507938084727` by `Danny` on April 19, 2021)
       