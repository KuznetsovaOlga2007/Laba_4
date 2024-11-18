import circle
import square
import triangle


figs = ['circle', 'square', 'triangle']
funcs = ['perimeter', 'area']
sizes = {}

def calc(fig, func, size):
	assert fig in figs
	assert func in funcs

	result = eval(f'{fig}.{func}(*{size})')
	return result

if __name__ == "__main__":
	func = ''
	fig = ''
	size = list()
    
	while fig not in figs:
		fig = input(f"Enter figure name, avaliable are {figs}:\n")
	
	while func not in funcs:
		func = input(f"Enter function name, avaliable are {funcs}:\n")

	if fig == 'circle' or fig == 'square':
		while len(size) != sizes.get(f"{func}-{fig}", 1):
			size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square\n").split(' ')))
	else:
		while len(size) != sizes.get(f"{func}-{fig}", 3):
			size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square\n").split(' ')))
	
	res = calc(fig, func, size)
	print(res)



