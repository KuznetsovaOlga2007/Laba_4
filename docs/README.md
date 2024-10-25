# Общее описание
- Нам даны функции нахождения площадей и периметров различных фигур. Мы подаёём одни значения(1-2 аргумента) на вход и получаем готовый ответ


# Math formulas
## Area
- Circle: *(*S = πR²*)*  ***В данной функции мы отправляем радиус и получаем площадь окружности:***
```
  rad = 2
  are = Area(rad)
  return are
```
 **функция вернёт 4π,  что и будет площадью окружности**
- Rectangle: *(*S = ab*)* ***В данной функции мы отправляем две различные стороны прямоугольника и получаем его площадь:***
```
  a = 2
  b = 5
  are = Area(a,b)
  return are
```
 **функция вернёт 10, что и будет площадью прямоугольника**
- Square: S = *(*a²*)* ***В данной функции мы отправляем сторону квадрата и получаем его площадь:***
```
  a = 2
  are = Area(a)
  return are
```
 **функция вернёт 4, что и будет площадью квадрата**

## Perimeter
- Circle: *(*P = 2πR*)* ***В данной функции мы отправляем радиус и получаем периметр окружности:***
```
  rad = 2
  per = Perimetr(rad)
  return per
```
 **функция вернёт 4π,  что и будет периметром окружности**
- Rectangle: *(*P = 2a + 2b*)* ***В данной функции мы отправляем две различные стороны прямоугольника и получаем его периметр:***
```
  a = 2
  b = 5
  per = Perimetr(a,b)
  return per
```
 **функция вернёт 14, что и будет периметром прямоугольника**
- Square: *(*P = 4a*)* ***В данной функции мы отправляем сторону квадрата и получаем его периметр:***
```
  a = 2
  per = Perimetr(a)
  return per
```
 **функция вернёт 8, что и будет периметром квадрата**
# История изменения проекта
- 206198d (origin/feature) L-04: Update square.py
- ed5022e (origin/feature) L-04: Update rectangle.py
- 19a243c (origin/feature) L-04: Update circle.py
- 3049431 (origin/feature) L-04: Update README.md
- 438b89a L-05: Add user agreement
- 6adb962 L-03: Docs added
- 3049431 (origin/feature) L-04: Add rectangle.py
- b5b0fae (origin/develop) L-04: Update docs for calculate.py
- d76db2a L-04: Add calculate.py
- 51c40eb L-04: Doc updated for triangle
- d080c78 L-04: Triangle added
- d078c8d (origin/main, origin/HEAD, main) L-03: Docs added
- 8ba9aeb L-03: Circle and square added
