def area(a):
    '''Принимает число - длину стороны квадрата, возвращает площадь квадрата с заданной стороной'''
    if a <= 0:
        print("error: no such square")
        return -1

    return a * a


def perimeter(a):
    '''Принимает число - длину стороны квадрата, возвращает периметр квадрата с заданной стороной'''
    if a <= 0:
        print("error: no such square")
        return -1

    return 4 * a
