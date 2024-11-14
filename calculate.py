figs = ['circle', 'square']
funcs = ['perimeter', 'area']
sizes = {}


def calc(fig, func, size):
    assert fig in figs, f"Unknown figure: {fig}"
    assert func in funcs, f"Unknown function: {func}"

    return eval(f'{fig}.{func}(*{size})')


if __name__ == "__main__":
    func = ''
    fig = ''
    size = []

    while fig not in figs:
        fig = input(f"Enter figure name, available are {figs}:\n")

    while func not in funcs:
        func = input(f"Enter function name, available are {funcs}:\n")

    while len(size) != sizes.get(f"{func}-{fig}", 1):
        size = list(
            map(
                int,
                input(
                    "Input figure sizes separated by space\n"
                ).split()
            )
        )

    calc(fig, func, size)
