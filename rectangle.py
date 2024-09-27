def area(a, b):
    '''
    Принимает стороны прямоугольника, возврашает площадь прямоугольника.

        Параметры:
            a (int): сторона прямоугольника
            b (int): сторона прямоугольника

        Возвращаемое значение:
            a * b (int): площадь прямоугольника со сторонами a и b

        Примеры использования:
            Входные данные
                a = 3
                b = 4
            Выходные данные:
                area = 12
    '''
    if type(a) != int or type(b) != int:
        return TypeError
    if a < 0 or b < 0:
        return ValueError
    return a * b

def perimeter(a, b):
    '''
    Принимает стороны прямоугольника, возврашает периметр прямоугольника.

        Параметры:
            a (int): сторона прямоугольника
            b (int): сторона прямоугольника

        Возвращаемое значение:
            2 * (a * b) (int): периметр прямоугольника со сторонами a и b

        Примеры использования:
            Входные данные
                a = 3
                b = 4
            Выходные данные:
                perimeter = 14
    '''
    if type(a) == str or type(b) == str:
        return TypeError
    if a < 0 or b < 0:
        return ValueError
    return 2 * (a + b)
