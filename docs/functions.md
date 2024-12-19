## Описание каждой функции с примерами вызова

### Функции для расчёта площади

#### 1. Площадь круга
**Формула:** `S = πR²`

**Пример вызова:**
```cpp
#include <cmath>
#include <iostream>

double calculate_circle_area(double radius) {
    return M_PI * radius * radius;
}

int main() {
    double radius = 5.0;
    std::cout << "Площадь круга: " << calculate_circle_area(radius) << std::endl;
    return 0;
}
```

#### 2. Площадь прямоугольника
**Формула:** `S = ab`

**Пример вызова:**
```cpp
#include <iostream>

double calculate_rectangle_area(double length, double width) {
    return length * width;
}

int main() {
    double length = 10.0;
    double width = 4.0;
    std::cout << "Площадь прямоугольника: " << calculate_rectangle_area(length, width) << std::endl;
    return 0;
}
```

#### 3. Площадь квадрата
**Формула:** `S = a²`

**Пример вызова:**
```cpp
#include <iostream>

double calculate_square_area(double side) {
    return side * side;
}

int main() {
    double side = 6.0;
    std::cout << "Площадь квадрата: " << calculate_square_area(side) << std::endl;
    return 0;
}
```

---

### Функции для расчёта периметра

#### 1. Периметр круга
**Формула:** `P = 2πR`

**Пример вызова:**
```cpp
#include <cmath>
#include <iostream>

double calculate_circle_perimeter(double radius) {
    return 2 * M_PI * radius;
}

int main() {
    double radius = 5.0;
    std::cout << "Периметр круга: " << calculate_circle_perimeter(radius) << std::endl;
    return 0;
}
```

#### 2. Периметр прямоугольника
**Формула:** `P = 2a + 2b`

**Пример вызова:**
```cpp
#include <iostream>

double calculate_rectangle_perimeter(double length, double width) {
    return 2 * (length + width);
}

int main() {
    double length = 10.0;
    double width = 4.0;
    std::cout << "Периметр прямоугольника: " << calculate_rectangle_perimeter(length, width) << std::endl;
    return 0;
}
```

#### 3. Периметр квадрата
**Формула:** `P = 4a`

**Пример вызова:**
```cpp
#include <iostream>

double calculate_square_perimeter(double side) {
    return 4 * side;
}

int main() {
    double side = 6.0;
    std::cout << "Периметр квадрата: " << calculate_square_perimeter(side) << std::endl;
    return 0;
}
