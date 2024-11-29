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
