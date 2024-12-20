import circle
import square

# Список доступных фигур и функций
figs = ['circle', 'square']
funcs = ['perimeter', 'area']
sizes = {}

def calc(fig, func, size):
    """
    Вычисляет указанную функцию (например, периметр или площадь) для заданной фигуры.
    
    Параметры:
    fig (str): Имя фигуры (например, 'circle' или 'square').
    func (str): Функция для вычисления ('perimeter' или 'area').
    size (list): Список параметров для функции (например, радиус для окружности или длина сторон для квадрата).
    
    Возвращаемое значение:
    None: Результат функции выводится на экран.
    
    Пример:
    >>> calc('circle', 'area', [5])
    area of circle is 78.54
    """
    # Проверка, что фигура и функция действительны
    assert fig in figs
    assert func in funcs

    # Вычисление и вывод результата
    result = eval(f'{fig}.{func}(*{size})')
    print(f'{func} of {fig} is {result}')

if __name__ == "__main__":
    # Инициализация переменных
    func = ''
    fig = ''
    size = list()
    
    # Запрос имени фигуры
    while fig not in figs:
        fig = input(f"Enter figure name, avaliable are {figs}:\n")
    
    # Запрос имени функции
    while func not in funcs:
        func = input(f"Enter function name, avaliable are {funcs}:\n")
    
    # Запрос размера фигуры (в зависимости от функции и фигуры)
    while len(size) != sizes.get(f"{func}-{fig}", 1):
        size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square\n").split(' ')))
    
    # Вызов функции для расчета
    calc(fig, func, size)
