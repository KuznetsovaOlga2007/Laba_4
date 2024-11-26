import circle
import square
import triangle  # Подключаем модуль для треугольника

# Список доступных фигур и функций
figs = ['circle', 'square', 'triangle']
funcs = ['perimeter', 'area']

# Словарь с функциями для расчёта
figure_functions = {
    'circle': {
        'area': circle.area,
        'perimeter': circle.perimeter,
    },
    'square': {
        'area': square.area,
        'perimeter': square.perimeter,
    },
    'triangle': {
        'area': triangle.area,
        'perimeter': triangle.perimeter,
    }
}

# Требуемое количество параметров для каждой фигуры
sizes_required = {
    'circle': 1,  # Радиус
    'square': 1,  # Сторона
    'triangle': 3,  # Три стороны
}


def calc(fig, func, size):
    """
    Выполняет расчёт площади или периметра для указанной фигуры.

    :param fig: str, название фигуры (например, 'circle')
    :param func: str, функция ('area' или 'perimeter')
    :param size: list, параметры для расчёта (например, [3] для круга)
    :return: float, результат расчёта
    :raises ValueError: если переданы некорректные данные
    """
    # Проверяем, что фигура и функция допустимы
    if fig not in figs:
        raise ValueError(
            f"Invalid figure '{fig}', available figures are: {figs}"
        )
    if func not in funcs:
        raise ValueError(
            f"Invalid function '{func}', available functions are: {funcs}"
        )

    # Проверяем количество параметров
    required_size = sizes_required.get(fig, 1)
    if len(size) != required_size:
        raise ValueError(
            f"Wrong parameters. Expected {required_size},got {len(size)}"
        )

    # Проверяем, что все параметры - числа и положительные
    if not all(isinstance(x, (int, float)) for x in size):
        raise TypeError(f"Parameters must be numbers. Got: {size}")
    if any(x <= 0 for x in size):
        raise ValueError(f"Parameters must be positive numbers. Got: {size}")

    # Выполняем расчёт
    try:
        result = figure_functions[fig][func](*size)
        return result
    except Exception as e:
        raise ValueError(f"Error calculating {func} for {fig}: {e}")


if __name__ == "__main__":
    func = ''
    fig = ''
    size = []

    # Ввод фигуры
    while fig not in figs:
        fig = input(f"Enter figure name, available are {figs}:\n")

    # Ввод функции
    while func not in funcs:
        func = input(f"Enter function name, available are {funcs}:\n")

    # Ввод размеров
    while len(size) != sizes_required.get(fig, 1):
        try:
            size = list(map(float, input(
                "Input figure sizes separated by space "
            ).split()))
        except ValueError:
            print("Invalid input. Please enter numeric values.")

    # Расчёт и вывод результата
    try:
        result = calc(fig, func, size)
        print(f"{func.capitalize()} of {fig} is "
              f"{result:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
