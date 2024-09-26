def area(a, h):
    ''' Высчитывается площадь треугольника с основанием a и высотой h
            Агрумент a (int) равен основанию треугольника
            Агрумент h (int) равен высоте треугольника
            Возвращаемое значение area(a,h): (float)
                Площадь треугольника с основанием a и высотой h
        Пример запуска:
        area(3,4)
        >> 6
    '''
    return a * h / 2 

def perimeter(a, b, c):
    ''' Высчитывается периметр треугольника
            Агрумент a (int) равен 1-й стороне треугольника
            Агрумент b (int) равен 2-й стороне треугольника
            Агрумент c (int) равен 3-й стороне треугольника
            Возвращаемое значение perimeter(a,b,c): (int)
                Периметр треугольника с сторонами a b c
        Пример запуска:
        perimeter(3,4,5)
        >> 12
    '''
    return a + b + c 