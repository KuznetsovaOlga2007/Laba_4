import circle
import square

"""
Программа выполняет вычисление заданной функции (площадь или периметр) для указанной фигуры (круг или квадрат)
на основе переданных размеров фигуры.
Параметры: строка, строка, параметр фигуры.
Возвращаемое значение: площадь или периметр фигуры в виде числа.
"""

figs = ['circle', 'square']
funcs = ['perimeter', 'area']
sizes = {'circle': 1, 'square': 1}


def calc(fig, func, size):
    if fig not in figs:
        raise ValueError(f"Invalid figure name '{fig}'. Expected one of {figs}.")

    if func not in funcs:
        raise ValueError(f"Invalid function '{func}'. Expected one of {funcs}.")

    if not all(isinstance(s, (int, float)) and s > 0 for s in size):
        raise ValueError("All size parameters must be positive numbers.")

    if fig == "circle":
        if func == "area":
            return circle.area(*size)
        elif func == "perimeter":
            return circle.perimeter(*size)
    elif fig == "square":
        if func == "area":
            return square.area(*size)
        elif func == "perimeter":
            return square.perimeter(*size)


if __name__ == "__main__":
    func = ''
    fig = ''
    size = []

    while fig not in figs:
        fig = input(f"Enter figure name, available are {figs}:\n")

    while func not in funcs:
        func = input(f"Enter function name, available are {funcs}:\n")

    while len(size) != sizes.get(fig, 1):
        try:
            size = list(map(float, input(f"Input {sizes[fig]} size(s) for {fig} separated by space:\n").split()))
        except ValueError:
            print("Invalid input. Please enter numbers only.")

    try:
        result = calc(fig, func, size)
        print(f"{func} of {fig} is {result}")
    except ValueError as e:
        print(f"Error: {e}")
