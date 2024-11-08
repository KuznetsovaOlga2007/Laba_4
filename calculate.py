import circle
import square

figs = ['circle', 'square']
funcs = ['perimeter', 'area']
sizes = {
    'circle': 1,
    'square': 1
}

def calc(fig, func, size):
    assert fig in figs, f"Figure '{fig}' is not supported."
    assert func in funcs, f"Function '{func}' is not supported."

    module = globals()[fig]
    func_to_call = getattr(module, func)
    result = func_to_call(*size)
    return result

if __name__ == "__main__":
    func = ''
    fig = ''
    size = list()

    while fig not in figs:
        fig = input(f"Enter figure name, available are {figs}:\n")
    
    while func not in funcs:
        func = input(f"Enter function name, available are {funcs}:\n")
    
    while len(size) != sizes.get(fig, 1):
        try:
            size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square\n").split(' ')))
        except ValueError:
            print("Please enter valid integer values.")
    
    result = calc(fig, func, size)
    print(f'{func} of {fig} is {result}')
