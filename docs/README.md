### How to Use the Calculator:

1. Run the Python script by executing the command:  
   `python calculate.py`
   
2. You will be prompted to enter the name of a shape. The available options are:
   - Circle
   - Square

3. Then, you will be asked to choose the function you want to calculate:
   - Area
   - Perimeter

4. After that, provide the required measurements for the selected shape:
   - For a Circle, enter the **radius**.
   - For a Square, enter the **side length**.

5. Finally, the program will compute and display the result for either the area or perimeter.

---

### Mathematical Formulas:

- **Area Formulas:**
  - Circle: \( S = \pi r^2 \)
  - Square: \( S = a^2 \)
  - Rectangle: \( S = a \times b \)
  - Triangle: \( S = \sqrt{p(p - a)(p - b)(p - c)} \), where \( p \) is the semi-perimeter.
  
- **Perimeter Formulas:**
  - Circle: \( P = 2\pi r \)
  - Square: \( P = 4a \)
  - Rectangle: \( P = 2a + 2b \)
  - Triangle: \( P = a + b + c \)

---

### Program Description:

This Python program helps you calculate the perimeter or area of various geometric shapes, specifically **circle** and **square**. The program dynamically imports functions based on the shape and operation requested, performing the necessary calculations and displaying the result.

---

### Function Descriptions:

#### Circle Area
- **Purpose:** This function calculates the area of a circle.
- **Parameters:**
  - `r` (int): The radius of the circle.
- **Returns:** A float representing the area of the circle.
- **Example Call:** For `r = 5`, the function returns approximately `78.54`.

#### Circle Perimeter
- **Purpose:** This function calculates the perimeter (circumference) of a circle.
- **Parameters:**
  - `r` (int): The radius of the circle.
- **Returns:** A float representing the perimeter of the circle.
- **Example Call:** For `r = 5`, the function returns approximately `31.42`.

#### Square Area
- **Purpose:** This function calculates the area of a square.
- **Parameters:**
  - `a` (int): The length of one side of the square.
- **Returns:** An integer representing the area of the square.
- **Example Call:** For `a = 4`, the function returns `16`.

#### Square Perimeter
- **Purpose:** This function calculates the perimeter of a square.
- **Parameters:**
  - `a` (int): The length of one side of the square.
- **Returns:** An integer representing the perimeter of the square.
- **Example Call:** For `a = 4`, the function returns `16`.

#### Triangle Area
- **Purpose:** This function calculates the area of a triangle.
- **Parameters:**
  - `a, b, c` (int): The lengths of the three sides of the triangle.
- **Returns:** A float representing the area of the triangle.
- **Example Call:** For sides `a = 3`, `b = 4`, `c = 5`, the function returns `6.0`.

#### Triangle Perimeter
- **Purpose:** This function calculates the perimeter of a triangle.
- **Parameters:**
  - `a, b, c` (int): The lengths of the three sides of the triangle.
- **Returns:** An integer representing the perimeter of the triangle.
- **Example Call:** For sides `a = 3`, `b = 4`, `c = 5`, the function returns `12`.

---

This version rephrases the original description while retaining the original meaning and context.
