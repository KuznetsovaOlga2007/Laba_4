
def calc(fig, func, size):
    if fig not in ["circle", "square", "triangle"]:
        raise ValueError(f"Figure '{fig}' is not supported.")
    if func not in ["area", "perimeter"]:
        raise ValueError(f"Function '{func}' is not supported.")
    if fig == "triangle" and func == "area" and len(size) != 3:
        raise TypeError("area() missing 1 required positional argument: 'c'")
