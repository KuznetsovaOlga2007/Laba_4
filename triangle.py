def TriangleArea(a, h):
    '''
    Принимает два числа(сторону треугольника и его высоту проведенную к этой стороне) и возвращает их произведение, деленное на два, т.е. площадь треугольника
        Параметры:
                a (int): первое натуральное число
                h (int): второе натуральное число

        Возвращаемое значение:
            разделенное на два произведение a и h (int)

        Пример работы:
            input: 2, 5
            output: 5
    '''
    return a * h / 2

def TrianglePerimeter(a, b, c):
    '''
    Принимает три числа(стороны треугольника) и возвращает их сумму т.е. периметр треугольника
        Параметры:
                a (int): первое натуральное число
                b (int): второе натуральное число
                c (int): третье натуральное число

        Возвращаемое значение:
            сумма a, b, c (int)

        Пример работы:
            input: 2, 5, 6
            output: 13


    '''
    return a + b + c
