# Импорт пользовательских модулей для расчетов круга и квадрата
import circle
import square

# Списки доступных имен фигур и имен функций
figs = ['circle', 'square']  # доступные имена фигур
funcs = ['perimeter', 'area']  # доступные имена функций

# Словарь для хранения количества параметров размера, необходимых для каждой комбинации функции-фигуры
sizes = {}  # будет заполнен позже

def calc(fig, func, size):
    """
    Рассчитать результат указанной функции для указанной фигуры с заданными параметрами размера.
    
    Аргументы:
        fig (str): имя фигуры (например, 'circle' или 'square')
        func (str): имя функции (например, 'perimeter' или 'area')
        size (list): список параметров размера (например, [radius] для круга или [side_length] для квадрата)
    """
    # Проверка того, что имя фигуры и имя функции являются допустимыми
    assert fig in figs
    assert func in funcs
    
    # Динамический вызов указанной функции из указанного модуля с заданными параметрами размера
    result = eval(f'{fig}.{func}(*{size})')
    
    # Печать результата в консоль
    print(f'{func} of {fig} is {result}')

if __name__ == "__main__":
    # Инициализация переменных для хранения ввода пользователя
    func = ''
    fig = ''
    size = list()
    
    # Запрос имени фигуры у пользователя
    while fig not in figs:
        fig = input(f"Enter figure name, avaliable are: {figs}:\n")
    
    # Запрос имени функции у пользователя
    while func not in funcs:
        func = input(f"Enter function name, avaliable are: {funcs}:\n")
    
    # Запрос параметров размера у пользователя
    while len(size) != sizes.get(f"{func}-{fig}", 1):
        size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square\n").split(' '))
    
    # Вызов функции calc с вводом пользователя
    calc(fig, func, size)