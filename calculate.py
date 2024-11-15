import circle
import square
import triangle  # Importing triangle module

# List of available figures
figs = ['circle', 'square', 'triangle']

# List of available functions for calculation
funcs = ['perimeter', 'area']

# Dictionary to store the number of size parameters required for each figure
sizes = {
    'circle': 1,
    'square': 1,
    'triangle': 3
}

# Mapping figure names to their respective modules
fig_modules = {
    'circle': circle,
    'square': square,
    'triangle': triangle
}


def calc(fig: str, func: str, size: list) -> float:
    """
    Calculates and returns the result for the specified figure and function.

    Parameters:
    fig (str): Name of the figure (e.g., 'circle', 'square', 'triangle').
    func (str): Name of the function to calculate (e.g., 'perimeter', 'area').
    size (list): List of parameters for the figure (e.g., radius for circle).

    Returns:
    float: The result of the calculation.

    Example:
    calc('circle', 'area', [5])
    """
    if fig not in figs:
        raise ValueError("Некорректная фигура")
    if func not in funcs:
        raise ValueError("Некорректная функция")

    module = fig_modules[fig]
    func_to_call = getattr(module, func)
    result = func_to_call(*size)
    print(f'{func} of {fig} is {result}')
    return result


if __name__ == "__main__":
    func = ''
    fig = ''
    size = []

    # Request figure name from the user
    while fig not in figs:
        fig = input(f"Enter figure name, available are {figs}:\n")

    # Request function name from the user
    while func not in funcs:
        func = input(f"Enter function name, available are {funcs}:\n")

    # Request figure parameters from the user
    while len(size) != sizes.get(fig, 1):
        try:
            size = list(
                map(
                    int,
                    input(
                        "Input figure sizes separated by space, e.g., 1 for circle and square, 3 for triangle\n"
                    ).split()
                )
            )
        except ValueError:
            print("Please enter valid integer values.")

    # Call the calculation function and output the result
    calc(fig, func, size)
