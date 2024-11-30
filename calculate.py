import circle
import square

figs = ["circle", "square"]
funcs = ["perimeter", "area"]
sizes = {
    "perimeter-circle": 1,
    "area-circle": 1,
    "perimeter-square": 1,
    "area-square": 1,
}


def calc(fig, func, size):
    assert fig in figs, f"Unknown figure: {fig}"
    assert func in funcs, f"Unknown function: {func}"
    assert len(size) == sizes.get(
        f"{func}-{fig}", 1
    ), f"Invalid size count for {fig} and {func}"

    result = eval(f"{fig}.{func}(*{size})")
    return result

if __name__ == "__main__":
	func = ''
	fig = ''
	size = list()

	while fig not in figs:
		fig = input(f"Enter figure name, avaliable are {figs}:\n")

	while func not in funcs:
		func = input(f"Enter function name, avaliable are {funcs}:\n")

	while len(size) != sizes.get(f"{func}-{fig}", 1):
		size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square\n").split(' ')))

	calc(fig, func, size)