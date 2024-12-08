import circle
import square
import triangle

# Создаем список доступных фигур
figs = ['circle', 'square', 'triangle']
# Создаем список доступных функций
funcs = ['perimeter', 'area']
# Словарь размеров для каждой фигуры и функции
sizes = {
    "perimeter-circle": 1,
    "area-circle": 1,
    "perimeter-square": 1,
    "area-square": 1,
    "perimeter-triangle": 3,
    "area-triangle": 3
}


def calc(fig, func, size):
    """
    Вычисляет периметр или площадь фигуры.

    Параметры:
        fig (str): Название фигуры (например, 'circle').
        func (str): Название функции (например, 'perimeter' или 'area').
        size (list): Список параметров для фигуры.

    Возвращает:
        float: Результат вычисления (периметр или площадь).
    """
    assert fig in figs, f"Figure {fig} is not valid."
    assert func in funcs, f"Function {func} is not valid."

    if fig == 'circle':
        if func == 'perimeter':
            return circle.perimeter(*size)
        elif func == 'area':
            return circle.area(*size)
    elif fig == 'square':
        if func == 'perimeter':
            return square.perimeter(*size)
        elif func == 'area':
            return square.area(*size)
    elif fig == 'triangle':
        if func == 'perimeter':
            return triangle.perimeter(*size)
        elif func == 'area':
            return triangle.area(*size)


if __name__ == "__main__":  # Исправлено здесь
    func = ''
    fig = ''
    size = list()

    # Ввод фигуры
    while fig not in figs:
        fig = input(f"Enter figure name, available are {figs}:\n")

    # Ввод функции
    while func not in funcs:
        func = input(f"Enter function name, available are {funcs}:\n")

    # Ввод параметров фигуры
    expected_size = sizes.get(f"{func}-{fig}", 1)
    while len(size) != expected_size:
        try:
            size = list(map(float, input(
                f"Input {expected_size} sizes for {fig}, separated by space:\n").split()))
            if len(size) != expected_size:
                print(f"Please enter exactly {expected_size} values.")
        except ValueError:
            print("Invalid input. Please enter numbers only.")

    # Вычисление и возврат результата
    try:
        result = calc(fig, func, size)
        print(f"The result of {func} of {fig} is {result:.2f}")
    except Exception as e:
        print(f"An error occurred: {e}")

